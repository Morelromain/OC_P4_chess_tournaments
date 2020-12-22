"""Create """

from operator import attrgetter

from chess_tournaments.controller import validation as val
from chess_tournaments.model import model_r
from chess_tournaments.model import model_g
from chess_tournaments.view import start_r


class ContOR:
    """Controller First Round"""

    def other_r(self, list_p, list_g, list_r, count, nb_p):
        """start other round"""
        print("Round", count)
        nb = 0
        half_p = int(nb_p/2)
        for i in range(half_p):
            nb, nb_op = ContOR().position_p(list_p, nb)
            start_r.ViewStartRound().print_o_r_choice(list_p, nb_op, nb)
        for i in range(nb_p):
            list_p[i].cancel_taken()
        input("appuyer sur entrée pour lancer le round\n")
        name_r = count
        rounds = model_r.Round(name_r)
        print(rounds.name_r, "lancé à : ", rounds.time_start)
        input("appuyer sur entrée pour rentrer les scores du round\n")
        nb = 0
        for i in range(half_p):
            nb, nb_op = ContOR().position_p(list_p, nb)
            start_r.ViewStartRound().print_o_r(list_p, nb_op, nb)
            point1 = val.Valid().v_score(str(list_p[nb].ident))
            list_p[nb].update_score(point1)
            list_p[nb].append_meet(list_p[nb_op].ident)
            point2 = val.Valid().v_score(str(list_p[nb_op].ident))
            list_p[nb_op].update_score(point2)
            list_p[nb_op].append_meet(list_p[nb].ident)
            match_score = ([list_p[nb].name, point1],
                           [list_p[nb_op].name, point2])
            game = model_g.Game(match_score)
            list_g.append(game)
            rounds.add_match(match_score)
        list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
        for i in range(nb_p):
            list_p[i].cancel_taken()
        input("appuyer sur entrée pour finir le round\n")
        rounds.add_time()
        list_r.append(rounds)
        print(rounds)
        list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
        input("appuyer sur entrée pour revenir au menu le round")
        return count, list_p

    def position_p(self, list_p, nb):
        """
        search if player's was taken or meet, return position for each
        when they are not taken or meet,
        if round > (log2player), accept 2 players can meet 2 times.
        """
        try:
            while list_p[nb].taken is True:
                nb += 1
            nb_op = 0
            while (list_p[nb_op].ident in list_p[nb].meet or
                    list_p[nb_op].taken is True):
                nb_op += 1
            list_p[nb].taken = True
            list_p[nb_op].taken = True
        except IndexError:
            nb_op = nb_op - 1
        return nb, nb_op
