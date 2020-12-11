"""Player's Model"""

from tinydb import TinyDB, Query


class Player:
    """Player's class"""

    def __init__(self, name, fname, date, sex, rank):
        """Player's construction"""
        self.ident = 0
        self.name = name
        self.fname = fname
        self.date = date
        self.sex = sex
        self.rank = rank
        self.score = 0.0
        self.taken = False
        self.meet = []

    def __repr__(self):
        return 'ID: {6} Nom: {0} Prénom: {1} Date: {2} Sex: {3} Elo: {4} Score: {5} \
Occupé : {7} Rencontre : {8}'.format(self.name, self.fname, self.date,
                                     self.sex, self.rank, self.score,
                                     self.ident, self.taken, self.meet)

    def update_score(self, point):
        """update_score"""
        self.score += point

    def cancel_taken(self):
        """update_score"""
        self.taken = False 

    def append_meet(self, app):
        """append_meet"""
        self.meet.append(app)

    def collect_id(self):
        """recup ident player"""
        db = TinyDB("db.json")
        p_tab = db.table("players")
        alldata_p = p_tab.all()
        nb_datap = len(alldata_p)
        self.ident = nb_datap + 1

    def search_p(self):
        """search player, if exist remplace data and take this ident
        if dont exist create in db"""
        db = TinyDB("db.json")
        p_tab = db.table("players")
        serialized_player = {"ident": self.ident, "name": self.name,
                             "fname": self.fname, "date": self.date,
                             "sex": self.sex, "rank": self.rank}
        fp = Query()
        exist = p_tab.search((fp.name == self.name) & (fp.fname == self.fname))
        if not(exist):
            print("test")
            p_tab.insert(serialized_player)
        else:
            print("test2")
            self.ident = exist[0].get("ident")
