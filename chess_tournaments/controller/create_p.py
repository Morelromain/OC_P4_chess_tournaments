"""Create """

from operator import attrgetter

from chess_tournaments.model import model_p
from chess_tournaments.controller import validation as val
from chess_tournaments.controller import manag_data as md


class ContP:
    """Controller Player"""

    def create_player(self, nb_p, p_tab):
        """create players"""
        print("Création des ", nb_p, "joueurs :")
        list_p = []
        for nb in range(nb_p):
            (print("joueur", nb+1))
            valid = False
            while valid is not True:
                name = val.Valid().v_name("le nom du joueur : ")
                fname = val.Valid().v_str("le prénom du joueur : ")
                date = val.Valid().v_date("la date de naissance du joueur : ")
                sex = val.Valid().v_sex("le sexe du joueur (F/M) : ")
                rank = val.Valid().v_int("le elo du joueur : ")
                player = model_p.Player(name, fname, str(date), sex, rank)
                player.collect_id(p_tab)
                serial_p, search_n, search_f = player.serial_p(p_tab)
                md.ManagData().search_p(serial_p, search_n, search_f, p_tab, player)
                player.append_meet(player.ident)
                print("numero d'identification : ", player.ident)
                valid = val.Valid().v_summary("Valider? (O/N) : ")
            list_p.append(player)
        list_p = sorted(list_p, key=attrgetter("score", "rank"), reverse=True)
        return list_p
