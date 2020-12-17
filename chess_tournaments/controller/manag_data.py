"""Create """

from ..view import results
from ..model import model_t
from ..model import model_r
from ..model import model_g
from ..model import model_p

from tinydb import Query


class ManagData:
    """Controller Player"""

    def update_rank(self, p_tab):
        """update rank"""
        sp = Query()
        s_ident = int(input("ident du joueur : "))
        new_rank = int(input("changer le elo du joueur pour : "))
        p_tab.update({"rank": new_rank}, sp.ident == s_ident)

    def try_db_p(self, p_tab):
        """Sort"""
        sort_p = input("Tri par Nom (1) ou Elo (2) ? ")
        alldata_p = p_tab.all()
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
        results.ViewDB().display_all_p(list_a)

    def search_p(self, serial_p, search_n, search_f, p_tab, player):
        """Search player in data base Player and add or update player"""
        fp = Query()
        exist = p_tab.search((fp.name == search_n) & (fp.fname == search_f))
        if not(exist):
            print("Joueur Créé")
            p_tab.insert(serial_p)
        else:
            ident = exist[0].get("ident")
            player.update_ident(ident)
            print("Joueur existant dans la DataBase")

    def save_data(self, p_tab, t_tab, trmnt, list_p, list_r):
        """save_data"""
        info_r = []
        trmnt.i_player = []
        for nb in range(len(list_p)):
            trmnt.i_player.append(list_p[nb].ident)
        for nb in range(len(list_r)):
            info_r.append(list_r[nb].name_r)
            info_r.append(list_r[nb].time_start)
            info_r.append(list_r[nb].time_end)
            info_r.append(list_r[nb].list_match)
        serial_trnmt = {"name_t": trmnt.name_t, "place": trmnt.loc,
                        "date": trmnt.date, "nb_round": trmnt.nb_round,
                        "c_time": trmnt.c_time, "detail": trmnt.detail,
                        "i_player": trmnt.i_player,
                        "i_round": trmnt.i_round, "INFO": info_r}
        t_tab.insert(serial_trnmt)
        for nb in range(len(list_p)):
            fp = Query()
            p_tab.update({"score": list_p[nb].score},
                         fp.ident == list_p[nb].ident)
            p_tab.update({"meet": list_p[nb].meet},
                         fp.ident == list_p[nb].ident)

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
        c_time = alldata_t[-1].get("c_time")
        detail = alldata_t[-1].get("detail")
        i_player = alldata_t[-1].get("i_player")
        i_round = alldata_t[-1].get("i_round")
        inforound = alldata_t[-1].get("INFO")
        trmnt = model_t.Tournament(name_t, loc, date, nb_r, c_time, detail)
        trmnt.i_player = i_player
        trmnt.i_round = i_round
        trmnt.round = inforound
        t_tab.remove(doc_ids=[(len(t_tab))])
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
        return count, nb_r, p_tab, t_tab, trmnt, list_p, list_r, list_g, nb_p
