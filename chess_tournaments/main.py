"""Main"""

from .controller import validation as val
from .controller import create
from .view import vmenu

def menus():
    menu = 0
    counter = 0
    nb_round = 10
    while menu != 9:
        if counter == 0:
            vmenu.menustart()
        elif counter == nb_round+1:
            vmenu.menufinal()
        else:
            vmenu.menuround()
        menu = int(val.valid_int("Que voulez vous faire? (1 à 9) : "))
        print(" ")
        if menu > 9:
            print("Ce nombre n'existe pas dans le menu")
        if menu == 1:
            print("Voir précédants tournois")
        if menu == 2: 
            print("Voir classement joueur")
        if menu == 3:
            print("Changer Elo d'un joueur")
        if menu == 4:
            if counter == 0:
                print("Création tournoi/joueur")
                trmnt, nb_p, nb_round = create.create_tournament()
                print("veuillez rentrer les", nb_p, "joueurs")
                list_p = create.create_player(nb_p)
            if counter == 1:
                list_p, list_game, list_rounds = create.start_fround(list_p, nb_p)
                trmnt.i_round = list_rounds[counter-1].name_r
            if counter > 1:
                if counter == nb_round+1:
                    print("finalisation...")
                else:
                    counter = create.start_sround(list_p, list_game, list_rounds,
                                                counter, nb_p)
                    trmnt.i_round = list_rounds[counter-1].name_r
            counter += 1
        if menu == 5:
            if counter < 2:
                print("Pas de rounds existants")
            if counter >= 2:
                print('Affichage des rounds : ')
                for nb in range(len(list_rounds)):
                    print('{0} Début: {1} Fin: {2}'.format(list_rounds[nb].name_r,
                        list_rounds[nb].time_start, list_rounds[nb].time_end))
                    for nbr in range(int(nb_p/2)):
                        print('{0}'.format(list_rounds[nb].list_match[nbr]))
                input("appuyer sur entrée pour revenir au menu le round\n")
        if menu == 6:
            if counter == 0:
                print("Les joueurs du tournois ne sont pas créés")
            if counter >= 1:
                print('Classement des joueurs du tournoi: ')
                for nb in range(nb_p):
                    print('joueur', nb+1, ': {0}.'.format(list_p[nb]))
                input("appuyer sur entrée pour revenir au menu le round\n")
        if menu == 7:
            if counter < 2:
                print("Pas de match existants")
            if counter >= 2:
                print('Affichage des matchs du tournois : ')
                for nb in range(len(list_game)):
                    print('match', nb+1, ': {0}.'.format(list_game[nb]))
                input("appuyer sur entrée pour revenir au menu le round\n")
        if menu == 8:
            print('Affichage des infos du tournoi : ')
            print(trmnt)
        menu = 0
