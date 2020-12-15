"""Main"""

from . import validation as val
from . import create_t
from . import create_p
from . import make_first_r as mfr
from . import make_other_r as mor
from ..view import vmenu
from ..view import results
from ..view import vdb
from . import manag_data

from tinydb import TinyDB


class Menu:
    """Menu Controller"""

    dbp = TinyDB("database_player.json")
    p_tab = dbp.table("players")
    dbt = TinyDB("database_tournament.json")
    t_tab = dbt.table("tournament")
    menu = 0
    count = 0
    nb_r = 10
    list_r = []
    while menu != 11:
        if count == 0:
            vmenu.ViewMenu().menustart()
        elif count == nb_r+1:
            vmenu.ViewMenu().menufinal()
        else:
            vmenu.ViewMenu().menuround()
        menu = val.Valid().v_int("Que voulez-vous faire? : ")
        print(" ")
        if menu > 10:
            print("Ce nombre n'existe pas dans le menu")
        if menu == 1:
            print("Voir précédants tournois")
            vdb.ViewDB().display_all_t(t_tab)
        if menu == 2:
            print("Voir les joueurs dans la Base de donnée")
            manag_data.ManagData().try_db_p(p_tab)
        if menu == 3:
            print("Changer Elo d'un joueur")
        if menu == 4:
            if count == 0:
                trmnt, nb_p, nb_r = create_t.ContT().create_tournament()
                list_p = create_p.ContP().create_player(nb_p, p_tab)
            if count == 1:
                list_p, list_g, list_r = mfr.ContFR().first_r(list_p, nb_p)
                trmnt.add_i_round(list_r[count-1].name_r)
                trmnt.add_round(list_r[count-1])
                print(list_r[count-1].list_match)
            if count > 1:
                print(count)
                print(nb_r)
                if count == nb_r + 1:
                    print("finalisation...")
                else:
                    count, list_p = mor.ContOR().other_r(list_p, list_g,
                                                         list_r, count, nb_p)
                    trmnt.add_i_round(list_r[count-1].name_r)
                    trmnt.add_round(list_r[count-1])
                    print(list_r[count-1].list_match)
            count += 1
        if menu == 5:
            if count < 2:
                print(count)
                print("Pas de rounds existants dans le tournoi en cour")
            if count >= 2:
                results.ViewResult().results_r(list_r, nb_p)
        if menu == 6:
            if count == 0:
                print("Les joueurs du tournois ne sont pas créés")
            if count >= 1:
                sort = input("tri par nom ou Elo? : ")
                if sort == "nom":
                    results.ViewResult().results_p_n(list_p, nb_p)
                else:
                    results.ViewResult().results_p_r(list_p, nb_p)
        if menu == 7:
            if count < 2:
                print("Pas de match existants dans le tournoi en cour")
            if count >= 2:
                results.ViewResult().results_g(list_g)
        if menu == 8:
            if count == 0:
                print("Pas de tournois en cour")
            if count >= 1:
                print("tournoi")
                results.ViewResult().results_t(trmnt)
        if menu == 9:
            if count == 0:
                print("Pas de tournois en cour")
            if count >= 1:
                print("SAUVEGARDE ET QUITTER")
                manag_data.ManagData().save_data(p_tab, t_tab, trmnt,
                                                 list_p, list_r)
        if menu == 10:
            print("CHARGEMENT DU PRECEDENT TOURNOI")
            (count, nb_r, p_tab, t_tab,
             trmnt, list_p, list_r, list_g,
             nb_p) = manag_data.ManagData().load_data(t_tab, p_tab)
            print(trmnt)
            menu = 0
        if menu == 11:
            exit()
        menu = 0
