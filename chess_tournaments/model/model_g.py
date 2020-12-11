"""Model"""


class Game:
    """Game's class"""

    def __init__(self, match_score):
        """Game's construction"""
        self.match_score = match_score

    def __repr__(self):
        """display Game"""
        return "{0} {1} VS {2} {3}".format(self.match_score[0][0],
                                           self.match_score[0][1],
                                           self.match_score[1][1],
                                           self.match_score[1][0])



 #   def __str__(self):
 #       """display game with print"""
 #       return repr(self)
