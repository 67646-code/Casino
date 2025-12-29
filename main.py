from casino import init_solde

choixmenu = 0

solde = init_solde()
while choixmenu < 1 or choixmenu > 4:
    print("Menu principal")
    print(solde)
    print("1 - Black Jack")
    print("2 - Roulette")
    print("3 - Machine à sous")
    print("4 - Quitter")
    choixmenu = int(input("Entrez votre choix "))
