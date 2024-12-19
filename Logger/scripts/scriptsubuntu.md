
---
mc scripts

Start script

        ./"scriptname"

JAVA MINECRAFT SERVER
------------

        #!/bin/bash

        # Starter mc server
        echo "Starter Minecraft-server..."
        java -Xmx1024M -Xms1024M -jar server.jar

        echo "Minecraft server er oppe"

----- Add onto previous to check if worked  remove previous "minecraft server er oppe"

        if [ $? -eq 0 ]; then
                echo "Server startet"
        else
                echo "Server startet ikke"
        fi

        echo "Minecraft server er oppe"




<!-- # Starter getplayer
echo "Starter getplayer.py..."
nohup python3 getplayer.py > getplayer.log 2>&1 & -->