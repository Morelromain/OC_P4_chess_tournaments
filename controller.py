"""Controller input """

import datetime
from unicodedata import normalize, combining

def valid_int(ask):
    """Valid question if number only"""
    valid = False
    while valid != True:
        nb = (input(ask))
        verif = nb.isdigit()
        if verif:
            valid = True
            return nb
        else:
            print('Saisi invalide, veuillez rentrer un chiffre')

def valid_name(ask):
    """Up and normalize reply"""
    valid = False
    while valid != True:
        info = (input(ask))
        info = info.upper()
        infnorm = normalize('NFKD', info)
        valid = True
        return "".join([c for c in infnorm if not combining(c)])

def valid_sex(ask):
    """Valid sex question if F/M only, up reply"""
    valid = False
    while valid != True:
        sex = (input(ask))
        sex = sex.upper()
        if sex == 'F' or sex == 'M':
            valid = True
            return sex
        else:
            print('Saisi invalide, veuillez rentrer F ou M (Femme/Homme)')

def valid_date(ask):
    """Valid date question if DD/MM/YYYY only, date's format reply"""
    valid = False
    while valid != True:    
        try:
            date_text = (input(ask))
            date = datetime.datetime.strptime(date_text, '%d/%m/%Y')
            valid = True
            date = date.date()
            return date
        except ValueError:
            print('Saisi invalide, veuillez rentrer ce format : DD/MM/YYYY')

def valid_summary(ask):
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
            print ('Repondez par la touche O ou N (Oui/Non)')