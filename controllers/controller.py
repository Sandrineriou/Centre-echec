"""Contrôleur des menus"""


from datetime import datetime
from pprint import pprint



from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
players_table = db.table('players')



from views.view import ViewMenu, ViewReport, ViewRound, ViewTournament, ViewPlayer, ViewParticipant, ViewMatch
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from models.database import DataPlayer, DataRound, DataTournament, DataMatch
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
            if self.niveau2 == 'Q':
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
                """Enregistre les données du nouveau tournoi."""
                ViewTournament.tournament_view(self)
                ControlTournament.add_tournament(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()

            elif self.niveau2 == '3':
                """Ajoute les joueurs dans la 'player_list'."""#voir si affiche la liste des joueurs inscrits plutot
                ControlTournament.build_list_players_control(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()

            elif self.niveau2 == '4':
                """Démarre le tournoi ou prépare au démarrage :????
                Génère les premières paires de joueurs, selon, le modèle Suisse qui s'affronteront au Tour1,
                à partir de la liste joueurs du tournoi sélectionné
                et les affiche.
                
                XXXXXXX
                
                """
                
                """Crée les rounds à venir et les enregistre dans la base."""
                
                ControlRound.setting_up_rounds_control(self)
                ControlTournament.setting_up_rounds_tournament_control(self)
                
                """Crée les premières de paires de joueur pour le Round 1."""

                
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

            elif self.niveau2 == '200':
                """Efface la base de données 'rounds_table'(pas afficher dans ViewPlayer, donnée cachée)."""
                ControlRound.truncate_rounds_table_control(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()

            elif self.niveau2 == '300':
                """Efface la base de données 'matchs_table'(pas afficher dans ViewPlayer, donnée cachée)."""
                ControlMatch.truncate_matchs_table_control(self)
                self.niveau2 = ViewMenu.gamemenu(self).upper()

            else:
               
                while True :
                    print("\n Vous n'avez pas choisi le bon !! recommencer...\n")
                    self.niveau2 = ViewMenu.gamemenu(self).upper()
                
                    break
            
            
            
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
                self.niveau2 = ViewMenu.personmenu(self).upper()
                
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
        """Affiche le menu du participant à un tournoi si choix 3 est sélectionné au niveau principal
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
            elif self.niveau2 == '2':
                """Modifie le rang du participant en cours de tournoi :
                met à jour le rang du joueur dans la liste des joueurs du tournoi,
                met à jour la base de données."""
                print("En cours de construction")
                return self.openmainscreen()
            else:
                while True :
                    print("\n Vous n'avez pas choisi le bon !! recommencer...\n")
                    self.niveau2 = ViewMenu.participant_view(self).upper()
                
                    break
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
                ControlReport.show_all_rounds_tournament_control(self)
                self.niveau2 = ViewMenu.report_view(self).upper()
                
            elif self.niveau2 == '7' :
                """Edite rapport tous les matchs d'un tournoi.."""
                DataMatch.search_all_matchs(self)
                ControlReport.show_all_matchs_tournament_control(self)
                self.niveau2 = ViewMenu.report_view(self).upper()

            else:
                self.niveau2 = ViewMenu.report_view(self).upper()
            
        

    
class ControlTournament:
    """Contrôleur qui entre en interaction avec le module Tournoi, et la class Vue spécifique au tournoi"""

    
    def __init__(self, tournament):
        self.tournament = tournament
    
    """Méthodes pour la création et l'enregistrement des données d'un tournoi."""

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
        self.rounds_tournament = [] # voir si possible de modifier et mettre à jour via la table round à créer / créer une méthode pour cela
        self.list_dict_matchs = [] # voir si nécessaire de garder cela ??
        self.comment = None
                
        
        Tournament.serialize_tournament(self)
        DataTournament.saving_data_tournament(self)
        
    def name_tournament_control(self):
        """Contrôle la cohérence de saisie du nom du tournoi."""

        self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
        while True:
            if self.name_tournament == "":
                print("Veuillez saisir un nom de tournoi")
                self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
            else :
                return self.name_tournament
            break
    
    def place_control(self):
        """Controle la cohérence de saisie du nom du lieu du tournoi."""
        self.place = ViewTournament.prompt_place_tournament_view(self).upper()
        while True:
            if self.place == "":
                print("Veuillez saisir un nom de ville")
                self.place = ViewTournament.prompt_place_tournament_view(self).upper()
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
    def setting_up_rounds_tournament_control(self):# sans doute à supprimer .??
        """Contrôle la création des dictionnaires comprenant pour clé le nom des rounds,
        dictionnaires inclus dans la liste 'rounds_tournament' d'un tournoi sélectionné.
        """
        Tournament.get_rounds(self)
        DataTournament.update_data_rounds_tournament(self)
        print('mise à jour round dans tournoi')
        input('\n Continuer (toucher une touche): \n')
        



  
    """Méthodes pour construction de la liste des participants avant démarrage du tournoi,
    et la préparation des premières paires pour démarrer le round 1.
    """   
    
    def search_list_players_tournament_control(self):
        self.name_tounament = ControlTournament.name_tournament_control(self)
        result = DataTournament.search_by_name_tournament(self)
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
        """Intègre les participants dans la liste de joueurs du tournoi sélectionné."""
        self.players_list = ControlTournament.search_list_players_tournament_control(self)
        while True:
            if len(self.players_list) == MAX_PLAYERS :
                print('\n La liste de joueurs est COMPLETE - Le Tournoi peut démarrer \n')
                input('Continuer (toucher une touche): ')
                break
            elif len(self.players_list) < MAX_PLAYERS :
                player = ControlParticipant.search_participant_control(self)
                while True:
                    if player == None:
                        print("\n Veuillez vérifier les données à saisir\n")
                        input('Continuer (toucher une touche): ')
                        break
                    else:
                        self.players_list.append(player)
                        print(self.players_list)
                        DataTournament.update_players_list_tournament(self)
                        input('\n Continuer (toucher une touche): ')
                        break

    def build_first_pairs_players_control(self):
        """A partir de la liste des joueurs, crée la liste des premières paires de joueurs qui vont s'affronter au Round1."""
        self.players_list = ControlTournament.return_list_players_tournament_control(self)
        Tournament.sorted_ranking_list(self)
        self.pairs_players = Tournament.create_first_pairs_players(self)
        print("\n Liste des premières rencontres pour le Round 1:\n")
        for element in self.pairs_players:
            print(element)
        return self.pairs_players
        

   
    """Méthodes de recherche."""
    
    def show_tournament_control(self):
        """Recherche d'un tournoi par son nom."""
        ViewTournament.search_name_tournament_view(self)
        self.name_tournament = input("Nom du tournoi: ").upper()
        print('\n')
        result = DataTournament.search_by_name_tournament(self)
        for element in result:
            print(element)            
            print('\n')
            for key, value in element.items():
                print(f"\033[1m {key}: \033[0m", value)   
        input('Continuer (toucher une touche): ')

    def return_list_players_tournament_control(self):
        """Retourne la liste des joueurs enregistrer pour un tournoi donné."""
        
        """ControlTournament.name_tournament_control(self)"""
        result = DataTournament.search_by_name_tournament(self)
        while True:
            if result == []:
                print("\n Le tournoi recherché n'est pas dans la base de données. Faites une nouvelle recherche.\n")
            else :
                for element in result:
                    plist = element['Liste_joueurs'] 
                    if plist == []:
                        print("Il n'y a pas de participants inscrits dans la liste des joueurs du tournoi.")
                        break
                    else:
                        return(plist)
            print('\n')
            input('\n Continuer: toucher une touche :')          
            break  
        
    
    """Méthode de suppression."""
    def truncate_tournaments_table_control(self):
        """Contrôle de cohérence de saisie du choix de l'utilisateur à effacer la totalité de la table 'Tournaments'."""  

        output = ViewTournament.truncate_tournaments_table_view(self).upper()
        while True :
            if output == 'R':
                break
            elif output == 'O':
                DataTournament.truncate_tournaments_table(self)
                print("La Table 'Tournaments' a été effacée.")
                break
            else:
                break

    def remove_rounds_tournament(self):# A SUPPRIMER QUAND LE DEBUT D'UN ROUND SERA CALE : utiliser pour éviter de recréer un tournoi à chaque erreur de code
        """Efface le contenu de rounds_tournament A SUPPRIMER QUAND TOUT SERA CALER"""
        self.name_tournament = ControlTournament.name_tournament_control(self)
        result = DataTournament.search_by_name_tournament(self)
        for element in result:
            self.rounds_tournament = element['Detail_tours']
            self.rounds_tournament = []
            DataTournament.update_data_rounds_tournament(self)

       


class ControlRound:
    """Contrôleur qui entre en interaction principalement avec le module 'round", et la class Vue spécifique au tour."""

    def setting_up_rounds_control(self):
        """Crée les attributs des rounds du tournoi sélectionné,
        enregistre ces élements dans une liste de tours, 
        et sauvegarde ces élements dans la table 'round' de tinydb.
        """
        self.name_tournament = ControlTournament.name_tournament_control(self)
        ViewRound.create_rounds_view(self)
        i = 1
        for i in range(1, NUMBER_ROUNDS+1):
            while True:
                self.name_tournament = self.name_tournament
                self.name_round = f'Round_{i}'
                self.pairs_players = []
                self.startdatetime = None
                self.enddatetime = None
                self.matchs_round = [] # créer une méthode qui retourne les élément d'une table à créer
                self.data_round = []# suppression possible ? redondant avec l'utilisation de la table 'round'?
                self.values_list = []
                self.list_dict_matchs = []

                self.round_serialized = Round.serialize_round(self)
                DataRound.saving_data_round(self)
                break
        input('\n Continuer (toucher une touche): \n')


    def return_id_rounds_control(self):
        """Affiche la liste des identifiants des rounds créés."""
        


    def return_pairs_players_round1_control(self):
        """Retourne la liste de paires des joueurs du round1."""
        self.pairs_players = ControlTournament.build_first_pairs_players_control(self)
        DataRound.update_pairs_players_round(self)
        input('\n Continuer (toucher une touche): \n')
    
    def get_matchs_control(self):#pass ?
        """Crée le nombre des matches à venir dans le round en cours."""

        pass

    """Méthode de suppression."""
    
    def truncate_rounds_table_control(self):
        """Contrôle de cohérence de saisie du choix de l'utilisateur à effacer la totalité de la table 'Rounds'."""  

        output = ViewRound.truncate_rounds_table_view(self).upper()
        while True :
            if output == 'R':
                break
            elif output == 'O':
                DataRound.truncate_rounds_table(self)
                print("La Table 'Rounds' a été effacée.")
                input('\n Continuer (toucher une touche): \n')
                break
            else:
                break



class ControlMatch:
    """Contrôleur qui entre en interaction avec les matchs d'un round d'un tournoi sélectionné."""

    """Méthode de recherche."""

    def setting_up_matchs_round(self):
        """Créer les premières données des matchs à venir, 
        les enregistre dans la base.
        """

        ControlMatch.create_name_matchs(self)

    
    def create_name_matchs(self):
        i = 1
        for i in range (1,len(self.pairs_players)+1):
            while True:
                self.name_match = f'Match_{i}'
                print(self.name_match)
                self.pair_players = []
                self.data_match = tuple()
                self.match_serialized = Match.serialize_match(self)
                DataMatch.saving_data_match(self)
                break
        input('\n Continuer (toucher une touche): \n')
                
    
    """Méthode de suppression."""
    
    def truncate_matchs_table_control(self):
        """Contrôle de cohérence de saisie du choix de l'utilisateur à effacer la totalité de la table 'Matchs'."""  

        output = ViewMatch.truncate_matchs_table_view(self).upper()
        while True :
            if output == 'R':
                break
            elif output == 'O':
                DataMatch.truncate_matchs_table(self)
                print("La Table 'Matchs' a été effacée.")
                break
            else:
                break

        



class ControlParticipant:
    """Contrôleur qui entre en interaction avec la liste des joueurs(attr) d'un tournoi sélectionné."""

    """Méthode de recherche."""

    def search_participant_control(self):
        """Retourne les données du joueur si le participant existe dans la base
        sinon propose de créer le joueur.
        """
        ViewPlayer.search_player_view(self)
        self.lastname = ControlPlayer.lastname_control(self)
        self.firstname = ViewPlayer.prompt_firstname_view(self).upper()
        print('\n')
        while True:
            if DataPlayer.search_player(self) == []:
                print("\nLa personne n'est pas incrite dans la base de données."
                    "Veuillez créer ce joueur avant de continuer \n")
                break
            else:
                for element in DataPlayer.search_player(self):
                    print("Joueur: ID "f'{element.doc_id}', element['lastname'], element['firstname'],"Né le :" , element['birthdate'],
                        element['gender'], "Classement: ", element['ranking'], "Score =", element['score'])
                    output = ViewParticipant.add_participant_view(self).upper()
                    if output == 'O':
                        return element
                    else: 
                        break
            input('\n Continuer (toucher une touche): \n')
            break
        
    def next_participant_tournament(self):
        """Choix entre continuer à intégrer un participant dans la liste des joueurs d'un tournoi ou revenir au menu précédent."""
        
        output = ViewTournament.prompt_next_participant_view(self).upper()
        while True:
            if output == 'O':
                ControlTournament.build_list_players_control(self)
                output = ViewPlayer.prompt_next_add_player(self).upper()
            else:             
                pass
            break
    
    def show_participant_control(self):#utiliser avec modif rang participant
        """Recherche un participant et affiche ses données, dans un tournoi sélectionné."""

        self.players_list = ControlTournament.search_list_players_tournament_control(self)
        print("\n liste des participants déjà inscrits:\n")
        x = 0
        while x < len(self.players_list):
                print(f"N°:{self.players_list.index(self.players_list[x])} : {self.players_list[x]}") 
                x += 1
        output = ViewParticipant.select_participant_view(self)
        while True:
            if int(output) < len(self.players_list):
                print(self.players_list[int(output)])
                return self.players_list[int(output)]
            else:
                print("vous n'avez pas inscrit le bon numéro")
                output = ViewParticipant.select_participant_view(self)
                
            input('\n Continuer (toucher une touche): ')
            
    
    """Méthodes de modification."""
    #Méthode de modif rang en attente : à intégrer à chaque fin de round avant tri par classement
    def new_ranking_participant_control(self):# mis en attente car modificaiotn rang à tout moment veut dire à toutes les étapes du touirnoi donc sur chaque liste
        """Affiche le participant choisi dans la liste des joueurs, 
        modifie le rang du participant dans la liste des joueurs,
        modifie le rang du joueur dans la base de données."""
        
        participant = ControlParticipant.show_participant_control(self)
        print(participant)
        input('\n Continuer (toucher une touche): ')

    def modify_ranking_participant_view_control(self):
        """Contrôle la cohérence de saisie du choix de l'utilisateur
        pour modifier le classement du participant dans la liste des joueurs.
        """
        ViewParticipant.modify_ranking_participant_view(self)
        while True :
            try:
                self.new_ranking = int(ViewParticipant.new_ranking_participant_view(self))
                break
            except ValueError:
                print("le retour attendu est un nombre")
        return self.new_ranking
    
    

    """Méthodes de suppression."""

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
            result = DataTournament.search_by_name_tournament(self)
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
        self.lastname = ControlPlayer.lastname_control(self)
        self.firstname = ViewPlayer.prompt_firstname_view(self).upper()# bug : il refuse fistname control affiche list vide !!
        print('\n')
        result = DataPlayer.search_player(self)
        
        while True:
            if result == []:
                print("la personne recherchée n'est pas dans la base de données.")
                input('\n Continuer (toucher une touche): ')
                break
            else:
                for element in result:
                    print(f"{element.doc_id} : {element}")
                    input('Continuer (toucher une touche): ')
                    return element
            
            break   
        
      
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
                ControlPlayer.next_add_player(self)
            else:
               break
       
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
                break
   
    
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
        """Contrôle la cohérence de saisie du choix de l'utilisateur
        pour modifier le classement du joueur dans la base.
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
       
        DataPlayer.update_ranking_player(self)
        print(DataPlayer.search_player(self))
        input('Continuer (toucher une touche): ')
        


class ControlReport:
    """Contrôleur qui entre en interaction avec le module database."""
    
    def show_all_sorted_alpha_players(self):
        """Affiche tous les joueurs, par ordre alphabétique, inscrits dans la base de données."""
    
        while True:
            DataPlayer.search_all_players(self)
            DataPlayer.sorted_all_players_alpha(self)
            input('\n Continuer: toucher une touche :')
            break
    
    def show_all_sorted_alpha_participants(self):
        """Affiche tous les participant au tournoi, par ordre alphabétique, inscrits dans la liste dses joueurs du tournoi concerné."""
        
        self.name_tournament = ViewTournament.prompt_name_tournament_view(self).upper()
        result = DataTournament.search_by_name_tournament(self)
        while True:
            if result == []:
                print("\n Le tournoi recherché n'est pas dans la base de données. Faites une nouvelle recherche.\n")
                input('\n Continuer: toucher une touche :')
            else :
                for element in result:
                    plist = element['Liste_joueurs'] 
                    if plist == []:
                        print("Il n'y a pas de participants inscrits dans la liste des joueurs du tournoi.")
                        input('\n Continuer: toucher une touche :')
                        break
                    else:
                        print('\n'f"Il y a {len(plist)} joueurs incrits dans la liste des joueurs."'\n')
                        for data in plist:
                            print(data)
                    print('\n')
                    input('\n Continuer: toucher une touche :')  
            break  
        
    def show_all_tournaments(self):
        """Affiche tous les tournois inscrits dans la base de données."""
     
        while True:   
            DataTournament.search_all_tournaments(self)
            for element in self.all:
                print(f"{element.doc_id} : {element}")
                for key, value in element.items():
                    print(f"\033[4m{key} :\033[0m", value)
                    
                print('\n')
                input('\n Continuer: toucher une touche :')
            break
        
    def show_all_rounds_tournament_control(self):
        """Affiche tous les tours d'un tournoi sélectionné."""

        self.name_tournament = ControlTournament.name_tournament_control(self)
        result = DataRound.search_by_nametournament_round(self)
        while True:
            for element in result:
                print(f"\n {element.doc_id} : {element['Nom_tournoi']} - {element['Round_nom']}")
                for key, value in element.items():
                    print(f"\033[4m{key} :\033[0m", value)
            break
        print('\n')
        input('\n Continuer: toucher une touche :')
    
    def show_all_matchs_tournament_control(self):
        """Affiche tous les matchs d'un tournoi sélectionné."""

        self.name_tournament = ControlTournament.name_tournament_control(self)
        result = DataMatch.search_by_nametournament_matchs(self)
        print(f"Il y a {len(result)} matchs inscrits pour le tournoi {self.name_tournament}")
        while True:
            if result == []:
                print("Je ne trouve pas d'informations, veuillez recommencer")
                input('\n Continuer: toucher une touche :')

            else:  
                
                for element in result:
                    print(f"\n {element.doc_id} : {element['Nom_Round']}-{element['Match_nom']}")
                    for key, value in element.items() :
                        print(f"\033[4m{key} :\033[0m", value)
                        
            break       
   
        print('\n')
        input('\n Continuer: toucher une touche :')
            

       
        
      
            
