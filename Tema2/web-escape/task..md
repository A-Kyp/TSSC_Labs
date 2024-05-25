# Poli Redemption / Prison Break

Due to a series of regrettable decisions in life, you find yourself imprisoned
inside the super-max facility called "Poli".
After four years of torment and misery, you finally decide to put it all behind:
the great escape!

You have limited access (max. 30 minutes per session) to the PFE server
(Penitentiary Front End), where you can log in with your given credentials
(private key) and must escalate your access by carefully exploiting the
infrastructure.

You outline your plan and hope everything goes as expected:

0. log into the system and explore it; where is the main website hosted?
1. find the web portal and enter inside (try the default password); you'll soon
   find out that you have no friends and your access rights are limited, but you
   get your first flag ;)
2. find the credentials to some other account (the security guard seems
   prone to mistakes, check the network traffic!);
3. time to hack the dean! let's try an XSS attack... target the password change
   form, maybe?;
4. don't forget about the DBA! as the dean, ask him if he can do some SQL
   queries for you (e.g., count the number of inmates); maybe you can find
   a way to inject other stuff into them?
5. Just for the lulz (and a flag!), try to obtain the website's source code
   using just public accessible resources! git it?
6. before leaving, you need to create a diversion (remember: snipers on rooftops)...
   I know! delete the penitentiary's website and wait for the insurrection to
   unfold (keep the shell open to get the final flag ;) )

For each of the subtasks above (1-6, excl. 0), you will find a specific flag
which you will need to persist as proof of your deeds (so... total = 6 flags,
5 required for 100% completion).

Also beware: the jail container is reset everytime you disconnect, so it's
mandatory to save anything locally (don't worry, initial credentials / flags
found will remain the same).

The challenges are mostly linear: you should complete them in order (using
the privilege escalation approach)!

After each successful account hijack, in case you applied a password changing
vulnerability, make sure to take note of the original password for easily
continuing the assignment when the instance is reset (printed inside the web
development console -- you should have it active all the time ;)).

DISCLAIMER: ALL NAMES, CHARACTERS, AND INCIDENTS PORTRAYED IN THIS ROLE-PLAYING
GAME ARE FICTITIOUS. ANY RESEMBLANCE TO REAL PERSONS, LIVING OR DEAD, IS PURELY
COINCIDENTAL KTHX.


Access instructions:
====================

You will use SSH Tunnel Forwarding to access the website (after finding its
address and running the tunneling script from your shell container, ofc) by
going to http://localhost:8080 from your browser.

Scripts are provided (bash and powershell), though they might need minor tweaks.
Here's how the infrastructure works:

The server spawns individual Docker containers (including database) for each SSH
user session and allocates a random port to use for forwarding the HTTP
protocol, so we will use the OpenSSH client connection multiplexing feature to
keep the session open throughout this process:

- the SSH client will establish a persistent connection to the task server; the
  server will allocate dedicated resources to your client (i.e., random
  container port);
- script will ask the server to return your random web port number;
- after that, it will configure SSH to forward the port previously discovered as
  ':8080' on your machine;
- finally, the script will start the shell container; from now on, keep the
  terminal up and you will be able to access the website using a browser on your
  local machine (after reaching that task);
- if you close the connection, the server will clean up all resources
  allocated for you (so WARNING: everything you posted / modified on any container
  is lost, you will need to repeat some steps again, so make sure to record
  them e.g. in a readme; the flags / credentials / other variables are static
  and do not change between your personalized instances); there is also a 20m
  time limit for each connection!

**Note for Windows users**: OpenSSH for Windows doesn't support control master
/ session multiplexing. Try to use WSL (Windows Subsystem for Linux) if
possible. Otherwise, install Putty and Plink (command line client, bundled if
you use the Putty installer) and use the provided Powershell script
(`connect-putty.ps1`, read the script's code).
With Putty, don't forget to convert the private SSH key to PPK format (it
doesn't speak PEM). Ofc, Google it!

For modern, POSIX-compatible OSes, the bash script should work out of the box.
For WSL2, you might need to use the Linux virtual machine's IP address instead
of 'localhost' when accessing port 8080 in your browser.


Notes / hints:
==============

Grouped by task:

0. you have several network scanning utilities installed, check them out ;)
1. you must first start the tunnel to the discovered server; log in with the
   usual credentials ;) the flag may be hidden in plain sight :P
2. use your shell, see hint for #0; still don't get it? check packet contents
   for more hints (see manpage); note: wait for at least 1 minute to make sure
      you capture some requests; after logging in as the guard, the flag is in
      there, this time a bit more concealed :P
3. note that you can only send messages to friends... so find an account which
   is friends with the dean and see if you can trick him into changing its
   password! Check out the HTML/JS source code for more hints ;) 
4. Mr. DBA is not very responsive... fortunately, he built a BOT answering
   requests from the higher-ups ;) as dekhan, you'll need to use it to change
   the password of Lord Rekt0r himself in order to access the prison admin
   interface!
5. check manual at repository layout; you use zlib-flate to manually decode
   objects, or write a Python script ;)) unfortunately, commits will change on
   each sesssion, so make sure to scrape everything you require right away!
6. a dark crusader will contact and assist you (check your student account) for
   this last difficult task; although he's a bit crazy, he should prove himself
   useful ;) after doing the deed, patiently wait for the action to unfold
   (in your shell).

Remember: 5 flags + 1 bonus!

