"""Create """

from ..model import model_t
from . import validation as val


class ContT:
    """Controller Tournament"""

    def create_tournament(self):
        """create tournament"""
        print("Création du tournois :")
        valid = False
        while valid is not True:
            name_t = val.Valid().v_str("le nom du tournois : ")
            loc = "b"  # val.Valid().v_str("le lieu du tournois : ")
            date_d = val.Valid().v_date("la date de debut du tournoi : ")
            date_f = val.Valid().v_duree("tournoi sur plusieurs jours?(O/N): ")
            date = (str(date_d) + str(date_f))
            c_time = "b"  # val.Valid().v_str("bullet/blitz/coup rapide : ")
            detail = "b"  # val.Valid().v_str("la description du tournois : ")
            nb_p = val.Valid().v_player("nombre de joueur (pair): ")
            nb_r = val.Valid().v_int("nombre de round (defaut:4): ")
            trnmt = model_t.Tournament(name_t, loc, date, nb_r, c_time, detail)
            print(trnmt)
            valid = val.Valid().v_summary("Valider? (O/N) : ")
        print("le tournois {0} à été créé.\n".format(trnmt.name_t))
        return trnmt, nb_p, nb_r
