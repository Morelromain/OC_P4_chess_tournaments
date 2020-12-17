"""Main"""

from . import validation as val
from . import create_t
from . import create_p
from . import make_first_r as mfr
from . import make_other_r as mor
from ..view import vmenu
from ..view import results
from . import manag_data

from tinydb import TinyDB


class Menu:
    """Menu Controller"""

    dbp = TinyDB("database_player.json")
    dbt = TinyDB("database_tournament.json")
    p_tab = dbp.table("players")
    t_tab = dbt.table("tournament")
    menu, count, nb_r, list_r = 0, 0, 10, []
    load = val.Valid().v_load("Nouveau tournoi(1)/Charger tournoi(2) : ")
    if load == "2":
        vmenu.ViewMenu().Sentence(11)
        (count, nb_r, p_tab, t_tab,
         trmnt, list_p, list_r, list_g,
         nb_p) = manag_data.ManagData().load_data(t_tab, p_tab)
    while menu != 10:
        if count == 0:
            vmenu.ViewMenu().menustart()
        elif count == nb_r+1:
            vmenu.ViewMenu().menufinal()
        else:
            vmenu.ViewMenu().menuround(count)
        menu = val.Valid().v_int("Que voulez-vous faire? : ")
        vmenu.ViewMenu().Sentence(0)
        if menu > 10:
            vmenu.ViewMenu().Sentence(1)
        if menu == 1:
            vmenu.ViewMenu().Sentence(2)
            results.ViewDB().display_all_t(t_tab)
        if menu == 2:
            vmenu.ViewMenu().Sentence(3)
            manag_data.ManagData().try_db_p(p_tab)
        if menu == 3:
            vmenu.ViewMenu().Sentence(4)
            manag_data.ManagData().update_rank(p_tab)
        if menu == 4:
            if count == 0:
                trmnt, nb_p, nb_r = create_t.ContT().create_tournament()
                list_p = create_p.ContP().create_player(nb_p, p_tab)
            if count == 1:
                list_p, list_g, list_r = mfr.ContFR().first_r(list_p, nb_p)
                trmnt.add_i_round(list_r[count-1].name_r)
                trmnt.add_round(list_r[count-1])
            if count > 1:
                if count == nb_r + 1:
                    vmenu.ViewMenu().Sentence(5)
                    manag_data.ManagData().save_data(p_tab, t_tab, trmnt,
                                                     list_p, list_r)
                    exit()
                else:
                    count, list_p = mor.ContOR().other_r(list_p, list_g,
                                                         list_r, count, nb_p)
                    trmnt.add_i_round(list_r[count-1].name_r)
                    trmnt.add_round(list_r[count-1])
                    print(list_r[count-1].list_match)
            count += 1
        if menu == 5:
            if count < 2:
                vmenu.ViewMenu().Sentence(6)
            if count >= 2:
                results.ViewResult().results_r(list_r, nb_p)
        if menu == 6:
            if count == 0:
                vmenu.ViewMenu().Sentence(7)
            if count >= 1:
                sort = input("Tri par Nom (1) ou Elo (2) ? ")
                results.ViewResult().results_p(list_p, nb_p, sort)
        if menu == 7:
            if count < 2:
                vmenu.ViewMenu().Sentence(8)
            if count >= 2:
                results.ViewResult().results_g(list_g)
        if menu == 8:
            if count == 0:
                vmenu.ViewMenu().Sentence(9)
            if count >= 1:
                results.ViewResult().results_t(trmnt)
        if menu == 9:
            if count == 0:
                vmenu.ViewMenu().Sentence(9)
            if count >= 1:
                vmenu.ViewMenu().Sentence(10)
                manag_data.ManagData().save_data(p_tab, t_tab, trmnt,
                                                 list_p, list_r)
                exit()
        if menu == 10:
            exit()
        menu = 0
