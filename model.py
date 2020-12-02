"""Appli's model"""

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
        self.meet = []

    def __repr__(self):
        return 'ID: {6} Nom: {0} Prénom: {1} Date: {2} Sex: {3} Elo: {4} Score: {5} Occupé : {7} Rencontre : {8}'.format(
        self.name, self.fname, self.date, self.sex, self.rank, self.score, self.ident, self.taken, self.meet) #info non necessaire

class Tournament:
    """Tournament's class"""

    def __init__(self, name_t, location, date, nb_round, 
    c_time, description, i_player, i_round):
        """Tournament's construction"""
        self.name_t = name_t
        self.location = location
        self.date = date
        self.nb_round = nb_round
        self.c_time = c_time
        self.description = description
        self.i_player = i_player
        self.i_round = i_round

    def __repr__(self):
        return 'Tournois: {0} Lieu: {1} Date: {2}\nNombre de tours: {3} \
Controle de temps: {4}\nDescription: {5}'.format(self.name_t, self.location, 
        self.date, self.nb_round, self.c_time, self.description)

class Round:
    """Round's class"""

    def __init__(self, name, date_start, date_end):
        """Round's construction"""
        self.name = name
        self.date_start = date_start
        self.date_end = date_end

class Game:
    """Game's class"""

    def __init__(self, match_name, match_score):
        """Game's construction"""
        self.match_name = match_name
        self.match_score = match_score

    def __repr__(self):
        return 'Match {0} Score {1}'.format(self.match_name, self.match_score)