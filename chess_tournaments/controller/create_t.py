"""Create """

import math
from operator import attrgetter

from ..model import model_t
from . import validation as val


def create_tournament():
    """create tournament"""
    print("Création du tournois :")
    valid = False
    while valid is not True:
        name_t = val.valid_str('le nom du tournois : ')
        loc = val.valid_str('le lieu du tournois : ')
        date = val.valid_str('la date du tournois : ')
        c_time = val.valid_str('controle temps (bullet/blitz/coup rapide) : ')
        detail = val.valid_str('la description du tournois : ')
        nb_p = int(input("combien de joueurs? (4/8/16/32) : "))
        nb_r = math.ceil(math.log2(nb_p))
        trnmt = model_t.Tournament(loc, name_t, date, nb_r, c_time, detail)
        print(trnmt)#ligne a enlever?
        valid = val.valid_summary("Valider? (O/N) : ")
    print('le tournois {0} à été créé.\n'.format(trnmt.name_t))
    return trnmt, nb_p, nb_r
