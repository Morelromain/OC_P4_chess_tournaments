"""Main"""

import time

import controller as ctlr
import create
import cmenu


print(time.strftime('%H:%M:%S'))


menu = 0
while menu != 5:
    cmenu.menustart()
    menu = int(ctlr.valid_int("Que voulez vous faire? (1 à 5) : "))
    if menu > 5:
        print("Ce nombre n'existe pas dans le menu")
    if menu == 1:
        print("Voir précédants tournois")
    if menu == 2:
        print("Voir classement joueur")
    if menu == 3:
        print("Changer Elo d'un joueur")
    if menu == 4:
        print("Création tournoi/joueur")
        trmnt = create.create_tournament()
        list_p = create.create_player()
        firstround = False
        list_game = []
        list_match = []
        list_rounds = []
        counter = 1
        while menu != 9:
            cmenu.menuround()
            menu = int(ctlr.valid_int("Que voulez vous faire? (1 à 8) : "))
            if menu > 9:
                print("Ce nombre n'existe pas dans le menu")
            if menu == 1:
                print("Voir précédants tournois")
            if menu == 2:
                print("Voir classement joueur")
            if menu == 3:
                print("Changer Elo d'un joueur")
            if menu == 4:
                if firstround == False:
                    list_game, list_p = create.start_fround(list_p, list_game, list_rounds)
                    firstround = True
                else:
                    list_game,list_p,counter = create.start_sround(list_p, list_game, list_rounds, counter)
            if menu == 5:
                print ('Affichage des rounds : ')
                for nb in range(len(list_rounds)):
                    print ('{0} Début: {1} Fin: {2}'.format(list_rounds[nb].name_r, list_rounds[nb].time_start, list_rounds[nb].time_end))
                    for nbr in range(4):
                        print ('{0}'.format(list_rounds[nb].list_match[nbr]))
            if menu == 6:
                print ('Classement des 8 joueurs : ')
                for nb in range(8):
                    print ('joueur', nb+1, ': {0}.'.format(list_p[nb]))
            if menu == 7:
                print ('Affichage des matchs du tournois : ')
                for nb in range(len(list_game)):
                    print ('match', nb+1, ': {0}.'.format(list_game[nb]))
            if menu == 8:
                print ('Affichage des infos du tournoi : ')
                print(trmnt)

        menu = 5
