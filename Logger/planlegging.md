Planlegging

# My Project

[Intro](#Intro/plan/Overview)  
*[Sikkerhet](#sikkerhet)
[MVP](#MVP)

[Planen](#Planen)

[Endringer av Planen/notater](#endringer-av-planen)

[Veiledning](#Notater)

[Kilder](#Kilder)

[Gamle ting for dokumentasjon](#Gammelt)


## Intro/plan
Jeg tenker å lage en minecraft server hvor man kan såsagt gå inn og spille der, med en nettside som viser antall spillere i serveren, og potensielt et mini-map for det trenger jeg,
en nettside,
informasjon om hvordan hoste minecraft-server,
raspberry pi med linux OS for hosting av server og nettside
og andre ting sikkert jeg ikke husker nå.

  Så etter å ha sammenlingt burde raspberry pi sin CPU kan funke spesielt siden den har 8 gb ram og ok lagringsplass
 men du kan også spørre hvorfor jeg lager en minecraft java server og ikke bedrock, 1, Java er bedre, 2 Det er mere guider for java/plugins og annet og lettere for meg.


## Sikkerhet
Firewall, etc etc

## MVP
    Trenger,
    --
    Server hostet på Raspberry pi 4, Java, Minecraft server setup/installation.

    Nice to have,
    --
    Player counter, Server status on/off,  Server wi-fi/connection, Nettside.


## Planen (11/12/24)
Lage en minecraft server i Raspberry Pi 4, med Ubuntu OS.
Lage en simpel placeholder nettside til å vise antall spillere, Ping, Status til serveren.
Så kan jeg starte med plugins eventuelt hvis det funker med java server.

## Endringer av planen

11/13 
  Usikker på om man kan ha plugins for java skal finne ut

  Sjekket om Raspberry pi 4 kan håndtere å hoste en minecraft server so det kan pga 1.5 hz og minimum er ca 3 som burde holde

  har greid å hoste det så den og spille der så den kan.



## 6. Minecraft server


    Sette opp minecraft server guide konkret hvis jeg noen gang trenger det igjen
    Ubuntu OS RPi 4b 8GB 32GB 
    Either SSH or do it manually/copy paste into terminal 
    Install java usually 17,21
    1. sudo apt install openjdk- VERSION -jre 

    Create a directory/folder for your minecraft server
    2.  mkdir ~/minecraft
    cd ~/minecraft

    3. Install minecraft server and move it to the minecraft directory/folder or use 'wget' in minecraft server directory

    4. Edit the Eula.txt to say true and update any server.properties you want or use nano to adjust settings like gamemode, difficulty.

    5. java -Xmx1024M -Xms1024M -jar server.jar nogui
    -Xmx, -Xms to adjust amount of ram. and start the server.


## 6.1 Player tracker

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





## Gammelt
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

bruk av Co-pilot og chat-gpt for hjelp med å sette opp minecraft-server (gi mere konkret guide)
