"""Contrôleur des menus"""


import datetime
from pprint import pprint

from tinydb import TinyDB, Query, where


from views.view import ViewMenu, ViewTournament, ViewPlayer
from models.tournament import Tournament
from models.player import Player


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
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else: 
                    pass
            if self.niveau1 == '1' :
                return self.game()
            elif self.niveau1 == '2':
                ViewPlayer.player_view(self)
                ControlPlayer.add_player(self)
            elif self.niveau1 == '3':
                pass
            elif self.niveau1 == '4':
                pass
            else:
                self.niveau1 = ViewMenu.homemenu().upper()

    def game(self):
        """Afffiche le menu du Jeu et gère les choix de l'utilisateur."""

        self.niveau2 = ViewMenu.gamemenu().upper()
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
                pass
            elif self.niveau2 == '2':
                ViewTournament.tournament_view(self)
                ControlTournament.add_tournament(self)
                return ViewMenu.gamemenu()
            elif self.niveau2 == '3' :
                ControlTournament.add_comment(self) #à reprendre pas possible de l'intégrer dans la sauvegarde
                return ViewMenu.gamemenu()
            else:
               self.niveau2 = ViewMenu.gamemenu().upper()
            
    #pas sure de garder cette méthode : en attente    
    def add_player(self):
    
        ViewMenu.player_view(self)
        entry = input("Voulez_vous ajouter des joueurs ? (O/N) : ").upper()
        while entry not in ["O", "N"]:
            input("Voulez_vous ajouter des joueurs ? (O/N) : ").upper()
        if entry == 'O':
            return add_player(self)
        elif entry == 'N':
            return self.openmainscreen()
        
        pass
  

    def update_ranking(self):
        self.niveau2 = ViewMenu.updaterankingview()
        pass

    def report(self):
        self.niveau2 = ViewMenu.reporteditingview()
        pass

    
class ControlTournament:

    def __init__(self, tournament):
        self.tournament = tournament
    
    def add_tournament(self):
        """ # à revoir :je teste la fonction """
        
        self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
        while self.name_tournament is None:
            ViewTournament.prompt_name_tournament_view(self)
            if self.name_tournament == "":
                print("Veuillez saisir un nom de tournoi")
                ViewTournament.prompt_name_tournament_view(self)
                break
            else :
                break
   
        self.place = ViewTournament.prompt_place_tournament_view(self).upper()
        while self.place is None:
            ViewTournament.prompt_place_tournament_view(self)
            if self.place == "":
                print("Veuillez saisir un nom de ville")
                ViewTournament.prompt_place_tournament_view(self)
                break
            else :
                break
  
        self.controller_time = ViewTournament.prompt_controller_time_view(self)
        while self.controller_time not in ['1', '2', '3']:
                    self.controller_time = ViewTournament.prompt_controller_time_view(self)
                        
        if self.controller_time == '1':
            self.controller_time = 'Bullet'
        elif self.controller_time == '2':
            self.controller_time = 'Blitz'
        elif self.controller_time == '3':
            self.controller_time == 'Coup Rapide'
    
        self.startdate = datetime.datetime.now().strftime("%d/%m/%Y")
        self.enddate = None
        self.n_rounds = NUMBER_ROUNDS
        self.players_list = []
        self.rounds_tournament = []
        self.list_dict_matchs = []
                
        Tournament.get_rounds(self)
        Tournament.serialize_tournament(self)
        Tournament.saving_data_tournament(self)
        Tournament.show_tournament(self)
                
    def add_comment(self):
        """Permet au gestionnaire de saisir un commentaire sur un tournoi"""
        Tournament.prompt_for_comment(self)
        Tournament.saving_data_tournament(self)
   
    
    
class ControlPlayer:
    """Controlleur qui entre en interaction avec le module player"""

    def __init__(self, player):
        self.player = player
    
    #mettre en attente cette méthode et tester directement la création d'un joueur
    def get_db_lastname(self):
        self.lastname = input("Saisir le nom du joueur").upper()
        Player.players_table.search(Gamer.lastname == self.lastname)
        if None :
            result = input("Voulez_vous ajouter un joueur ? (O/N").upper()
            if result == "O":
                self.add_player()
            else : 
                return self.openmainscreen()
        pass
            
    def add_player(self):
        """Permet la saisie de l'ensemble des données du joueur,
            et l'enregistrement dans la base.
            
        """
        self.lastname = ViewPlayer.prompt_lastname_view(self).upper()
        while self.lastname is None:
            ViewPlayer.prompt_lastname_view(self).upper()
            if self.lastname == '':
                print("Veuillez saisir un nom de famille !")
                ViewPlayer.prompt_lastname_view(self).upper()
                break
    
        self.firstname = ViewPlayer.prompt_firstname_view(self).upper()
        while self.firstname is None:
            ViewPlayer.prompt_firstname_view(self).upper()
            if self.firstname == '':
                print("Veuillez saisir un prénom !")
                ViewPlayer.prompt_firstname_view(self).upper()
                break
        
        self.birthdate = ViewPlayer.prompt_birthdate_view(self)
        while self.birthdate is None:
            ViewPlayer.prompt_birthdate_view(self)
            if self.birthdate == '':
                print("Veuillez saisir une date de naissance")
                ViewPlayer.prompt_birthdate_view(self)
                break
                
        self.gender = ViewPlayer.prompt_gender_view(self).upper()
        while self.gender is None:
            ViewPlayer.prompt_gender_view(self).upper()
            if self.gender == "":
                print("Veuillez saisir un genre ")
                iewPlayer.prompt_gender_view(self).upper()
                break
                
        self.ranking = int(ViewPlayer.prompt_ranking_view(self))
        while True :
            try : 
                self.ranking = int(ViewPlayer.prompt_ranking_view(self))
                break
            except ValueError:
                print("oops : le rang est un chiffre ")
                
        self.score = 0
        
        Player.add_player(self)
        Player.saving_data_player(self)