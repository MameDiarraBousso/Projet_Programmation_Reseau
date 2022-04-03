1-Le module mysql.connector a été importé pour pouvoir interagir avec la base de données. 
La fonction "VerifierMail" permet de verifier la présence de l'adresse mail fournie.
La fonction "Inscription" renvoie true si l'insertion s'est bien déroulée.
Enfin, nous avons la fonction "Connexion" 

2- La fonction "OpenServer" permet au serveur d'initialiser une session en attente d'un client mais aussi de pouvoir interagir avec ce dernier.Lancement du script OpenServer se fait en tapant : ./server.py

3-Une fonction "openClientTunnel" est une fonction qui offre au client la possibilité de fournir ses informations d'identification, de se connecter ou de quitter la session. Lancement de ce script se fait en tapant ./client.py

4- Analyseur: 
Nous avons : 
-une fonction "ethernet_frame" qui déballe les packets de frame ethernet. 
-une fonction "ipv4_packet" qui recupère les packets ipv4. 
-une fonction "get_mac_addr" qui retourne proprement une adresse MAC. 
-une fonction "ipv4" qui retourne le format propre de ipv4. 
-une fonction "tcp_segment" qui déballe les segments tcp. 
-une fonction "udp_segment" qui déballe les segments udp. 
-une fonction "format_multi_line" qui formate les données multi lignes.

5-La fonction "EnvoiMail" permet d'envoyer un mail 
