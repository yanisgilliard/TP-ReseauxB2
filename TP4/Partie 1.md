# I. Simple bs program

Première partie pour mettre en place un environnement fonctionnel et deux programmes simples qui discutent à travers le réseau.

- [I. Simple bs program](#i-simple-bs-program)
  - [1. First steps](#1-first-steps)
  - [2. User friendly](#2-user-friendly)
  - [3. You say client I hear control](#3-you-say-client-i-hear-control)

## 1. First steps

🌞 **`bs_server_I1.py`**

https://github.com/yanisgilliard/TP-ReseauxB2/blob/1e0004a29163da155e2d455433871ab94d564cf4/TP4/bs_server_l1.py

🌞 **`bs_client_I1.py`**

https://github.com/yanisgilliard/TP-ReseauxB2/blob/e98f1174341163c099e9afef0f17577f4c968f78/TP4/bs_client_l1.py


🌞 **Commandes...**
````
[yanis@bs-server]$ python3 bs_server_I1.py 
Meooooo !
````
````
[yanis@bs-client]$ python3 bs_client_I1.py
Meooooo !
````
````
[yanis@bs-server ~]$ ss -tupnl | grep 13337
tcp   LISTEN 0      1          10.1.1.10:13337      0.0.0.0:*    users:(("python3",pid=2083,fd=3))
````

## 2. User friendly

🌞 **`bs_client_I2.py`**

https://github.com/yanisgilliard/TP-ReseauxB2/blob/636217785c9e7e5dd119fba9cd9922549d076892/TP4/bs_client_I2.py

🌞 **`bs_server_I2.py`**

https://github.com/yanisgilliard/TP-ReseauxB2/blob/636217785c9e7e5dd119fba9cd9922549d076892/TP4/bs_server_I2.py

## 3. You say client I hear control

On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.

🌞 **`bs_client_I3.py`**

- vérifier que...
  - le client saisit bien une string
    - utilisez la méthode native `type()` pour vérifier que c'est une string
  - que la string saisie par le client contient obligatoirement soit "waf" soit "meo"
    - utilisez [**une expression régulière**](https://www.programiz.com/python-programming/regex) (signalez-le moi s'il serait bon de faire un cours sur cette notion)
- sinon lever une erreur avec `raise`
  - choisissez avec pertinence l'erreur à lever dans les deux cas (s'il saisit autre chose qu'une string, ou si ça contient aucun des deux mots)
  - y'a une liste des exceptions natives (choisissez-en une donc) tout en bas du [cours sur la gestion d'erreur](../../../../cours/dev/error_handling/README.md)

> On poussera le contrôle plus loin plus tard.