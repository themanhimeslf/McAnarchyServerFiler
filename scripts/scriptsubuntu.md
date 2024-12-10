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
