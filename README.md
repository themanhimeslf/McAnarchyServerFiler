Sjekk mappen "Logger" for dokumentasjon

Planlegging


# Start
- [Planen](#Planen)
- [Hva man trenger](#prerequisities)
- [MVP](#MVP)
- [Sikkerhet](#sikkerhet)

# Other
 - [Kilder](#Kilder)
 - [Gamle ting for dokumentasjon](#Gammelt)

## Prerequisities
 - Raspberry pi 4, eller noe annet så lenge den kan runne linux 
 - Website
 - Nødvendig installerte programmer og filer, f.eks: Pip/python, mcstatus, java, MCserver filer.


## Planen
Lage en minecraft server som runner i Rasperry pi 4,
Nettside med en butikk kanskje til serveren/mc,
Player tracker, status etc til serveren.

## MVP
Trenger
    
- Raspberry pi
- Nettside (HTML&CSS (python,flask etc))
- MC Server

Nice to have,
    
- Player counter
- Server status on/off
- Server wi-fi/connection status

## Sikkerhet
for å beskytte mot eksterne trusler som DDoS og uautorisert tilgang.

Fysiske

    2 Komponenter.
    Laptop & Raspberry Pi.

Digitalt

    Backups på github/pc
    SSH/Internet
    DDOS til server/raspberry pi


deny/allow

    sudo ufw deny/allow (port)
Porter tilatt
22 - for SSH
25565 - for Minecraft
5000 - For nettsiden
"apache" - for apache

Porter stengt
23 - gammel telnet protocol, gir ut data, inkludert passord i "plain"   text, sårbar mot "man in the middle"
21 - som telnet, gammel protocol.
139 - windows fil deling og eternalblue angrep
445 - samme


hvorfor stenge porter? åpene porter gir potensiell angrepsmål, 
Å stenge unødvendige porter reduserer risikoen for at angripere bruke sårbarheter.

(hva gjør firewall mest traffikk filtering den analyserer data pakker og tillater/nekter dem basert på ip,port og andre greier)
Kan også logge og følge på trafikken





<!-- 
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
 -->

## Kilder
https://www.cherryservers.com/blog/minecraft-server-ubuntu#1-install-minecraft-on-ubuntu-java-edition 
https://minecraft.fandom.com/wiki/Server/Requirements/Dedicated#Unix_(Linux,_BSD,_macOS)
https://www.intel.com/content/www/us/en/products/sku/33910/intel-core2-duo-processor-e8400-6m-cache-3-00-ghz-1333-mhz-fsb/specifications.html
https://minecraft.fandom.com/wiki/Server/Requirements
https://www.reddit.com/r/LinuxOnThinkpad/comments/1bblq0j/anyone_knows_how_to_make_a_minecraft_server_with/
