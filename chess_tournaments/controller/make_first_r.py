"""Create """

from operator import attrgetter

from . import validation as val
from ..model import model_r
from ..model import model_g
from ..view import start_r


class ContFR:
    """Controller First Round"""

    def first_r(self, list_p, nb_p):
        """start first round"""
        list_r = []
        list_g = []
        half_p = int(nb_p/2)
        print("Round 1 :")
        start_r.ViewStartRound().print_f_r_choice(list_p, half_p)
        input("appuyer sur entrée pour démarrer le round\n")
        name_r = 1
        rounds = model_r.Round(name_r)
        print(rounds.name_r, "lancé à : ", rounds.time_start)
        list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
        input("appuyer sur entrée pour rentrer les scores du round\n")
        for nb in range(half_p):
            start_r.ViewStartRound().print_f_r(list_p, half_p, nb)
            point1 = val.Valid().v_score(str(list_p[nb].ident))
            list_p[nb].update_score(point1)
            list_p[nb].append_meet(list_p[nb+half_p].ident)
            point2 = val.Valid().v_score(str(list_p[nb+half_p].ident))
            list_p[nb+half_p].update_score(point2)
            list_p[nb+half_p].append_meet(list_p[nb].ident)
            match_score = ([list_p[nb].name, point1],
                           [list_p[nb+half_p].name, point2])
            game = model_g.Game(match_score)
            list_g.append(game)
            rounds.add_match(match_score)
        input("appuyer sur entrée pour finir le round\n")
        rounds.add_time()
        list_r.append(rounds)
        print(rounds)
        list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
        input("appuyer sur entrée pour revenir au menu le round")
        return list_p, list_g, list_r
