"""Menu"""

import time

import controller as ctlr
import create

menu = 0


while menu != 11:
    print(
    "CREER                       VOIR\n\
    1 : Création Tournoi        6 : Voir Tournoi\n\
    2 : Création Joueur         7 : Voir Joueur\n\
    3 : Remplir Round 1         8 : Voir Round 1\n\
    4 : Remplir Round 2         9 : Voir Round 2\n\
    5 : Remplir Round 3         10: Voir Round 3"
    )
    menu = int(ctlr.valid_int("Que voulez vous faire? (1 à 11) : "))
    if menu > 10:
        print("Ce nombre n'existe pas dans le menu")
    if menu == 1:
        trmnt = create.create_tournament()
        print(trmnt.name_t, "créé")
    if menu == 2:
        list_p = create.create_player()
    if menu == 3:
        #4 MATCH OK, NOM ROUND A CREER
        
        list_game,list_p = create.create_round(list_p)
    if menu == 4:
        print("Remplir Round 2")
    if menu == 5:
        print("Remplir Round 3")
    if menu == 6:
        print(trmnt)
    if menu == 7:
        print ('Classement des 8 joueurs : ')
        for nb in range(8):
            print ('joueur', nb+1, ': {0}.'.format(list_p[nb]))
    if menu == 8:
        print ('Affichage Round 1 : ')
        for nb in range(4):
            print ('match', nb+1, ': {0}.'.format(list_game[nb]))
    if menu == 9:
        print("Voir Round 2")
    if menu == 10:
        print("Voir Round 3")
    time.sleep(2)
    menu = 0