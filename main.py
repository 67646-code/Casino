
from casino import init_solde, maj_solde, menu_principal, menu_jeu

solde = init_solde()
while True:
    choix = menu_principal()
    if choix == 4:
        estsur = input("Etes-vous sûr de vouloir partir? vous pouvez encore vous refaire :) (oui/non): ")
        if estsur == "oui":
            maj_solde(solde)
            exit()
    else:
        solde=menu_jeu(choix,solde)
#         fonctionne mais boucle sur l'affichage du menu
