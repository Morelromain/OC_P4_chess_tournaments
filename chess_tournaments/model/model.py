"""Model"""


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


class Player:
    """Player's class"""

    def __init__(self, ident, name, fname, date, sex, rank):
        """Player's construction"""
        self.ident = ident
        self.name = name
        self.fname = fname
        self.date = date
        self.sex = sex
        self.rank = rank
        self.score = 0.0
        self.taken = False
        self.meet = [ident]

    def __repr__(self):
        return 'ID: {6} Nom: {0} Prénom: {1} Date: {2} Sex: {3} Elo: {4} Score: {5} \
Occupé : {7} Rencontre : {8}'.format(self.name, self.fname, self.date,
                                     self.sex, self.rank, self.score,
                                     self.ident, self.taken, self.meet)


class Round:
    """Round's class"""

    def __init__(self, name_r, time_start):
        """Round's construction"""
        self.name_r = name_r
        self.time_start = time_start
        self.time_end = ""
        self.list_match = []

    def add_time(self, time_end):
        """Modif time_end, list_match"""
        self.time_end = time_end

    def __repr__(self):
        return '{0} Début: {1} Fin: {2}'.format(self.name_r, self.time_start,
                                                self.time_end)


class Game:
    """Game's class"""

    def __init__(self, match_name, match_score):
        """Game's construction"""
        self.match_name = match_name
        self.match_score = match_score

    def __repr__(self):
        return '{0} {1}'.format(self.match_name, self.match_score)
