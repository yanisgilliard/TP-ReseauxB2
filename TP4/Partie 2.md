# II. You say dev I say good practices

- [II. You say dev I say good practices](#ii-you-say-dev-i-say-good-practices)
  - [1. Args](#1-args)
  - [2. Logs](#2-logs)
    - [A. Logs serveur](#a-logs-serveur)
    - [B. Logs client](#b-logs-client)
    - [C. NOTE IMPORTANTE](#c-note-importante)

## 1. Args

🌞 **`bs_server_II1.py`**

[Fichier](https://github.com/yanisgilliard/TP-ReseauxB2/blob/cf4e7b15de3d7a395bd85240697a66ca0e83d84c/TP4/bs_server_II1.py)

## 2. Logs

🌞 **`bs_server_II2A.py`**

[Fichier]()

### B. Logs client

Les logs du client, c'est que dans un fichier. En effet, que ce soit une app console ou graphique, le client on veut lui montrer que ce qui est directement lié à SON utilisation de l'application. Et pas le reste.   
Donc on lui jette pas les logs et des vilaines erreurs au visage, ni 14000 messages informatifs.

Je vous laisse choisir l'emplacement du fichier de log de façon **pertinente**.

🌞 **`bs_client_II2B.py`**

- ce qui doit générer une ligne de log :
  - `INFO` connexion réussie à un serveur
    - `Connexion réussie à <IP>:<PORT>.`
  - `INFO` message envoyé par le client
    - `Message envoyé au serveur <IP_SERVER> : <MESSAGE>.`
  - `INFO` message reçu du serveur
    - `Réponse reçue du serveur <IP_SERVER> : <MESSAGE>.`
  - `ERROR` connexion au serveur échouée
    - pour le tester, il suffit de lancer le client alors que le serveur est éteint !
    - le message : `Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>.`
- en console
  - affiche juste `ERROR Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>.` en rouge quand ça fail (pas de timestamp là)
  - les messages de niveau INFO ne sont pas visibles dans la console du client
- dans un fichier
  - `<DOSSIER_DE_LOG>/bs_client.log`

### C. NOTE IMPORTANTE

**A partir de maintenant, vous savez gérer des logs à peu près proprement.**

Vous allez dév plusieurs machins en cours, vous devrez utiliser exactement la même méthode que précédemment pour générer les logs : timestamp, niveau de log, message, stocké dans un fichier précis etc.