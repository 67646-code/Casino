import datetime
import os

#  à ameliorer, erreur au premier lancement, crée le fichier mais crash et si pas de fichier le crée mais pas de suite donc crash
def init_solde():
    if os.path.exists('./scores.txt') :
        with open("scores.txt", "r") as f:
            return f.read()
    else:
        with open("scores.txt", 'w') as f:
            f.write("100")
            return int(100)

def maj_solde(solde):
    #mise à jour du solde à faire en début de partie et en fin
    now = datetime.datetime.now()
    with open("scores.txt", 'w') as f:
        f.write(f"{solde}")