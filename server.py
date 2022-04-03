import socket
import time
import json
import database

def Inscription(client:socket, buffer:int):
    liste = list()
    req = "Entrer votre nom svp : " 
    client.send(req.encode("utf-8"))
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Entrer votre prenom :"
    client.send(req.encode("utf-8"))
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Entrer votre adresse mail :"
    client.send(req.encode("utf-8"))
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    requete1 = "motdepasse1"
    requete2 = "motdepasse2"

    while requete1 != requete2:
        req = " Entrez votre mot de passe :"
        client.send(req.encode("utf-8"))
        requete1 = client.recv(buffer)

        req = "Entrez à nouveau le mot de passe :"
        client.send(req.encode("utf-8"))
        requete2 = client.recv(buffer)

        if requete1 != requete2:
            req = "Désolée mais les mots de passe ne sont pas identiques"
            client.send(req.encode("utf-8"))
        else:
            req = "Les mots de passe sont identiques"
            client.send(req.encode("utf-8")) 

    liste.append(requete1.decode("utf-8"))
    if database.Inscription(liste) == True:
        req = "Votre inscription est validée"
        client.send(req.encode("utf-8")) 
    else:
        req = "Erreur"
        client.send(req.encode("utf-8")) 



def Connexion(client:socket,buffer:int):
    liste = list()
    req = "Entrer votre adresse mail :"
    client.send(req.encode("utf-8")) 
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Entrer votre mot de passe :"
    client.send(req.encode("utf-8"))
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Connexion(liste) == True:
        req = "Connexion reussie"
        client.send(req.encode("utf-8"))
    else:
        req = "Echec"
        client.send(req.encode("utf-8"))





def openServer(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((host,port))
    serveur.listen(5)

    client, infosClient = serveur.accept()
    print("Client connecté. Adresse " + infosClient[0])  

    while True:    
        
        reponse = "Choisissez l'option 1 pour s'inscrire , l'option 2 pour se connecter ou l'option 3 pour quitter "
        client.send(reponse.encode("utf-8"))
        time.sleep(2)

        requete = client.recv(buffer)
        requete_decode = requete.decode("utf-8")

        if requete_decode == "1":
            Inscription(client,buffer)

        elif requete_decode == "2":
            Connexion(client,buffer)

        elif requete_decode == "3":         
            req = "Au revoir!"
            client.send(req.encode("utf-8")) 
            client.close()
            break

    serveur.close()
           
    


if __name__ == "__main__":
    
    openServer('192.168.10.1', 50000)
