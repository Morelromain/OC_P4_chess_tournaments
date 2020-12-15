"""Create """

from ..view import vdb
from ..model import model_t
from ..model import model_r
from ..model import model_g
from ..model import model_p

from tinydb import Query


class ManagData:
    """Controller Player"""

    def try_db_p(self, p_tab):
        """Sort"""
        sort_p = input("Tri par Nom (1) ou Elo (2) ? ")
        alldata_p = p_tab.all()
        # p_data = ()
        list_p = []
        for nb in range(len(alldata_p)):
            p_data = ()
            p_data = (alldata_p[nb].get("ident"), alldata_p[nb].get('name'),
                      alldata_p[nb].get('fname'), alldata_p[nb].get('date'),
                      alldata_p[nb].get('sex'), alldata_p[nb].get('rank'),
                      alldata_p[nb].get('score'), alldata_p[nb].get('meet'),
                      alldata_p[nb].get('taken'))
            list_p.append(p_data)
        if sort_p == "1":
            list_a = sorted(list_p, key=lambda colonnes: colonnes[1])
        else:
            list_a = sorted(list_p, key=lambda colonnes: colonnes[5],
                            reverse=True)
        vdb.ViewDB().display_all_p(list_a)

    def save_data(self, p_tab, t_tab, trmnt, list_p, list_r):
        """save_data"""
        trmnt.save_t(t_tab, list_p, list_r)
        for nb in range(len(list_p)):
            list_p[nb].save_p(p_tab)

    def load_data(self, t_tab, p_tab):
        """load_data"""
        list_r = []
        list_p = []
        del list_p[:]
        list_g = []
        alldata_t = t_tab.all()
        #  T
        name_t = alldata_t[-1].get("name_t")
        loc = alldata_t[-1].get("place")
        date = alldata_t[-1].get("date")
        nb_r = alldata_t[-1].get("nb_round")
        print(nb_r)
        c_time = alldata_t[-1].get("c_time")
        detail = alldata_t[-1].get("detail")
        i_player = alldata_t[-1].get("i_player")
        i_round = alldata_t[-1].get("i_round")
        inforound = alldata_t[-1].get("INFO")
        trmnt = model_t.Tournament(name_t, loc, date, nb_r, c_time, detail)
        trmnt.i_player = i_player
        trmnt.i_round = i_round
        trmnt.round = inforound
        #  R and G
        nb = 0
        for _ in range(trmnt.i_round):
            name_r = trmnt.round[nb]
            time_start = trmnt.round[nb+1]
            time_end = trmnt.round[nb+2]
            list_match = trmnt.round[nb+3]
            nb += 4
            rounds = model_r.Round(name_r)
            rounds.time_start = time_start
            rounds.time_end = time_end
            rounds.list_match = list_match
            print("en dessous")
            print(rounds)
            for nb_g in range(len(list_match)):
                game = model_g.Game(rounds.list_match[nb_g])
                list_g.append(game)
            list_r.append(rounds)
        #  P
        nb_p = (len(i_player))
        for nb_play in range(nb_p):
            search_p = Query()
            found_p = p_tab.search(search_p.ident == i_player[nb_play])
            ident = found_p[0].get("ident")
            name = found_p[0].get("name")
            fname = found_p[0].get("fname")
            date = found_p[0].get("date")
            sex = found_p[0].get("sex")
            rank = found_p[0].get("rank")
            score = found_p[0].get("score")
            taken = found_p[0].get("taken")
            meet = found_p[0].get("meet")
            player = model_p.Player(name, fname, date, sex, rank)
            player.ident = ident
            player.score = score
            player.taken = taken
            player.meet = meet
            list_p.append(player)
        # end
        count = i_round + 1
        print(list_p)
        return count, nb_r, p_tab, t_tab, trmnt, list_p, list_r, list_g, nb_p
