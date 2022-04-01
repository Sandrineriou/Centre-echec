"""Base de données Tinydb  -  Gestion des données."""

from pprint import pprint
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
    
    
    def saving_data_player(self):
        """Sauvegarde les instances créées du joueur dans la base tinydb."""
        players_table.insert(self.player_serialized)
    
    def search_player(self):
        """Affiche le joueur de la base portant le nom et prénom saisie"""
        return players_table.search((where('lastname') == self.lastname)and(where('firstname') == self.firstname))
    
    def search_lastname_player(self):
        """Affiche les joueurs de la base portant le nom saisie."""
        return players_table.search(where('lastname') == self.lastname)

    
    def search_all_players(self):
        """Affiche tous les joueurs de la base."""
        print('\n'f"Il y a {len(players_table)} joueurs incrits dans la base."'\n')
        self.all = players_table.all()
        return self.all
        

    def sorted_all_players_alpha(self):
        """Affiche tous les joueurs de la base par ordre alphabétique(nom)"""
        self.alpha_sorted = sorted(self.all, key=lambda x: x['lastname'])
        for element in self.alpha_sorted:
            print("Joueur: ID "f'{element.doc_id}', element['lastname'], element['firstname'],"Né le :" , element['birthdate'],
                element['gender'], "classement: ", element['ranking']
            )

    def delete_player(self):
        """Supprime 1 joueur recherché"""
        User = Query()
        return players_table.remove((User.lastname == self.lastname) and (User.firstname == self.firstname))

    def truncate_players_table(self):
        """Efface toutes les données de la table 'Player(mise à zéro)."""
        return players_table.truncate()
    
    def update_ranking_player(self):# modifier pour mettre l'ID en recherche plutot que le nom ou sinon rajouter le prénom
        User = Query()
        return players_table.update({'ranking':self.new_ranking}, User.lastname == self.lastname)

    

    

class DataTournament:
    """Classe qui gère les opérations de la base en lien avec le tournoi :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un tournoi.
    """    
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')

    def saving_data_tournament(self):
        """Sauvegarde les instances créées dans la base tinydb."""
        tournaments_table.insert(self.tournament_serialized)
 
    def search_all_tournaments(self):
        """Affiche tous les tournois inscrits dans la base."""
        print('\n'f"Il y a {len(tournaments_table)} tournois incrits dans la base."'\n')
        self.all = tournaments_table.all()
        return self.all
    
    def search_name_tournament(self):
        """Affiche les informations en lien avec le nom du tournoi."""
        return tournaments_table.search(where("Nom_tournoi") == self.name_tournament)

    def update_players_list_tournament(self):
        User = Query()
        print(tournaments_table.update({'Liste_joueurs': self.players_list}, User.Nom_tournoi == self.name_tournament))
    
    
    
    
    def truncate_tournaments_table(self):
        """Efface toutes les données de la table 'Tournaments'(mise à zéro)."""
        return tournaments_table.truncate()