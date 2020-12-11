"""Main"""

from . import validation as val
from . import create_t
from . import create_p
from . import make_first_r as mfr
from . import make_other_r as mor
from ..view import vmenu
from ..view import results


class Menu:
    """Menu Controller"""

    menu = 0
    count = 0
    nb_r = 10
    while menu != 9:
        if count == 0:
            vmenu.ViewMenu().menustart()
        elif count == nb_r+1:
            vmenu.ViewMenu().menufinal()
        else:
            vmenu.ViewMenu().menuround()
        menu = int(val.Valid().v_int("Que voulez vous faire? (1 à 9) : "))
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
            if count == 0:
                trmnt, nb_p, nb_r = create_t.ContT().create_tournament()
                list_p = create_p.ContP().create_player(nb_p)
            if count == 1:
                list_p, list_g, list_r = mfr.ContFR().first_r(list_p, nb_p)
                trmnt.i_round = list_r[count-1].name_r
            if count > 1:
                if count == nb_r + 1:
                    print("finalisation...")
                else:
                    count, list_p = mor.ContOR().other_r(list_p, list_g,
                                                         list_r, count, nb_p)
                    trmnt.i_round = list_r[count-1].name_r
            count += 1
        if menu == 5:
            if count < 2:
                print("Pas de rounds existants dans le tournoi en cour")
            if count >= 2:
                results.ViewResult().results_r(list_r, nb_p)
        if menu == 6:
            if count == 0:
                print("Les joueurs du tournois ne sont pas créés")
            if count >= 1:
                results.ViewResult().results_p(list_p, nb_p)
        if menu == 7:
            if count < 2:
                print("Pas de match existants dans le tournoi en cour")
            if count >= 2:
                results.ViewResult().results_g(list_g)
        if menu == 8:
            if count < 0:
                print("Pas de tournois en cour")
            if count >= 1:
                results.ViewResult().results_t(trmnt)
        if menu == 9:
            exit()
        menu = 0
