"""Model"""

import time


class Round:
    """Round's class"""

    def __init__(self, name_r):
        """Round's construction"""
        self.name_r = name_r
        self.time_start = time.strftime('%H:%M:%S')
        self.time_end = ""
        self.list_match = []

    def add_time(self):
        """Modif time_end, list_match"""
        self.time_end = time.strftime('%H:%M:%S')

    def add_match(self, list_g):
        """Modif time_end, list_match"""
        self.list_match.append(list_g)

    def __repr__(self):
        return '{0} Début: {1} Fin: {2}'.format(self.name_r, self.time_start,
                                                self.time_end)

    def position_p(list_p, nb):
        """
        search if player's was taken or meet, return position
        for each when they are not taken or meet.
        """
        while list_p[nb].taken is True:
            nb += 1
        nb_op = 0
        while (list_p[nb_op].ident in list_p[nb].meet or
                list_p[nb_op].taken is True):
            nb_op += 1
        list_p[nb].taken = True
        list_p[nb_op].taken = True
        return nb, nb_op

