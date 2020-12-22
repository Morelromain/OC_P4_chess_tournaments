"""Round's Model"""

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

    def add_match(self, game):
        """Modif time_end, list_match"""
        self.list_match.append(game)

    def __repr__(self):
        """display round"""

        return "{0} Début: {1} Fin: {2}".format(self.name_r, self.time_start,
                                                self.time_end)

    def display_match(self):
        """display match"""
        print("\n{0} Début: {1} Fin: {2}".format(self.name_r, self.time_start,
                                                 self.time_end,))
        for nb in range(len(self.list_match)):
            print("{0} {1} VS {2} {3}".format(self.list_match[nb][0][0],
                                              self.list_match[nb][0][1],
                                              self.list_match[nb][1][1],
                                              self.list_match[nb][1][0]))
