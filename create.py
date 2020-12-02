"""Create """

import model
import controller as ctlr

from operator import attrgetter

def create_tournament():
    """create tournament"""
    print ('création du tournois')
    valid = False
    while valid != True :  
        name_t = input('le nom du tournois : ')
        location = input('le lieu du tournois : ')
        date = input('la date du tournois : ')
        nb_round = input('le nombre de tours : ')
        c_time = input('controle temps : ') #blitz?
        description = input('la description du tournois : ')
        i_player = input('nombre de joueurs : ')
        i_round = input('nombre des tours : ') #instance de ronde
        trnmt = model.Tournament(name_t, location, date, nb_round, c_time, 
        description, i_player, i_round)
        print(trnmt)
        valid = ctlr.valid_summary("Valider? (O/N) : ")
    print ('le tournois {0} à été créé.'.format(trnmt.name_t))
    return trnmt

def create_player():
    """create 8 players"""
    print ('ajout des 8 joueurs')
    list_p = []
    for nb in range(8):
        (print ('joueur', nb+1))
        valid = False
        while valid != True :  
            ident = nb+1
            name = ctlr.valid_name('le nom du joueur : ')
            fname = input('le prénom du joueur : ')
            date = ctlr.valid_date('la date de naissance du joueur : ')
            sex = ctlr.valid_sex('le sexe du joueur (F/M) :')
            rank = ctlr.valid_int('le niveau du joueur (elo): ')
            player = model.Player(ident, name, fname, date, sex, rank)
            print (player)
            valid = ctlr.valid_summary("Valider? (O/N) : ")  
        list_p.append(player)
    #list_p = sorted(list_p, key=lambda list_p: list_p.rank, reverse=True) 
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)   
    return list_p

def create_round(list_p):
    """create round"""
    print("Remplir Round 1 :")
    list_game = []
    for nb in range(4):
        print(list_p[nb].name, list_p[nb].fname, "VS", 
        list_p[nb+4].name, list_p[nb+4].fname)

        #joueurnb
        point = input("Resultat "+list_p[nb].name+" "+list_p[nb].fname+" : ")
        point = float(point)
        list_p[nb].score += point

        meet = list_p[nb+4].ident
        list_p[nb].meet.append(meet)

        #joueurnb+4
        point = input("Resultat "+list_p[nb+4].name+" "+list_p[nb+4].fname+" : ")
        point = float(point)
        list_p[nb+4].score += point

        meet = list_p[nb].ident
        list_p[nb+4].meet.append(meet)

        #affichage etc
        match_name = list_p[nb].name + " VS " + list_p[nb+4].name
        scorej1 = str(list_p[nb].score)
        scorej2 = str(list_p[nb+4].score)
        match_score = scorej1 + " : " + scorej2
        game = model.Game(match_name, match_score)
        print(game)
        list_game.append(game)

    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    return list_game, list_p


