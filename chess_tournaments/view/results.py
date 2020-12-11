"""Menu"""


def results_r(list_rounds, nb_p):
    """display round's tournament"""
    print("Affichage des rounds : ")
    for nb in range(len(list_rounds)):
        print("{0} Début: {1} Fin: {2}".format(list_rounds[nb].name_r,
            list_rounds[nb].time_start, list_rounds[nb].time_end))
        for nbr in range(int(nb_p/2)):
            print('{0}'.format(list_rounds[nb].list_match[nbr]))#FAUX
    input("appuyer sur entrée pour revenir au menu le round\n")


def results_p(list_p, nb_p):
    """display player's tournament"""
    print('Classement des joueurs du tournoi: ')
    for nb in range(nb_p):
        print('joueur', nb+1, ': {0}.'.format(list_p[nb]))
    input("appuyer sur entrée pour revenir au menu le round\n")


def results_g(list_game):
    """display matchs's tournament"""
    print("Affichage des matchs du tournois : ")
    for nb in range(len(list_game)):
        print("match", nb+1, ": ", list_game[nb])
    input("appuyer sur entrée pour revenir au menu le round\n")


def results_t(trmnt):
    """display tournament's info"""
    print('Affichage des infos du tournoi : ')
    print(trmnt)