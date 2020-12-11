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
        self.i_round = "round n°0"

    def __repr__(self):
        return 'Tournois: {0} Lieu: {1} Date: {2}\nNombre de tours: {3} \
Controle de temps: {4}\nDescription: {5} \
Round en cour: {6}'.format(self.name_t, self.loc, self.date, self.nb_round,
                           self.c_time, self.detail, self.i_round)
