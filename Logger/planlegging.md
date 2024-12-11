Planlegging

# My Project

[Intro](#Intro/plan/Overview)  

[Sikkerhet](#sikkerhet)

[MVP](#MVP)

[Planen](#Planen)

[6. Minecraft veiledning](#6-minecraft)

[6.1 Minecraft JAVA](#6.1-Minecraft-server-JAVA)

[6.2 Minecraft Spigot](#6.2-Minecraft-server-SPIGOT/BUILDTOOLS)

[6.3 Minecraft tracker Java](#6.3-Player-tracker-JAVA)


[Kilder](#Kilder)

[Gamle ting for dokumentasjon](#Gammelt)

## Planen (11/12/24)
Lage en minecraft server i Raspberry Pi 4, med Ubuntu OS.
Lage en simpel placeholder nettside til å vise antall spillere, Ping, Status til serveren.
Så kan jeg starte med plugins eventuelt hvis det funker med java server.

## Sikkerhet


## MVP
    Trenger,
    --
    MariaDB, på raspberry pi, Nettside/butikk
    Minecraft server
    

    Nice to have,
    --
    Player counter, Server status on/off,  Server wi-fi/connection status, Minecraft server






## 6. Minecraft
Guide til å sette opp alt igjen hvis ting blir bricked

Ubuntu OS RPi 4b 8GB 32GB 
Either SSH or do it manually/copy paste into terminal 

Notater/Prerequisities:

    VIKTIG
    Installer riktig/den versjonen av java for den versjonen av minecraft du vil ha
        sudo apt install openjdk-VERSJON-jre 
    
    For connection
        Sudo ufw enable
        Sudo ufw allow 22/tcp
        Sudo ufw allow 25565/tcp 
    
    VIKTIG
    Lag en mappe f.eks "minecraft" og put filene til serveren oppi der/cd inn dit (trenger ikke bare nyttig)

---
## 6.1 Minecraft server JAVA
    Ha installert java

1. Create a directory/folder for your minecraft server (trenger ikke bare nyttig)

        mkdir ~/minecraft
        cd ~/minecraft
2. Install minecraft server and move it to the minecraft directory/folder or use 'wget' og link in minecraft server directory

3. Edit the Eula.txt to say true and update any server.properties you want or use nano to adjust settings like gamemode, difficulty.

4. -Xmx, -Xms to adjust amount of ram. and start the server. (fjern nogui for gui)

        java -Xmx1024M -Xms1024M -jar server.jar nogui


## 6.2 Minecraft server SPIGOT/BUILDTOOLS
Ha installert java og Git eventuelt
    1. installer nyeste "BuildTools.jar" fra nettside eller med 'wget'

2. så CD in i mappa "minecraft" f.eks. og run denne

        java -jar BuildTools.jar
3.  nogui = ingen grafisk interface fjern eller ha hvis du vill Xmx2g for hvor mye ram, xms for start ram

            java -Xmx2G -Xms1G -jar "navn til serveren.jar" nogui
    (du kan bytte navne til serveren med 'mv spigot-"" server.jar')
    

Viktig: Sa det før men sier det igjen, å sette opp en minecraft server er lett, men bare at jeg gjør det for første gang og vil bare gjøre alt rett.





## Gammelt
Intro: dette et enten ting som er gammelt eller ikke trengs men likavel her for dokumentasjon

## 6.3 Player tracker JAVA

    ---MINETRACK----
    https://github.com/Cryptkeeper/Minetrack
        you need Node.Js for this you can install it using:
        1.  sudo apt update
        sudo apt install nodejs npm

    Clone the Minetrack repository from GitHub:
        2.  git clone https://github.com/Cryptkeeper/Minetrack.git
            cd Minetrack

    Install the required dependencies:
        3.  npm install
            Configure Minetrack: Edit the config.json file to customize settings such as server IP, port, and update speed.

    Run Minetrack: Start the Minetrack server:
        4.  node main.js

    Open your web browser and go to http://<your-server-ip>:8080 to view the player counter and other statistics.

    ---SERVERSTATS---

    Follow the installation instructions on this github page.
    https://github.com/diced/ServerStats

    Customize the settings to match your server's requirements.

    Open your web browser and go to the provided URL to view the player counter and other statistics.

    --VIS PÅ NETTSIDE

        Use a script to fetch the player count data from Minetrack or ServerStats. (press the github/yt for whatever you chose)

        Use HTML and JavaScript to show the player count on your website.

        https://www.youtube.com/watch?v=Zjt0p7VoP3E
        https://github.com/leonardosnt/mc-player-counter
---

 Del 2 (gammelt)
Jeg må finne ut hvordan lage en minecraft server bare og eventuelt connecte til den, 
så må jeg fikse plugins evt med js eller installert fra 
forhånd til å vise antall spillere, ping og kanskje et minimap av det.

del 3 (gammelt)
Først sette opp minecraft server,
så nettside,
så player count tracker.

Først finne ut om det en gang går å runne en minecraft server på raspberry pi 4, hvis det fungerer og jeg greier å connecte går 
jeg till neste stege, (mvp)


## Kilder
https://www.cherryservers.com/blog/minecraft-server-ubuntu#1-install-minecraft-on-ubuntu-java-edition 
https://minecraft.fandom.com/wiki/Server/Requirements/Dedicated#Unix_(Linux,_BSD,_macOS)
https://www.intel.com/content/www/us/en/products/sku/33910/intel-core2-duo-processor-e8400-6m-cache-3-00-ghz-1333-mhz-fsb/specifications.html
https://minecraft.fandom.com/wiki/Server/Requirements
https://www.reddit.com/r/LinuxOnThinkpad/comments/1bblq0j/anyone_knows_how_to_make_a_minecraft_server_with/
