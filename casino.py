# import datetime
import random
import os
import curses.ascii

# TODO : crée fonctions pour le choix du mode difficulté, voir le fichier score.txt
# TODO : les variables resteront dans ce fichier donc il faut changer les paramètres des fonctions et le nom variables dedans

#hello word

starting_score=100
file_name='score.txt'

# def starting_score()
def file_exist():
    return os.path.exists(file_name)

def file_content_isdecimal(file_content):
    if file_content.isdecimal():
        return True
    else:
        return False

def isvalid(file_content):
    if int(file_content) > 0 :
        return True
    else:
        return False

def score_file_reading():
    with open(file_name,"r") as f:
        return f.read()

def get_valid_score():
    if file_exist() :
        file_content = score_file_reading()
        if file_content_isdecimal(file_content):
            if isvalid(file_content):
                return int(file_content)
    else:
        # toute autres situation possible = écrasemement et réecriture du fichier
        create_score_file()
        return int(score_file_reading())

def create_score_file():
    with open(file_name,"w") as f :
        f.write(str(starting_score))
    return None

# def score_file_load():
#     if isusable_file(file_name):
#         with open(file_name,"r") as f:
#             return int(f.read())
#     else:
#         create_score_file()
#     return None

-----------------------------------------------------------
def test_mise(mise,solde):
    while mise < -1 or mise > solde:
        print("Mise invalide")
        mise =int(input("Entrez une mise valide, entrez -1 pour revenir au menu: "))
    return mise

def maj_solde(solde):
    #mise à jour du solde à faire en début de partie et en fin
    with open(file_name, 'w') as f:
        f.write(f"{solde}")

def menu_principal():
    # TODO : solution contre les entrées users non désirée (ValueError quand on entre une chaine)
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
    if choixmenu == 1:
        solde = black_jack(solde)

    elif choixmenu == 2:
        print("Bienvenue à la Roulette")
        input("Appuie sur Entrée pour revenir au menu...")

    elif choixmenu == 3:
        solde = machine_sous(solde)

    return solde



def machine_sous(solde):
    print("Bienvenue aux machines à sous! ")
    print(solde)
    mise=int(input("Entrez votre mise (-1 pour retourner au menu): "))
    test = test_mise(mise,solde)
    while test != -1:
        symboles = ["🍒", "🍋", "🔔", "⭐", "💎"]
        tirage = [random.choice(symboles) for _ in range(3)]
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

def black_jack(solde):
    print("Bienvenue aux Balck Jack! ")
    print(solde)
    mise = int(input("Entrez votre mise (-1 pour retourner au menu): "))
    test = test_mise(mise, solde)
    while test != -1:
        mainuser=[random.randint(1,11) for _ in range(2)]
        print(f"{mainuser}")
        choix=input("Hit or Stay?: ")
        while True and choix == "Hit" or choix == "hit":
            mainuser.append(random.randint(1,11))
            print(f"{mainuser}")
            if sum(mainuser) > 21 :
                print("Dommage")
                solde -= test
                break
            elif sum(mainuser) == 21:
                print("21 !")
                solde += test
            choix = input("Hit or Stay?: ")
        print(solde)
        mise = int(input("Entrez votre mise (-1 pour retourner au menu): "))
        test = test_mise(mise, solde)
    return solde
