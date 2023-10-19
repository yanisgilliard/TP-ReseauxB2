# TP1 : Maîtrise réseau du poste
## I. Basics
### ☀️ Carte réseau WiFi
````
PS C:\Users\yanis> ipconfig
[...]
Carte réseau sans fil Wi-Fi :

   Adresse physique . . . . . . . . . . . : 90-E8-68-62-F0-A7
````

````
PS C:\Users\yanis> ipconfig
[...]
Carte réseau sans fil Wi-Fi :

   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.235(préféré)
````

Masque de sous réseau du réseau LAN :
 - en CIDR : ``10.33.64.0/20``
 - en notation décimale : ``255.255.240.0``

 ### ☀️ Déso pas déso
 Adresse de réseau du LAN : `` 10.33.64.0``
 
 Adresse du broadcast : `` 10.33.79.255 ``

 Adresse IP disponible : ``4096 ``

### ☀️ Hostname
````
PS C:\Users\yanis> hostname
yanis
````

### ☀️ Passerelle du réseau
IP passerelle réseau :
````
PS C:\Users\yanis> ipconfig
[...]
Carte réseau sans fil Wi-Fi :

   Passerelle par défaut. . . . . . . . . : 10.33.79.254
````
MAC passerelle réseau : 
````
PS C:\Users\yanis> arp -a 10.33.79.254

Interface : 10.33.76.235 --- 0xf
  Adresse Internet      Adresse physique      Type
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
````

### ☀️ Serveur DHCP et DNS
L'adresse IP du serveur DHCP qui m'a filé une IP :
````
PS C:\Users\yanis> ipconfig
[...]
Carte réseau sans fil Wi-Fi :

   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
````
L'adresse IP du serveur DNS que j'utilise quand je vais sur internet :
````
PS C:\Users\yanis> ipconfig
[...]
Carte réseau sans fil Wi-Fi :

   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
````

### ☀️ Table de routage
````
PS C:\Users\yanis> netstat -r
[...]
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.235     35
````

## II. Go further
### ☀️ Hosts ?
````
PS C:\Users\yanis> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=12 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=21 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 11ms, Maximum = 21ms, Moyenne = 14ms
````

## ☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...
````
PS C:\Users\yanis> netstat -a -n -b
 [msedge.exe]
  TCP    192.168.1.28:54537     192.229.221.95:80      TIME_WAIT
  TCP    192.168.1.28:54538     20.223.46.67:443       TIME_WAIT
  TCP    192.168.1.28:54541     13.107.246.42:443      ESTABLISHED
````
L'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo : ``13.107.246.42``

Le port du serveur auquel vous êtes connectés : ``443``

Le port que votre PC a ouvert en local pour se connecter au port du serveur distant : ``54541``

### ☀️ Requêtes DNS
A quelle adresse IP correspond le nom de domaine www.ynov.com : 
````
PS C:\Users\yanis> nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:ae9
          2606:4700:20::ac43:4ae2
          2606:4700:20::681a:be9
          172.67.74.226
          104.26.11.233
          104.26.10.233
````

A quel nom de domaine correspond l'IP ``174.43.238.89`` :
````
PS C:\Users\yanis> nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
````

### ☀️ Hop hop hop
````
PS C:\Users\yanis> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.10.233]
avec un maximum de 30 sauts :

  1     5 ms     2 ms     3 ms  10.33.79.254
  2     5 ms     4 ms     4 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     4 ms     6 ms     5 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     7 ms     6 ms     6 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    14 ms    13 ms    15 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    12 ms    11 ms    11 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    12 ms    16 ms    12 ms  141.101.67.48
  8    14 ms    13 ms    11 ms  141.101.67.54
  9    14 ms    12 ms    12 ms  104.26.10.233

Itinéraire déterminé.
````

### ☀️ IP publique
````
PS C:\Users\yanis> curl https://ifconfig.me/


StatusCode        : 200
StatusDescription : OK
Content           : 195.7.117.146
RawContent        : HTTP/1.1 200 OK
                    access-control-allow-origin: *
                    x-envoy-upstream-service-time: 0
                    strict-transport-security: max-age=2592000; includeSubDomains
                    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=259200...
Forms             : {}
Headers           : {[access-control-allow-origin, *], [x-envoy-upstream-service-time, 0], [strict-transport-security,
                    max-age=2592000; includeSubDomains], [Alt-Svc, h3=":443"; ma=2592000,h3-29=":443"; ma=2592000]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 13
````

### ☀️ Scan réseau
````
PS C:\Users\yanis> arp -a

Interface : 192.168.159.1 --- 0x4
  Adresse Internet      Adresse physique      Type
  192.168.159.255       ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique

Interface : 192.168.75.1 --- 0x8
  Adresse Internet      Adresse physique      Type
  192.168.75.254        00-50-56-eb-ca-a3     dynamique
  192.168.75.255        ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

Interface : 10.10.10.1 --- 0xb
  Adresse Internet      Adresse physique      Type
  10.10.10.255          ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique

Interface : 10.3.1.3 --- 0xc
  Adresse Internet      Adresse physique      Type
  10.3.1.255            ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique

Interface : 10.33.76.235 --- 0xf
  Adresse Internet      Adresse physique      Type
  10.33.67.35           88-d8-2e-eb-70-ad     dynamique
  10.33.78.173          40-ed-00-58-b9-cc     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

Interface : 192.168.200.1 --- 0x15
  Adresse Internet      Adresse physique      Type
  192.168.200.254       00-50-56-ed-6d-f2     dynamique
  192.168.200.255       ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

Interface : 169.254.11.249 --- 0x18
  Adresse Internet      Adresse physique      Type
  169.254.255.255       ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique
````

### ☀️ Capture ARP
J'ai utilisé le filtre "ARP" 
./captures/capture-arp.pcap

J'ai ultilsé le filtre "DNS"
````
PS C:\WINDOWS\system32> nslookup youtube.com
````

