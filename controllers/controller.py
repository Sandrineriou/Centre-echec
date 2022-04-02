"""Contrôleur des menus"""


from datetime import datetime
from pprint import pprint


from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
players_table = db.table('players')



from views.view import ViewMenu, ViewReport, ViewTournament, ViewPlayer, ViewParticipant
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
        self.niveau1 = ViewMenu.homemenu(self).upper()
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
                return self.person()
            elif self.niveau1 == '3':
                """Affiche le menu pour gérer un participant à un tournoi"""
                return self.participant()
            elif self.niveau1 == '4':
                """Affiche un menu pour l'édition de rapports."""
                return self.report()
            else:
                self.niveau1 = ViewMenu.homemenu(self).upper()

    def game(self):
        """Afffiche le menu du Jeu(tournoi) si choix 1 est sélectionné au niveau principal,
        et gère les choix de l'utilisateur sur les données d'un tournoi.
        """
        self.niveau2 = ViewMenu.gamemenu(self).upper()
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
                self.niveau2 = ViewMenu.gamemenu(self).upper()
            elif self.niveau2 == '3':
                """Ajoute les joueurs dans la 'player_list'."""#voir si affiche la liste des joueurs inscrits plutot
                ControlTournament.build_list_players_control(self)
                ControlParticipant.next_participant_tournament(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()

            elif self.niveau2 == '4':
                """Démarre le tournoi"""
                self.niveau2 = ViewMenu.gamemenu(self).upper()
            elif self.niveau2 == '5' :
                """Propose d'ajouter un commentaire au tournoi, à tout moment."""
                #à reprendre pas possible de l'intégrer dans la sauvegarde
                self.niveau2 = ViewMenu.gamemenu(self).upper()
                
            elif self.niveau2 == '6':
                ControlTournament.show_tournament_control(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()
            
            elif self.niveau2 == '100':
                """Efface la base de données 'tournaments_table'(pas afficher dans ViewPlayer, donnée cachée)."""
                ControlTournament.truncate_tournaments_table_control(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()

            else:
               self.niveau2 = ViewMenu.gamemenu(self).upper()
            
    #pas sure de garder cette méthode : en attente    
    def person(self):
        """Affiche le menu du joueur si choix 2 est sélectionné au niveau principal
        et gère les choix de l'utilisateur sur les données d'un joueur.
        """
        
        self.niveau2 = ViewMenu.personmenu(self).upper()
        while True:
            if self.niveau2 == "Q":
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else :
                    pass
            if self.niveau2 == 'R':
                return self.openmainscreen()
                
            elif self.niveau2 == '1':
                """Interface de recherche d'un joueur."""
                ControlPlayer.show_player_control(self)
                self.niveau2 = ViewMenu.personmenu(self).upper()
 
            elif self.niveau2 == '2':
                """Démarre la création d'un joueur, l'enregistrement dans la base des données saisies."""
                ViewPlayer.add_player_view(self)
                ControlPlayer.add_player_control(self)
                ControlPlayer.next_add_player(self)
                
            elif self.niveau2 == '3' :
                """Propose de supprimer un joueur de la base."""
                ControlPlayer.delete_player_view_control(self)
                self.niveau2 = ViewMenu.personmenu(self).upper()
                
            elif self.niveau2 == '4' :
                """Propose de modifier les données d'un joueur (notamment en cas d'erreur de saisie)."""
                ControlPlayer.modify_player_view_control(self)

            elif self.niveau2 == '5' :
                """Propose de mettre à jour le rang d'un joueur, à tout moment."""
                ControlPlayer.new_ranking_player_control(self)
                self.niveau2 = ViewMenu.personmenu(self).upper()

            elif self.niveau2 == '100':
                """Efface la base de données 'players_table'(pas afficher dans ViewPlayer, donnée cachée)."""
                ControlPlayer.truncate_players_table_control(self)
                self.niveau2 = ViewMenu.personmenu(self).upper()

            else:
                self.niveau2 = ViewMenu.personmenu(self).upper()


    def participant(self):
        """Affiche le menu du joueur si choix 3 est sélectionné au niveau principal
        et gère les choix de l'utilisateur sur les données d'un participant.
        """
        self.niveau2 = ViewMenu.participant_view(self).upper()
        while True:
            if self.niveau2 == "Q":
                """Propose de quitter l'application."""
                output = input("Souhaitez_vous réellement quitter GTE? (O/N)").upper()
                if output == 'O':
                    break
                else :
                    self.niveau2 = ViewMenu.participant_view(self).upper()
            if self.niveau2 == 'R':
                """Affiche le menu précédent."""
                return self.openmainscreen() 
            elif self.niveau2 == '1':
                """Supprime un participant de la liste des joueurs d'un tournoi, avant son démarrage."""
                ControlParticipant.delete_participant_control(self)
                return self.openmainscreen()
            else:
                while True :
                    print("\n Vous n'avez pas choisi le bon !! recommencer...\n")
                    self.niveau2 = ViewMenu.participant_view(self).upper()
                
                    break
    

    def report(self):
        """Affiche le menu des rapports, si choix 4 est sélectionné au niveau principal
        et gère les choix de l'utilisateur sur le rapport sélectionné.
        """
        self.niveau2 = ViewMenu.report_view(self).upper()
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
                """Edite rapport joueurs par ordre alpha."""
                ControlReport.show_all_sorted_alpha_players(self)
                self.niveau2 = ViewMenu.report_view(self).upper()
    
            elif self.niveau2 == '2':
                """Edite rapport joueurs par classements."""
                self.niveau2 = ViewMenu.report_view(self).upper()
            
            elif self.niveau2 == '3' :
                """Edite rapport participants tournoi par ordre alpha."""
                ControlReport.show_all_sorted_alpha_participants(self)
                self.niveau2 = ViewMenu.report_view(self).upper()
                
            elif self.niveau2 == '4' :
                """Edite rapport participants tournoi par classement."""
                
            elif self.niveau2 == '5' :
                """Edite rapport tous les tournois."""
                ControlReport.show_all_tournaments(self)
                self.niveau2 = ViewMenu.report_view(self).upper() 
 
            elif self.niveau2 == '6' :
                """Edite rapport tous les tours d'un tournoi."""
                pass
            elif self.niveau2 == '7' :
                """Edite rapport tous les matchs d'un tournoi.."""
                pass
            else:
                self.niveau2 = ViewMenu.report_view(self).upper()
        

    
class ControlTournament:
    """Contrôleur qui entre en interaction avec le module Tournoi, et la class Vue spécifique au tournoi"""

    def __init__(self, tournament):
        self.tournament = tournament
    
    def add_tournament(self):
        """Regroupe toutes les méthodes permettant l'ajout des attributs d'un tournoi à sa création,
        sérialise les données et les enregistre dans tinydb.
        """  
        ControlTournament.name_tournament_control(self)
        ControlTournament.place_control(self) 
        ControlTournament.controller_time_control(self)
        ControlTournament.startdate_tournament_control(self)
        self.enddate = None
        self.n_rounds = NUMBER_ROUNDS
        self.players_list = []
        self.rounds_tournament = []
        self.list_dict_matchs = []
        self.comment = None
                
        Tournament.get_rounds(self)
        Tournament.serialize_tournament(self)
        DataTournament.saving_data_tournament(self)
        
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
        self.startdate = datetime.now().strftime("%d/%m/%Y")

    def add_comment_tournament_control(self):
        """Permet au gestionnaire de saisir un commentaire sur un tournoi"""
        pass
        
  
    """Méthodes pour construction de la liste des participants avant démarrage du tournoi."""   
    
    def search_list_players_tournament_control(self):
        self.name_tounament = ControlTournament.name_tournament_control(self)
        result = DataTournament.search_name_tournament(self)
        while True :
            if result == []:
                print("\n Le tournoi recherché n'est pas dans la base de données. Faites une nouvelle recherche.\n")
                input('\n Continuer: toucher une touche :')
                return ControlTournament.search_list_players_tournament_control(self)
            else :
                
                for element in result:
                    self.players_list = element['Liste_joueurs']
                    for element in self.players_list :
                        print(element)
                    return self.players_list
            break
     
    def build_list_players_control(self):
        """Intègre les participantsà la liste de joueurs au tournoi sélectionné."""
        ControlTournament.search_list_players_tournament_control(self)
        player = ControlParticipant.search_participant_control(self)
        
        self.players_list.append(player)
        print(self.players_list)
        DataTournament.update_players_list_tournament(self)
        input('\n Continuer (toucher une touche): ')

    

    
    """Méthodes de recherche d'un tournoi."""
    
    def show_tournament_control(self):
        """Recherche d'un tournoi par son nom."""
        ViewTournament.search_name_tournament_view(self)
        self.name_tournament = input("Nom du tournoi: ").upper()
        print('\n')
        result = DataTournament.search_name_tournament(self)
        for element in result:
            print(f"{element.doc_id} : {element}")            
            print('\n')
        input('Continuer (toucher une touche): ')

    
    """Méthode de suppression."""
    def truncate_tournaments_table_control(self):
        """Contrôle de cohérence de saisie du choix de l'utilisateur à effacer la totalité de la table 'Tournaments'."""  

        output = ViewTournament.truncate_tournaments_table_view(self).upper()
        while True :
            if output == 'R':
                return self.game()
            elif output == 'O':
                DataTournament.truncate_tournaments_table(self)
                print("La Table 'Tournaments' a été effacée.")
                break
            else:
                return self.game()


class ControlParticipant:
    """Contrôleur qui entre en interaction avec la liste des joueurs(attr) d'un tournoi sélectionné."""

    
    def search_participant_control(self):
        """Retourne les données du joueur."""
        ViewPlayer.search_player_view(self)
        self.lastname = ViewPlayer.prompt_lastname_view(self).upper()
        self.firstname = ViewPlayer.prompt_firstname_view(self).upper()
        print('\n')
        while True:
            if DataPlayer.search_player(self) == []:
                ControlParticipant.none_player_control(self)
                break
            else:
                for element in DataPlayer.search_player(self):
                    print("Joueur: ID "f'{element.doc_id}', element['lastname'], element['firstname'],"Né le :" , element['birthdate'],
                        element['gender'], "Classement: ", element['ranking'], "Score =", element['score'])
                    output = ViewParticipant.add_participant_view(self).upper()
                    if output == 'O':
                        return element
                    else: 
                        return ControlParticipant.search_participant_control(self)
            input('\n Continuer (toucher une touche): \n')
            break
        
    def none_player_control(self):
        """Affiche une suite à donner quand le participant recherché n'est pas dans la base de données."""
        
        output = ViewPlayer.none_player_database_view(self).upper()
        while True:
            if output == '1':
                return ControlPlayer.add_player_control(self)
            elif output == '2':
                return ControlParticipant.search_participant_control(self)
            elif output == '3':
                return MainMenus.game(self)
            else:
                output = ViewPlayer.none_player_database_view(self).upper()

            break
 
    def next_participant_tournament(self):
        """Choix entre continuer à intégrer un participant dans la liste des joueurs d'un tournoi ou revenir au menu précédent."""
        
        output = ViewTournament.prompt_next_participant_view(self).upper()
        while True:
            if output == 'O':
                ControlTournament.build_list_players_control(self)
                output = ViewPlayer.prompt_next_add_player(self).upper()
            else:             
                break
            break

    

    def delete_participant_control(self):
        """Retire un participant de la liste des joueurs du tournoi sélectionné."""
        
        self.players_list = ControlTournament.search_list_players_tournament_control(self)
        print("\n liste des participants déjà inscrits:\n")
        x = 0
        while x < len(self.players_list):
                print(f"N°:{self.players_list.index(self.players_list[x])} : {self.players_list[x]}") 
                x += 1                  
        output = ViewParticipant.delete_participant_view(self)
        while True:
            if int(output) < len(self.players_list):
                self.players_list.pop(int(output))
                DataTournament.update_players_list_tournament(self)
            else:
                print("vous n'avez pas inscrit le bon numéro")
                break
            input('\n Continuer (toucher une touche): ')
            break
        
    def delete_list_players(self):
        """Vide la liste de joueurs d'un tournoi donné."""
        
        self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
        while True:
            result = DataTournament.search_name_tournament(self)
            for element in result:
                self.players_list = element['Liste_joueurs']
                print(self.players_list)
                if self.players_list == []:
                    print('La liste de joueurs du tournoi est déjà vide')
                    break
                else:
                    self.players_list.clear()
                    DataTournament.update_players_list_tournament(self)
                    print("La liste des joueurs du tournoi vient d'être effacer")
                    break
            input('\n Continuer (toucher une touche): ')
            break
 

class ControlPlayer:
    """Contrôleur qui entre en interaction avec les modules Player, database."""

    def __init__(self, player):
        self.player = player
  

    """Méthodes de recherche d'un joueur."""

    def show_player_control(self):
        """Recherche un joueur par son nom et son prénom et affiche l'ensemble des données."""
        
        ViewPlayer.search_player_view(self)
        self.lastname = ViewPlayer.prompt_lastname_view(self).upper()
        self.firstname = ViewPlayer.prompt_firstname_view(self).upper()
        print('\n')
        result = DataPlayer.search_player(self)
        for element in result:
            print(f"{element.doc_id} : {element}")
            return element
        input('Continuer (toucher une touche): ')
    
    
    """Méthodes d'ajout d'un joueur."""

    def add_player_control(self):
        """Regroupe toutes les méthodes permettant l'ajout des attributs du joueur,
        sérialise les données et les enregistre dans tinydb.
        """

        ControlPlayer.show_player_control(self)
        output = ViewPlayer.prompt_add_player_view(self).upper()
        while True:
            
            if output == 'O':
                ControlPlayer.lastname_control(self)
                ControlPlayer.firstname_control(self)
                ControlPlayer.birthdate_control(self)
                ControlPlayer.gender_control(self)
                ControlPlayer.ranking_control(self)
                self.score = 0
                Player.serialize_player(self)
                DataPlayer.saving_data_player(self)
                break
            else:
                return self.person()

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
                ControlPlayer.add_player_control(self)
                output = ViewPlayer.prompt_next_add_player(self).upper()
            else:             
                return self.person()
   
    
    """Méthodes de suppression d'un joueur"""

    def delete_player_control(self):
        """Supprime les données d'un joueur."""
        
        ControlPlayer.show_player_control(self)
        DataPlayer.delete_player(self)
  
    def delete_player_view_control(self):
        """Contrôle la cohérence de saisie du choix de l'utilisateur à supprimer un joueur dans la base."""
 
        while True:
            output = ViewPlayer.delete_player_view(self).upper()
            if output == 'O':
                ControlPlayer.delete_player_control(self)
                break
            else: 
                return self.person()
        
    def truncate_players_table_control(self):
        """Contrôle de cohérence de saisie du choix de l'utilisateur à effacer la totalité de la table 'Players'."""  

        output = ViewPlayer.truncate_players_table_view(self).upper()
        while True :
            if output == 'R':
                return self.person()
            elif output == 'O':
                DataPlayer.truncate_players_table(self)
                print("La Table 'Players' a été effacée.")
                break
            else:
                output=ViewPlayer.truncate_players_table_view(self).upper()

    
    """Méthodes de modification de données d'un joueur"""

    def modify_player_view_control(self):
        """Contrôle la cohérence de saisie du choix de l'utilisateur
            à modifier les données du joueur dans la base.
            """
        self.output = ViewPlayer.modify_data_player_view(self).upper()
        while True:
            if self.output == 'R':
                return self.person()
            else:
                print("En cours de création, A bientôt !")
                self.output = ViewPlayer.modify_data_player_view(self).upper()
    
    def modify_ranking_player_view_control(self):
        """Contrôle la cohérence de saisie du choix de l'utilisateur,
        à modifier le classement du joueur dans la base.
        """
        ViewPlayer.modify_ranking_player_view(self)
        while True :
            try:
                self.new_ranking = int(ViewPlayer.new_ranking_player_view(self))
                break
            except ValueError:
                print("le retour attendu est un nombre")
        return self.new_ranking

    def new_ranking_player_control(self):
        """Recherche le joueur et affiche son rang actuel, propose de donner son nouveau rang et met à jour la base."""
        
        ControlPlayer.show_player_control(self)

        ControlPlayer.modify_ranking_player_view_control(self)
       
        DataPlayer.update_ranking_player(self)# à modifier car 2 dupont dont 2 changements de classement
        print(DataPlayer.search_player(self))#à modifier car pareil pour le retour va retourner les 2 dupont
        input('Continuer (toucher une touche): ')
        
  




class ControlReport:
    """Contrôleur qui entre en interaction avec le module database."""
    
    def show_all_tournaments(self):
        """Récupére toutes les données en lien avec les tournois."""
     
        while True:   
            DataTournament.search_all_tournaments(self)
            for element in self.all:
                print(f"{element.doc_id} : {element}")
                print('\n')
                input('\n Continuer: toucher une touche :')
            break
    
    def show_all_sorted_alpha_players(self):
    
        while True:
            DataPlayer.search_all_players(self)
            DataPlayer.sorted_all_players_alpha(self)
            input('\n Continuer: toucher une touche :')
            break
    
    def show_all_sorted_alpha_participants(self):
        self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
        result = DataTournament.search_name_tournament(self)
        while True:
            if result == []:
                print("\n Le tournoi recherché n'est pas dans la base de données. Faites une nouvelle recherche.\n")
                input('\n Continuer: toucher une touche :')
            else :
                for element in result:
                    plist = element['Liste_joueurs'] 
                    if plist == []:
                        print("Il n'y a pas de participants inscrits dans la liste des joueurs du tournoi.")
                        break
                    else:
                        print('\n'f"Il y a {len(plist)} joueurs incrits dans la liste des joueurs."'\n')
                        for data in plist:
                            print(data)
                    print('\n')
                    input('\n Continuer: toucher une touche :')  
            break  
        
        
            
      
            
