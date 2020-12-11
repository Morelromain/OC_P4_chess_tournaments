"""Results view"""


class ViewResult:
    """Controller First Round"""

    def results_r(self, list_rounds, nb_p):
        """display round's tournament"""
        print("Affichage des rounds : ")
        for nb in range(len(list_rounds)):
            list_rounds[nb-1].display_match()
        input("appuyer sur entrée pour revenir au menu le round\n")

    def results_p(self, list_p, nb_p):
        """display player's tournament"""
        print('Classement des joueurs du tournoi: ')
        for nb in range(nb_p):
            print('joueur', nb+1, ': {0}.'.format(list_p[nb]))
        input("appuyer sur entrée pour revenir au menu le round\n")

    def results_g(self, list_game):
        """display matchs's tournament"""
        print("Affichage des matchs du tournois : ")
        for nb in range(len(list_game)):
            print("match", nb+1, ": ", list_game[nb])
        input("appuyer sur entrée pour revenir au menu le round\n")

    def results_t(self, trmnt):
        """display tournament's info"""
        print('Affichage des infos du tournoi : ')
        print(trmnt)