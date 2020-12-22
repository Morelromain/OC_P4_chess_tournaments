"""Validation input """

import datetime

from unicodedata import normalize, combining


class Valid:
    """Valid Input"""

    def v_int(self, ask):
        """Valid question if int and not empty"""
        while True:
            try:
                nb = int(input(ask))
                break
            except ValueError:
                print("Chiffre invalide")
        return nb

    def v_player(self, ask):
        """Valid question if int and not empty"""
        while True:
            try:
                nb = int(input(ask))
                if nb % 2 == 0:
                    break
                else:
                    print("Chiffre invalide (impair)")
            except ValueError:
                print("Chiffre invalide")
        return nb

    def v_score(self, ident):
        """Valid question if float and not empty"""
        while True:
            try:
                score = float(input("Resultat  " + ident + ": "))
                break
            except ValueError:
                print("Score invalide")
        return score

    def v_str(self, ask):
        """Valid question if not empty only"""
        while True:
            info = (input(ask))
            if info != '':
                break
            else:
                print('Saisi invalide (vide)')
        return info

    def v_name(self, ask):
        """Up and normalize reply"""
        while True:
            info = (input(ask))
            if info != '':
                info = info.upper()
                infnorm = normalize('NFKD', info)
                break
            else:
                print('Saisi invalide (vide)')
        return "".join([c for c in infnorm if not combining(c)])

    def v_sex(self, ask):
        """Valid sex question if F/M only, up reply"""
        while True:
            sex = (input(ask))
            sex = sex.upper()
            if sex == 'F' or sex == 'M':
                break
            else:
                print('Saisi invalide, veuillez rentrer F ou M (Femme/Homme)')
        return sex

    def v_date(self, ask):
        """Valid date question if DD/MM/YYYY only, date's format reply"""
        while True:
            try:
                date_text = (input(ask))
                date = datetime.datetime.strptime(date_text, '%d/%m/%Y')
                date = date.date()
                break
            except ValueError:
                print('Veuillez rentrer ce format : DD/MM/YYYY')
        return date

    def v_summary(self, ask):
        """Valid summary question if O/N only, up reply"""
        while True:
            valid = input(ask)
            valid = valid.upper()
            if valid == 'O':
                valid = True
                return valid
            elif valid == 'N':
                valid = False
                print('Vous avez n\'avez pas validé')
                break
            else:
                print('Repondez par la touche O ou N (Oui/Non)')

    def v_duree(self, ask):
        """Valid duree question"""
        valid = input(ask)
        valid = valid.upper()
        if valid == 'O':
            valid = True
            date_f = Valid().v_date("la date de fin du tournois : ")
            return date_f
        elif valid == 'N':
            valid = False
            date_f = " "
            return date_f
        else:
            print('Repondez par la touche O ou N (Oui/Non)')

    def v_load(self, ask):
        """Valid load question if 1/2 only, up reply"""
        while True:
            load = (input(ask))
            if load == "1" or load == "2":
                break
            else:
                print("Saisi invalide, veuillez choisir 1 ou 2")
        return load
