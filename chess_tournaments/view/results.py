"""Results view"""


class ViewResult:
    """Controller First Round"""

    def results_r(self, list_rounds, nb_p):
        """display round's tournament"""
        print("Affichage des rounds : ")
        for nb in range(len(list_rounds)):
            list_rounds[nb].display_match()
        input("appuyer sur entrée pour revenir au menu")

    def results_p_n(self, list_p, nb_p):
        """display player's tournament"""
        list_a = sorted(list_p, key=lambda list_p: list_p.name)
        print('Classement des joueurs du tournoi: ')
        for nb in range(nb_p):
            print('joueur', nb+1, ': {0}.'.format(list_a[nb]))
        input("appuyer sur entrée pour revenir au menu")

    def results_p_r(self, list_p, nb_p):
        """display player's tournament"""
        list_a = sorted(list_p, key=lambda list_p: list_p.rank, reverse=True)
        print('Classement des joueurs du tournoi: ')
        for nb in range(nb_p):
            print('joueur', nb+1, ': {0}.'.format(list_a[nb]))
        input("appuyer sur entrée pour revenir au menu")

    def results_g(self, list_game):
        """display matchs's tournament"""
        print("Affichage des matchs du tournois : ")
        for nb in range(len(list_game)):
            print("match", nb+1, ": ", list_game[nb])
        input("appuyer sur entrée pour revenir au menu")

    def results_t(self, trmnt):  # A MODIF
        """display tournament's info"""
        print('Affichage des infos du tournoi : ')
        print(trmnt)
        input("appuyer sur entrée pour revenir au menu")
