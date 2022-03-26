"""Contrôleur des menus"""


from datetime import datetime
from logging import setLogRecordFactory
from pprint import pprint

from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
players_table = db.table('players')



from views.view import ViewMenu, ViewTournament, ViewPlayer
from models.tournament import Tournament
from models.player import Player
from models.database import DataPlayer, DataTournament
import models.database



MAX_PLAYERS = 8
NUMBER_ROUNDS = 4


class MainMenus:
    """Principal contrôleur des menus"""
    def __init__(self, view):
        self.view = view
        
    def openmainscreen(self):
        """Affiche le menu principal de l'accueil au lancement de l'application,
            
        Gère les choix de l'Utilisateur.
            
        """
        self.niveau1 = ViewMenu.homemenu().upper()
        while True:
            if self.niveau1 == "Q":
                """Propose de quitter l'application."""
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else: 
                    pass
            if self.niveau1 == '1' :
                """Affiche le menu pour gérer un tournoi, choix multiple."""
                return self.game()
            elif self.niveau1 == '2':
                """Affiche le menu pour gérer un joueur, choix multiple."""
                return self.gamer()
            elif self.niveau1 == '3':
                """Propose la mise à jour du classement joueur."""
                pass
            elif self.niveau1 == '4':
                """Affiche un menu pour l'édition de rapports."""
                return self.report()
            else:
                self.niveau1 = ViewMenu.homemenu().upper()

    def game(self):
        """Afffiche le menu du Jeu(tournoi) si choix 1 est sélectionné au niveau principal,
        et gère les choix de l'utilisateur sur les données d'un tournoi.
        """
        self.niveau2 = ViewMenu.gamemenu().upper()
        while True:
            if self.niveau2 == "Q":
                """Propose de quitter l'application."""
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else: 
                    pass
            if self.niveau2 == 'R':
                """Affiche le menu précédent."""
                return self.openmainscreen()
            elif self.niveau2 == '1':
                """Redémarre un tournoi suspendu."""
                pass
            elif self.niveau2 == '2':
                """Démarre la création d'un tournoi."""
                ViewTournament.tournament_view(self)
                ControlTournament.add_tournament(self)
                return ViewMenu.gamemenu()
            elif self.niveau2 == '3' :
                """Propose d'ajouter un commentaire au tournoi, à tout moment."""
                ControlTournament.add_comment(self) #à reprendre pas possible de l'intégrer dans la sauvegarde
                pass
                return ViewMenu.gamemenu()
            else:
               self.niveau2 = ViewMenu.gamemenu().upper()
            
    #pas sure de garder cette méthode : en attente    
    def gamer(self):
        """Affiche le menu du joueur si choix 2 est sélectionné au niveau principal
        et gère les choix de l'utilisateur sur les données d'un joueur.
        """
        
        self.niveau2 = ViewMenu.gamermenu().upper()
        while True:
            if self.niveau2 == "Q":
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else: 
                    pass
            if self.niveau2 == 'R':
                return self.openmainscreen()
            elif self.niveau2 == '1':
                """Interface de recherche d'un joueur."""
                pass
            elif self.niveau2 == '2':
                """Démarre la création d'un joueur, l'enregistrement dans la base des données saisies."""
                ViewPlayer.add_player_view(self)
                ControlPlayer.add_player(self)
                ControlPlayer.next_add_player(self)
                
            elif self.niveau2 == '3' :
                """Propose de supprimer un joueur de la base."""
                ViewPlayer.delete_player_view(self)
                ControlPlayer.delete_player_view_control(self)
                ControlPlayer.delete_player(self)
                pass
                
            elif self.niveau2 == '4' :
                """Propose de modifier les données d'un joueur (notamment en cas d'erreur de saisie)."""
                pass
            elif self.niveau2 == '5' :
                """Propose de mettre à jour le rang d'un joueur, à tout moment."""
                pass
            else:
                self.niveau2 = ViewMenu.gamermenu().upper()


    def update_ranking(self):
        
        pass

    def report(self):
        """Affiche le menu des rapports, si choix 4 est sélectionné au niveau principal
        et gère les choix de l'utilisateur sur le rapport sélectionné.
        """
        self.niveau2 = ViewMenu.report_view().upper()
        while True:
            if self.niveau2 == "Q":
                """Propose de quitter l'application."""
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else: 
                    pass
            if self.niveau2 == 'R':
                """Affiche le menu précédent."""
                return self.openmainscreen()
            elif self.niveau2 == '1':
                """Edite rapport acteurs par ordre alpha."""
                pass
            elif self.niveau2 == '2':
                """Edite rapport acteurs par classements."""
                pass
            elif self.niveau2 == '3' :
                """Edite rapport joueurs tournoi par ordre alpha."""
                ControlReport.show_all_players(self)
                pass
            elif self.niveau2 == '4' :
                """Edite rapport joueurs tournoi par classement."""
                pass
            elif self.niveau2 == '5' :
                """Edite rapport tous les tournois."""
                
                pass
            elif self.niveau2 == '6' :
                """Edite rapport tous les tours d'un tournoi."""
                pass
            elif self.niveau2 == '7' :
                """Edite rapport tous les matchs d'un tournoi.."""
                pass
            else:
                self.niveau2 = ViewMenu.report_view().upper()
        

    
class ControlTournament:
    """Controlleur qui entre en interaction avec le module Tournoi, et la class Vue spécifique au tournoi"""

    def __init__(self, tournament):
        self.tournament = tournament
    
    def add_tournament(self):
        """Regroupe toutes les méthodes permettant l'ajout des attributs d'un tournoi à sa création,

        sérialise les données et les enregistre dans tinydb.
            
        """  
        self. name_tournament_control()
        self.place_control() 
        self.controller_time_control()
        self.startdate_tournament_control()
        self.enddate = None
        self.n_rounds = NUMBER_ROUNDS
        self.players_list = []
        self.rounds_tournament = []
        self.list_dict_matchs = []
                
        Tournament.get_rounds(self)
        Tournament.serialize_tournament(self)
        Tournament.saving_data_tournament(self)
        Tournament.show_tournament(self)

        
    def name_tournament_control(self):
        """Contrôle la cohérence de saisie du nom du tournoi."""

        self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
        while True:
            if self.name_tournament == "":
                print("Veuillez saisir un nom de tournoi")
                self.name_tournament = ViewTournament.prompt_name_tournament_view(self)
            else :
                break
    
    def place_control(self):
        """Controle la cohérence de saisie du nom du lieu du tournoi."""
        self.place = ViewTournament.prompt_place_tournament_view(self).upper()
        while True:
            if self.place == "":
                print("Veuillez saisir un nom de ville")
                ViewTournament.prompt_place_tournament_view(self)
            else :
                break
    def controller_time_control(self):
        """Contrôle la cohérence de saisie du choix de gestion du temps du tournoi."""            
        self.controller_time = ViewTournament.prompt_controller_time_view(self)
        while True:
            if self.controller_time == '1':
                self.controller_time = 'Bullet'
                break
            elif self.controller_time == '2':
                self.controller_time = 'Blitz'
                break
            elif self.controller_time == '3':
                self.controller_time == 'Coup Rapide'
                break
            else :
                print("Veuillez saisir un choix entre 1, 2 ou 3.")
                self.controller_time = ViewTournament.prompt_controller_time_view(self)
    
    def startdate_tournament_control(self):
        """Contrôle la cohérence de saisie de la date de début du tournoi."""
        self.startdate = datetime.datetime.now().strftime("%d/%m/%Y")

    def add_comment(self):
        """Permet au gestionnaire de saisir un commentaire sur un tournoi"""
        Tournament.prompt_for_comment(self)
        Tournament.saving_data_tournament(self)
        pass
   

class ControlPlayer:
    """Controlleur qui entre en interaction avec le module player et la Vue PLayer"""

    def __init__(self, player):
        self.player = player
  
    def add_player(self):
        """Regroupe toutes les méthodes permettant l'ajout des attributs du joueur,

        sérialise les données et les enregistre dans tinydb.
            
        """
        ControlPlayer.lastname_control(self)
        ControlPlayer.firstname_control(self)
        ControlPlayer.birthdate_control(self)
        ControlPlayer.gender_control(self)
        ControlPlayer.ranking_control(self)
        self.score = 0
        Player.serialize_player(self)
        DataPlayer.saving_data_player(self)

    def lastname_control(self):
        """Contrôle la cohérence de saisie du nom de famille du joueur."""
        
        self.lastname = ViewPlayer.prompt_lastname_view(self).upper()
        while True:
            if self.lastname == "":
                print("Veuillez saisir un nom de famille !")
                self.lastname = ViewPlayer.prompt_lastname_view(self).upper()
            else:
                break
 
    def firstname_control(self):
        """Contrôle la cohérence de saisie du prénom du joueur."""

        self.firstname = ViewPlayer.prompt_firstname_view(self).upper()
        while True:
            if self.firstname == "":
                print("Veuillez saisir un prénom !")
                self.firstname = ViewPlayer.prompt_firstname_view(self).upper()
            else:
                break

    def birthdate_control(self):    
        """Contrôle la cohérence de saisir de la date de naissance."""

        self.birthdate = ViewPlayer.prompt_birthdate_view(self)
        while True:
            try:
                datetime.strptime(self.birthdate, '%d/%m/%Y')
                break
            except ValueError:
                print('veuillez saisir le bon format de date : jj/mm/aaaa')
                self.birthdate = ViewPlayer.prompt_birthdate_view(self)

    def gender_control(self):
        """Contrôle la cohérence de saisie du genre du joueur."""

        self.gender = ViewPlayer.prompt_gender_view(self).upper()
        while True:
            if self.gender not in ['H', 'F', 'T']:
                print("Veuillez saisir un genre dans la liste de choix")
                self.gender = ViewPlayer.prompt_gender_view(self).upper()
            else:
                break
    
    def ranking_control(self):            
        """Contrôle la cohérence de saisie du rang du joueur."""

        while True :
            try:
                self.ranking = int(ViewPlayer.prompt_ranking_view(self))
                break
            except ValueError:
                print("le retour attendu est un nombre")
      
    def next_add_player(self):
        """Choix entre continuer à créer un joueur sinon revenir au menu précédent."""
        output = ViewPlayer.prompt_next_add_player(self).upper()
        while True:
            if output == 'O':
                ControlPlayer.add_player(self)
                output = ViewPlayer.prompt_next_add_player(self).upper()
            else:             
                return MainMenus.gamer(self)
                
    def delete_player(self):
        """Regroupe toutes les méthodes permettant la suppression des données d'un joueur."""
    pass

    def delete_player_view_control(self):
        """Contrôle la cohérence de saisie du choix de l'utilisateur à supprimer un joueur dans la base."""
        output = ViewPlayer.delete_player_view(self).upper()
        while True:
            if output == 'O':
                ControlPlayer.delete_player(self)
                output = ViewPlayer.delete_player_view(self).upper()
            else:
                return MainMenus.gamer(self)

    def modify_player_view_control(self):
        """Contrôle la cohérence de saisie du choix de l'utilisateur
            à modifier les données du joueur dans la base.
            """
        ViewPlayer.modify_data_player_view(self).upper()
        pass

class ControlReport:
    """Controlleur qui entre en interaction avec le module database ???? et la vue ???"""
    
    

    def show_all_tournaments():
        """Récupére toutes les données en lien avec les tournois."""
       
        DataTournament.show_tournament()
            
    def show_all_players(self):
        while True :
            DataPlayer.all_players(self)
            DataPlayer.sorted_all_players_alpha(self)
            break
        return MainMenus.report(self)
