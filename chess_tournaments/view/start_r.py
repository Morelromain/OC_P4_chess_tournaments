"""Start view"""

from random import choice


class ViewStartRound:
    """Controller Round"""

    def print_f_r_choice(self, list_p, half_p):
        """print first round and choice W or B"""
        for nb in range(half_p):
            print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
                list_p[nb+half_p].ident, list_p[nb+half_p].name,
                list_p[nb+half_p].fname)
            versus = [list_p[nb].ident, list_p[nb+half_p].ident]
            print("Joueur BLANC :", choice(versus))

    def print_f_r(self, list_p, half_p, nb):
        """print first round"""
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
                list_p[nb+half_p].ident, list_p[nb+half_p].name,
                list_p[nb+half_p].fname)

    def print_o_r_choice(self, list_p, nb_op, nb):
        """print other round and choice W or B"""
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
                list_p[nb_op].ident, list_p[nb_op].name, list_p[nb_op].fname)
        versus = [list_p[nb].ident, list_p[nb_op].ident]
        print("Joueur BLANC : ", choice(versus))

    def print_o_r(self, list_p, nb_op, nb):
        """print other round and choice W or B"""
        print(list_p[nb].ident, list_p[nb].name, list_p[nb].fname, "VS",
                list_p[nb_op].ident, list_p[nb_op].name, list_p[nb_op].fname)