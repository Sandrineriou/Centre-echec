"""Base de données Tinydb  -  Gestion des données."""

from tinydb import TinyDB, Query, where


from models.player import Player
from models.tournament import Tournament



db = TinyDB('db.json')
players_table = db.table('players')
tournaments_table = db.table('tournaments')
rounds_table = db.table('rounds')
matchs_table = db.table('matchs')

class DataPlayer:
    """Classe qui gère les opérations de la base en lien avec le joueur :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un joueur.
    """
    db = TinyDB('db.json')
    players_table = db.table('players')
    
    
    def all_players(self):
        print('\n'f"Il y a {len(players_table)} joueurs d'incrits dans la base."'\n')
        self.all = players_table.all()
        return self.all
    def sorted_all_players_alpha(self):
        self.alpha_sorted = sorted(self.all, key=lambda x: x['lastname'])
        for element in self.alpha_sorted:
            print(element['lastname'])


    def saving_data_player(self):
        """Sauvegarde les instances créées du joueur dans la base tinydb."""
        players_table.insert(self.player_serialized)
    
    def show_player(self):
        """Affiche les instances de tous les joueurs sauvegardés dans la base tinydb"""
        
        for row in players_table:
            print(row)

class DataTournament:
    """Classe qui gère les opérations de la base en lien avec le tournoi :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un tournoi.
    """    
   
    def saving_data_tournament(self):
        """Sauvegarde les instances créées dans la base tinydb."""
        tournaments_table.insert(self.tournament_serialized)



    def show_tournament():
        """Affiche les instances du tournoi sauvegardé"""
        tournaments_table.all()
        
    