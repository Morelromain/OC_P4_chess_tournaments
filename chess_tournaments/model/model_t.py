"""Tournament's Model"""


class Tournament:
    """Tournament's class"""

    def __init__(self, name_t, loc, date, nb_round,
                 c_time, detail):
        """Tournament's construction"""
        self.name_t = name_t
        self.loc = loc
        self.date = date
        self.nb_round = nb_round
        self.c_time = c_time
        self.detail = detail
        self.i_player = []
        self.i_round = "pas de round en cour"
        self.round = []

    def __repr__(self):
        return 'Tournois: {0} Lieu: {1} Date: {2}\nNombre de tours: {3} \
Controle de temps: {4}\nDescription: {5} \
Dernier round joué: {6}'.format(self.name_t, self.loc,
                                self.date, self.nb_round,
                                self.c_time, self.detail, self.i_round)

    def add_i_round(self, name):
        """Modif time_end, list_match"""
        self.i_round = name

    def add_round(self, rnd):
        """Modif time_end, list_match"""
        self.round.append(rnd)

    def save_t(self, t_tab, list_p, list_r):
        """Save tournament"""
        info_r = []
        self.i_player = []
        for nb in range(len(list_p)):
            self.i_player.append(list_p[nb].ident)
        for nb in range(len(list_r)):
            info_r.append(list_r[nb].name_r)
            info_r.append(list_r[nb].time_start)
            info_r.append(list_r[nb].time_end)
            info_r.append(list_r[nb].list_match)
        serialized_tournament = {"name_t": self.name_t, "place": self.loc,
                                 "date": self.date, "nb_round": self.nb_round,
                                 "c_time": self.c_time, "detail": self.detail,
                                 "i_player": self.i_player,
                                 "i_round": self.i_round, "INFO": info_r}
        t_tab.insert(serialized_tournament)
