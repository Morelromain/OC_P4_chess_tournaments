"""Create """

import time
import math
from random import choice
from operator import attrgetter

import model
import controller as ctlr


def create_tournament():
    """create tournament"""
    print('création du tournois')
    valid = False
    while valid is not True:
        name_t = ctlr.valid_str('le nom du tournois : ')
        location = ctlr.valid_str('le lieu du tournois : ')
        date = ctlr.valid_str('la date du tournois : ')
        c_time = ctlr.valid_str('controle temps (bullet/blitz/coup rapide) : ')
        description = ctlr.valid_str('la description du tournois : ')
        nb_p = int(input("combien de joueurs? (pair) : "))
        nb_round = math.ceil(math.log2(nb_p))
        i_player = ""  # instance de joueurs
        i_round = ""  # instance de round
        trnmt = model.Tournament(name_t, location, date, nb_round, c_time,
                                 description, i_player, i_round)
        print(trnmt)
        valid = ctlr.valid_summary("Valider? (O/N) : ")
    print('le tournois {0} à été créé.'.format(trnmt.name_t))
    return trnmt, nb_p, nb_round


def create_player(nb_p):
    """create players"""
    list_p = []
    for nb in range(nb_p):
        (print('joueur', nb+1))
        valid = False
        while valid is not True:
            ident = nb+1
            name = ctlr.valid_name('le nom du joueur : ')
            fname = "m"  # ctlr.valid_str('le prénom du joueur : ')
            date = 1  # ctlr.valid_date('la date de naissance du joueur : ')
            sex = "m"  # ctlr.valid_sex('le sexe du joueur (F/M) : ')
            rank = ctlr.valid_int('le niveau du joueur (elo): ')
            player = model.Player(ident, name, fname, date, sex, rank)
            print(player)
            valid = ctlr.valid_summary("Valider? (O/N) : ")
        list_p.append(player)
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    return list_p


def start_fround(list_p, nb_p):
    """start first round"""
    list_rounds = []
    list_game = []
    half_p = int(nb_p/2)
    print("Round 1 :")
    # Affichage 4 matchs
    for nb in range(half_p):
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
              list_p[nb+half_p].ident, list_p[nb+half_p].name,
              list_p[nb+half_p].fname)
        versus = [list_p[nb].ident, list_p[nb+half_p].ident]
        print("Joueur BLANC :", choice(versus))
    # Création round
    input("appuyer sur entrée pour lancer le round\n")
    name_r = "Round n°1"
    time_start = time.strftime('%H:%M:%S')
    rounds = model.Round(name_r, time_start)
    print(rounds)
    list_rounds.append(rounds)
    # Input des matchs
    input("appuyer sur entrée pour rentrer les scores du round\n")
    for nb in range(half_p):
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
              list_p[nb+half_p].ident, list_p[nb+half_p].name,
              list_p[nb+half_p].fname)
        # joueurnb
        point = ctlr.valid_float("Resultat " + list_p[nb].name + " "
                                 + list_p[nb].fname + " : ")
        point = float(point)
        list_p[nb].score += point
        meet = list_p[nb+half_p].ident
        list_p[nb].meet.append(meet)
        # joueurnb+4
        point = ctlr.valid_float("Resultat " + list_p[nb+half_p].name + " "
                                 + list_p[nb+half_p].fname + " : ")
        point = float(point)
        list_p[nb+half_p].score += point
        meet = list_p[nb].ident
        list_p[nb+half_p].meet.append(meet)
        # match
        match_name = (list_p[nb].name + " "+list_p[nb].fname + " VS "
                      + list_p[nb+half_p].name + " " + list_p[nb+half_p].fname)
        scorej1 = str(list_p[nb].score)
        scorej2 = str(list_p[nb+half_p].score)
        match_score = " score : "+scorej1+" : "+scorej2
        game = model.Game(match_name, match_score)
        rscore = (match_name+match_score)
        list_game.append(game)
        list_rounds[0].list_match.append(rscore)
    # finalisation du round
    input("appuyer sur entrée pour finir le round")
    time_end = time.strftime('%H:%M:%S')
    rounds.add_time(time_end)
    print(rounds)
    # try et récupère
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    input("appuyer sur entrée pour revenir au menu le round\n")
    return list_p, list_game, list_rounds


def start_sround(list_p, list_game, list_rounds, counter, nb_p):
    """start other round"""
    print("Round", counter)
    # Affichage 4 matchs
    nb = 0
    half_p = int(nb_p/2)
    for i in range(half_p):
        while list_p[nb].taken is True:
            nb += 1
        nb_op = 0
        while (list_p[nb_op].ident in list_p[nb].meet or
               list_p[nb_op].taken is True):
            nb_op += 1
        list_p[nb].taken = True
        list_p[nb_op].taken = True
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
              list_p[nb_op].ident, list_p[nb_op].name, list_p[nb_op].fname)
        versus = [list_p[nb].ident, list_p[nb_op].ident]
        print("Joueur BLANC : ", choice(versus))
    for i in range(nb_p):
        list_p[i].taken = False
        list_p[i].taken = False
    # Création round
    input("appuyer sur entrée pour lancer le round\n")
    name_r = "Round n°"+str(counter)
    time_start = time.strftime('%H:%M:%S')
    rounds = model.Round(name_r, time_start)
    print(rounds)
    list_rounds.append(rounds)
    # Input des matchs
    input("appuyer sur entrée pour rentrer les scores du round\n")
    nb = 0
    for i in range(half_p):
        while list_p[nb].taken is True:
            nb += 1
        nb_op = 0
        while (list_p[nb_op].ident in list_p[nb].meet or
               list_p[nb_op].taken is True):
            nb_op += 1
        list_p[nb].taken = True
        list_p[nb_op].taken = True
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
              list_p[nb_op].ident, list_p[nb_op].name, list_p[nb_op].fname)
        # joueurnb
        point = input("Resultat "+list_p[nb].name+" "+list_p[nb].fname+" : ")
        point1 = float(point)
        list_p[nb].score += point1
        meet = list_p[nb_op].ident
        list_p[nb].meet.append(meet)
        # joueurnb+1
        point = input("Resultat "+list_p[nb_op].name+" "
                      + list_p[nb_op].fname+" : ")
        point2 = float(point)
        list_p[nb_op].score += point2
        meet = list_p[nb].ident
        list_p[nb_op].meet.append(meet)
        # match
        match_name = (list_p[nb].name+" "+list_p[nb].fname+" VS "
                      + list_p[nb_op].name+" "+list_p[nb].fname)
        match_score = " score : "+str(point1)+" : "+str(point2)
        game = model.Game(match_name, match_score)
        rscore = (match_name+match_score)
        list_game.append(game)  # tout les match
        list_rounds[counter-1].list_match.append(rscore)
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    # Reset taken
    for i in range(nb_p):
        list_p[i].taken = False
        list_p[i].taken = False
    # finalisation du round
    input("appuyer sur entrée pour finir le round")
    time_end = time.strftime('%H:%M:%S')
    rounds.add_time(time_end)
    print(rounds)
    # try et récupère
    input("appuyer sur entrée pour revenir au menu le round\n")
    return counter
