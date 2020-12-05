"""Create """

import time
from random import choice
from operator import attrgetter

import model
import controller as ctlr

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
    print ('Ajout des 8 joueurs')
    list_p = []
    for nb in range(8):
        (print ('joueur', nb+1))
        valid = False
        while valid != True :  
            ident = nb+1
            name = ctlr.valid_name('le nom du joueur : ')
            fname = "m"#input('le prénom du joueur : ')
            date = 1#ctlr.valid_date('la date de naissance du joueur : ')
            sex = "m"#ctlr.valid_sex('le sexe du joueur (F/M) : ')
            rank = ctlr.valid_int('le niveau du joueur (elo): ')
            player = model.Player(ident, name, fname, date, sex, rank)
            print (player)
            valid = ctlr.valid_summary("Valider? (O/N) : ")  
        list_p.append(player) 
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)   
    return list_p

def start_fround(list_p, list_game,list_rounds):
    """start first round"""
    print("Round n°1 :")
    #Affichage 4 matchs
    for nb in range(4):
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS", 
        list_p[nb+4].ident, list_p[nb+4].name, list_p[nb+4].fname)
        versus = [list_p[nb].ident, list_p[nb+4].ident]
        print("Joueur BLANC :", choice(versus))
    #Création round
    input("appuyer sur entrée pour lancer le round")
    name_r = "Round n°1"
    time_start = time.strftime('%H:%M:%S')
    rounds = model.Round(name_r, time_start)
    print(rounds,"\n")
    list_rounds.append(rounds)
    #Input des matchs
    for nb in range(4):
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS", 
        list_p[nb+4].ident, list_p[nb+4].name, list_p[nb+4].fname)
        #joueurnb
        point = ctlr.valid_float("Resultat "+list_p[nb].name+" "+list_p[nb].fname+" : ")
        point = float(point)
        list_p[nb].score += point
        meet = list_p[nb+4].ident
        list_p[nb].meet.append(meet)
        #joueurnb+4
        point = ctlr.valid_float("Resultat "+list_p[nb+4].name+" "+list_p[nb+4].fname+" : ")
        point = float(point)
        list_p[nb+4].score += point
        meet = list_p[nb].ident
        list_p[nb+4].meet.append(meet)
        #match
        match_name = list_p[nb].name+" "+list_p[nb].fname+" VS "\
        +list_p[nb+4].name+" "+list_p[nb+4].fname
        scorej1 = str(list_p[nb].score)
        scorej2 = str(list_p[nb+4].score)
        match_score = " score : "+scorej1+" : "+scorej2
        game = model.Game(match_name, match_score)
        rscore = (match_name+match_score)
        list_game.append(game)
        list_rounds[0].list_match.append(rscore)
    #finalisation du round
    time_end = time.strftime('%H:%M:%S')
    print(list_game)
    #list_rounds.list_match = list_game
    rounds.add_time(time_end)
    input("appuyer sur entrée pour revenir au menu le round")
    #try et récupère
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    print ("RECAPITULATIF")
    print (list_rounds)
    return list_game, list_p

def start_sround(list_p, list_game, list_rounds, counter):
    """start other round"""
    counter += 1
    print("Round", counter)
    #Affichage 4 matchs
    nb = 0
    for i in range(4):
        while list_p[nb].taken == True:
            nb += 1
        nb_op = 0
        while list_p[nb_op].ident in list_p[nb].meet or list_p[nb_op].taken == True:
            nb_op += 1 
        list_p[nb].taken = True
        list_p[nb_op].taken = True
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS", 
        list_p[nb_op].ident, list_p[nb_op].name, list_p[nb_op].fname)
        versus = [list_p[nb].ident, list_p[nb_op].ident]
        print("Joueur BLANC : ", choice(versus))
    for i in range(8):
        list_p[i].taken = False
        list_p[i].taken = False
    #Création round
    input("appuyer sur entrée pour lancer le round")
    name_r = "Round n°"+str(counter)
    time_start = time.strftime('%H:%M:%S')
    rounds = model.Round(name_r, time_start)
    print(rounds,"\n")
    list_rounds.append(rounds)
    #Input des matchs
    nb = 0
    for i in range(4):
        while list_p[nb].taken == True:
            nb += 1
        nb_op = 0
        while list_p[nb_op].ident in list_p[nb].meet or list_p[nb_op].taken == True:
            nb_op += 1 
        list_p[nb].taken = True
        list_p[nb_op].taken = True
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS", 
        list_p[nb_op].ident, list_p[nb_op].name, list_p[nb_op].fname)
        #joueurnb
        point = input("Resultat "+list_p[nb].name+" "+list_p[nb].fname+" : ")
        point1 = float(point)
        list_p[nb].score += point1
        meet = list_p[nb_op].ident
        list_p[nb].meet.append(meet)
        #joueurnb+1
        point = input("Resultat "+list_p[nb_op].name+" "+list_p[nb_op].fname+" : ")
        point2 = float(point)
        list_p[nb_op].score += point2
        meet = list_p[nb].ident
        list_p[nb_op].meet.append(meet)
        #match
        match_name = list_p[nb].name+" "+list_p[nb].fname+" VS "\
        +list_p[nb_op].name+" "+list_p[nb].fname
        match_score = " score : "+str(point1)+" : "+str(point2)
        game = model.Game(match_name, match_score)
        rscore = (match_name+match_score)
        list_game.append(game) #tout les match
        list_rounds[counter-1].list_match.append(rscore)
    list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
    #Reset taken
    for i in range(8):
        list_p[i].taken = False
        list_p[i].taken = False
    #finalisation du round
    time_end = time.strftime('%H:%M:%S')
    rounds.add_time(time_end)
    input("appuyer sur entrée pour revenir au menu le round")
    #try et récupère
    print ("RECAPITULATIF")
    print(list_rounds)
    return list_game, list_p, counter