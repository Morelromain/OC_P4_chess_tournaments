"""Create """

import time
from operator import attrgetter

from . import validation as val
from ..model import model_r
from ..model import model_g
from ..view import start_r


def first_r(list_p, nb_p):
    """start first round"""
    list_r = []
    list_g = []
    half_p = int(nb_p/2)
    print("Round 1 :")
    # Affichage 4 matchs
    start_r.print_f_r_choice(list_p, half_p)
    # Création round
    input("appuyer sur entrée pour démarrer le round\n")
    name_r = "Round n°1"
    rounds = model_r.Round(name_r)
    print(rounds.name_r, "lancé à : ", rounds.time_start)
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    # Input des matchs
    input("appuyer sur entrée pour rentrer les scores du round\n")
    for nb in range(half_p):
        start_r.print_f_r(list_p, half_p, nb)
        # j1 rencontre j2
        point1 = val.valid_float("Resultat " + str(list_p[nb].ident) + " : ")
        list_p[nb].update_score(point1)
        list_p[nb].append_meet(list_p[nb+half_p].ident)
        # j2 rencontre j1
        point2 = val.valid_float("Resultat " + str(list_p[nb+half_p].ident) + " : ")
        list_p[nb+half_p].update_score(point2)
        list_p[nb+half_p].append_meet(list_p[nb].ident)
        # Création match du match
        match_score = ([list_p[nb].name, point1], 
                       [list_p[nb+half_p].name, point2])
        game = model_g.Game(match_score)
        list_g.append(game)
    # finalisation du round
    input("appuyer sur entrée pour finir le round\n")
    rounds.add_match(list_g)
    rounds.add_time()
    list_r.append(rounds)
    print(rounds)
    # tri et récupère
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    input("appuyer sur entrée pour revenir au menu le round")
    return list_p, list_g, list_r
