"""Menu view"""


class ViewMenu:
    """display menu"""

    def menustart(self):
        """display menu start"""
        print("\nTOURNOIS SUISSE\n\
1 : Voir précédants tournois\n\
2 : Voir liste joueur Base de donnée\n\
3 : Changer Elo d'un joueur\n\
4 : CREATION DU TOURNOI ET DES JOUEURS\n\
5 : Voir info round\n\
6 : Voir joueur tournoi en cour\n\
7 : voir match du tournoi\n\
8 : voir info tournoi\n\
9 : SAUVEGARDER et quitter\n\
10 : Quitter sans sauvegarger")

    def menuround(self, count):
        """display menu after create tournament"""
        print("\nTOURNOIS SUISSE\n\
1 : Voir précédants tournois\n\
2 : Voir liste joueur Base de donnée\n\
3 : Changer Elo d'un joueur\n\
4 : FAIRE LE ROUND N°", count, "\n\
5 : Voir info round\n\
6 : Voir joueur tournoi en cour\n\
7 : voir match du tournoi\n\
8 : voir info tournoi\n\
9 : SAUVEGARDER et quitter\n\
10 : Quitter sans sauvegarger")

    def menufinal(self):
        """display menu after last round"""
        print("\nTOURNOIS SUISSE\n\
1 : Voir précédants tournois\n\
2 : Voir liste joueur Base de donnée\n\
3 : Changer Elo d'un joueur\n\
4 : FINIR LE TOURNOI et quitter\n\
5 : Voir info round\n\
6 : Voir joueur tournoi en cour\n\
7 : voir match du tournoi\n\
8 : voir info tournoi\n\
9 : SAUVEGARDER et quitter\n\
10 : Quitter sans sauvegarger")

    def Sentence(self, m_choice):
        if m_choice == 0:
            print(" ")
        if m_choice == 1:
            print("Ce nombre n'existe pas dans le menu")
        if m_choice == 2:
            print("Voir précédants tournois")
        if m_choice == 3:
            print("Voir les joueurs dans la Base de donnée")
        if m_choice == 4:
            print("Changer Elo d'un joueur")
        if m_choice == 5:
            print("MATCH FINI, SAUVEGARDE ET QUITTER")
        if m_choice == 6:
            print("Pas de rounds existants dans le tournoi en cour")
        if m_choice == 7:
            print("Les joueurs du tournois ne sont pas créés")
        if m_choice == 8:
            print("Pas de match existants dans le tournoi en cour")
        if m_choice == 9:
            print("Pas de tournois en cour")
        if m_choice == 10:
            print("SAUVEGARDE ET QUITTER")
        if m_choice == 11:
            print("CHARGEMENT DU PRECEDENT TOURNOI")
        if m_choice == 12:
            print("Pas de tournoi à charger")            
