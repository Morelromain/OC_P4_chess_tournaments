# OC_P4_chess_tournaments
Programme de création de tournoi d'echec (système suisse)

## Pré-requis

Version Python : 3.8.3
Python packages : tinydb==4.3.0

-Activer le programme:
```bash
python -m chess_tournaments
```

## Utilisation

### Options Start

1 : Nouveau tournoi  
*Accède au menu*  
2 : Charger tournoi  
*Charge le dernier tournoi enregistré puis accède au menu*  

### Options Menu

1 : Voir précédants tournois  
*Affiche les tournois enregistrés dans le fichier "database_tournament"*  
2 : Voir liste joueur Base de donnée  
*Affiche les joueurs enregistrés dans le fichier "database_player"*  
*Tri par Nom ou Elo (niveau)*  
3 : Changer Elo d'un joueur  
*Modifie le Elo (niveau) d'un joueur dans la base de donnée*  
4 : CREATION DU TOURNOIS ET DES JOUEURS  
*Lance la création du tournoi et de ces joueurs associés*  
4 : FAIRE LE ROUND N°X  
*Lance la création d'un round et de ces matchs associés*  
4 : FINIR LE TOURNOI ET QUITTER  
*Enregistre les résultats du tournoi/joueurs dans les fichiers "database"*  
*Ferme le programme*  
5 : Voir info round  
*Voir les informations des rounds du tournoi*  
6 : Voir joueur tournois en cour  
*Voir les joueurs du tournoi*  
*Tri par Nom ou Elo (niveau)*  
7 : voir match du tournoi  
*Voir l'integralité des matchs du tournoi*  
8 : voir info tournoi  
*Voir les informations du tournoi*  
9 : SAUVEGARDER et quitter  
*Enregistre les résultats du tournoi/joueurs dans les fichiers "database"*  
*Ferme le programme*  
10 : Quitter sans sauvegarger  
*Ferme le programme*  