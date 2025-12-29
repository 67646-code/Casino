# import datetime
import random
import os

#  à ameliorer, erreur au premier lancement, crée le fichier mais crash et si pas de fichier le crée mais pas de suite donc crash
def init_solde():
    if os.path.exists('./scores.txt') :
        with open("scores.txt", "r") as f:
            return int(f.read())
    else:
        with open("scores.txt", 'w') as f:
            f.write("100")
            return int(100)

def maj_solde(solde):
    #mise à jour du solde à faire en début de partie et en fin
    with open("scores.txt", 'w') as f:
        f.write(f"{solde}")

def menu_principal():
    choixmenu = 0
    while choixmenu < 1 or choixmenu > 4:
        print("Menu principal")
        print(init_solde())
        print("1 - Black Jack")
        print("2 - Roulette")
        print("3 - Machine à sous")
        print("4 - Quitter")
        choixmenu = int(input("Entrez votre choix "))
    return choixmenu

def menu_jeu(choixmenu,solde):
    solde = init_solde()
    if choixmenu == 1:
        print("Bienvenue à la table de Black Jack")
        input("Appuie sur Entrée pour revenir au menu...")

    elif choixmenu == 2:
        print("Bienvenue à la Roulette")
        input("Appuie sur Entrée pour revenir au menu...")

    elif choixmenu == 3:
        solde = machine_sous(solde)

    return solde

def test_mise(mise,solde):
    while mise < -1 or mise > solde:
        print("Mise invalide")
        mise =int(input("Entrez une mise valide, entrez -1 pour revenir au menu: "))
    return mise

def machine_sous(solde):
    print("Bienvenue aux machines à sous! ")
    print(solde)
    mise=int(input("Entrez votre mise (-1 pour retourner au menu): "))
    test = test_mise(mise,solde)
    while test != -1:
        symboles = ["🍒", "🍋", "🔔", "⭐", "💎"]
        tirage = [random.choice(symboles) for i in range(3)]
        print(f"{tirage[0]},{tirage[1]},{tirage[2]}")
        if tirage[0] == tirage[1] == tirage[2] :
            solde += 2*test
        else:
            print("Dommage")
            solde -= test
        print(solde)
        mise=int(input("Entrez votre mise (-1 pour retourner au menu): "))
        test = test_mise(mise,solde)
    maj_solde(solde)
    return solde
