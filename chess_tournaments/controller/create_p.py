"""Create """

import math
from operator import attrgetter

from ..model import model_p
from . import validation as val


def create_player(nb_p):
    """create players"""
    print("Création des ", nb_p, "joueurs :")
    list_p = []
    for nb in range(nb_p):
        (print('joueur', nb+1))
        valid = False
        while valid is not True:
            name = val.valid_name('le nom du joueur : ')
            fname = "m"  # val.valid_str('le prénom du joueur : ')
            date = 1  # val.valid_date('la date de naissance du joueur : ')
            sex = "m"  # val.valid_sex('le sexe du joueur (F/M) : ')
            rank = val.valid_int('le niveau du joueur (elo): ')
            player = model_p.Player(name, fname, date, sex, rank)
            player.collect_id()
            player.search_p()
            player.append_meet(player.ident)
            print(player)
            valid = val.valid_summary("Valider? (O/N) : ")
        list_p.append(player)
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    return list_p
