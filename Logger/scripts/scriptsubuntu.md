
[RUNLINES](#runlines)  
[Scripts](#scripts)  

## runlines
---
hvis starter ny ubuntu/linux os

$ sudo apt update

$ sudo apt upgrade

$ sudo apt install openssh-server

$ sudo ufw enable

$ sudo ufw allow 22

## scripts
---
mc scripts

Start script

JAVA
    start.sh
    #!/bin/bash
    java -XmxXXXXM -jar server.jar nogui
---------

SPIGOT
    start.sh
    #!/bin/sh
    java -Xms#G -Xmx#G -XX:+UseG1GC -jar spigot.jar nogui

For å ha GUI bytt "nogui" til "gui"

Så for begge
    chmod +x start.sh

    Bruk 'start.sh' til å starte deretter.


Andre scripts
---