""" Déroulement d'un Tournoi."""

import datetime
from pprint import pprint

from tinydb import TinyDB, Query, where

db = TinyDB('db.json')
tournaments_table = db.table('tournaments')


from models.player import Player
from models.round import Round
from models.match import Match

MAX_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_DAY_EVENT = 1


class Tournament:
    """Tournoi."""
    
    
    def __init__(self, name_tournament, place, controller_time,startdate=datetime.datetime.now().strftime("%d/%m/%Y"), 
                n_rounds=NUMBER_ROUNDS, players_list=[], rounds_tournament=[], list_dict_matchs=[], comment=None):
         
        """Initialise le nom du tournoi, le lieu, le tye de temps de jeu, la date de début, le nombre de tour,
        
            une liste de joueur, le détail des tours, le détails des matches jouées,
            
            le commenaire laissé par le gestionnaire du tournoi.
        
        """
        
        self.name_tournament = name_tournament
        self.place = place
        self.controller_time = controller_time
        self.startdate = startdate
        self.players_list = players_list
        self.enddate = None
        self.n_rounds = n_rounds
        self.rounds_tournament = rounds_tournament
        self.list_dict_matchs = list_dict_matchs
        self.comment = comment
            
    def get_rounds(self):
        """Créer la liste des rounds à venir"""
        self.rounds_tournament = [] 
        i = 1
        for i in range (1,NUMBER_ROUNDS+1):
            self.rounds_tournament.append(f"Round_{i}")
        return self.rounds_tournament    
    
    # il se peut qu'avec le base tiny cette méthode saute : à voir aprés écriture complète de tous les paramètres de la base
    def new_tournament(self):
        """Créer un nouveau tournoi"""
        
        new_tournament = {
            "name_tournament": self.name_tournament,
            "place": self.place,
            "startdate": self.startdate,
            "controller_time": self.controller_time,# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
            "number_rounds": self.n_rounds,
            "list_rounds" : self.rounds_tournament,
            "players_list": self.players_list,
            "Détail des matches" : self.list_dict_matchs
        }
        return  pprint(new_tournament, end='\n\n')
        
    def serialize_tournament(self):
        """Sérialize les instances tournoi une fois saisie à la création d'un tournoi."""
        self.tournament_serialized = {}
        self.tournament_serialized = {
            "Nom du Tournoi": self.name_tournament,
            "Lieu": self.place,
            "Date de debut": self.startdate,
            "Date de fin" : self.enddate,
            "Gestion du temps": self.controller_time,# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
            "Nombre de Tours": self.n_rounds,
            "Liste des joueurs": self.players_list,
            "Detail des Tours" : self.rounds_tournament,
            "Detail des matchs" : self.list_dict_matchs,
            "Commentaire": self.comment
        }
        return pprint(self.tournament_serialized)

    def deserialize_tournament(self):
        """Déserialize les instances sérialisées et les transforme en instances utilisables."""
        name_tournament = tournament_serialized['Nom du Tournoi']
        place = tournament_serialized['Lieu']
        startdate = tournament_serialized['Date de début']
        enddate = tournament_serialized['Date de fin']
        controller_time = tournament_serialized['Gestion du temps']
        number_rounds = tournament_serialized['Nombre de Tours']
        players_list = tournament_serialized['Liste des joueurs']
        rounds_tournament = tournament_serialized['Détail des Tours']
        list_dict_matchs = tournament_serialized['Détail des matchs']
        comment = tournament_serialized['Commentaire']
        
        
        
        tournament = Tournament(
            name_tournament = name_tournament,
            place = place,
            stardate = stardate,
            enddate = enddate,
            controller_time = controller_time,
            number_rounds = number_rounds,
            players_list = players_list,
            rounds_tournament = rounds_tournament,
            list_dict_matchs = list_dict_matchs,
            comment = comment
        )
        return tournament
        
    def saving_data_tournament(self):
        """Sauvegarde les instances créées dans la base tinydb."""
        tournaments_table.insert(self.tournament_serialized)
        
    def show_tournament(self):
        """Affiche les instances du tournoi sauvegardé"""
        self.tournament_serialized = tournaments_table.all()
 
    def build_list_players(self, player):
        self.players_list.append(player)
        return self.players_list

    def return_list_players(self):
        return print(self.players_list, end='\n\n')

    def sorted_ranking_list(self):
        """Trie la liste des joueurs par leur rang, et affiche une liste avec une liste des rangs supérieurs et une liste des rangs inférieurs"""
        self.ranking_sorted = sorted(self.players_list, key=lambda x:x['ranking'], reverse=True)
        print(self.ranking_sorted, end='\n\n')
        self.half_list = [tuple(
            [[element['id_person'],element['lastname'], element['score']] for element in self.ranking_sorted[0:4]]), 
            tuple([[element['id_person'],element['lastname'], element['score']] for element in self.ranking_sorted[4:8]])
        ]
        return self.half_list
     
    def create_first_pairs_players(self):
        """Affiche une liste des 4 paires pour le rounds 1"""
        self.first_pairs_players = []
        j=0
        while j < NUMBER_ROUNDS :
            element = (self.half_list[0][j],self.half_list[1][j])
            self.first_pairs_players.append(tuple(element))
            j += 1
        return self.first_pairs_players
    
    def store_rounds_tournament(self, data_round):
        """Ajoute les instances d'un round au tournoi concerné"""
        self.rounds_tournament.append(data_round)
        return self.rounds_tournament

    def show_rounds_tournament(self):
        """Affiche tous les rounds d'un tournoi données, et les instances attachées à chaque round"""
        return print(self.rounds_tournament, end='\n\n')
    
    def store_list_dict_matchs(self, other):# à supprimer semble faire doublon voir modif total score avec other
        """Ajoute la liste de dictionnaire créer après les matchs"""
        self.list_dict_matchs.append(other)
        return print(self.list_dict_matchs, end='\n\n')
    
    def show_list_dict_matchs(self):# à supprimer semble faire doublon voir modif total score avec other
        self.dict_players_matchs = self.list_dict_matchs[0]
        return print(self.dict_players_matchs, end='\n\n')

    def total_score_dict_players(self, other): 
        """Remplace le score initial du joueur par le score cumulé des matchs et créer une nouvelle liste de joueurs pour le tour suivant."""
        self.increased_score_players = []
        i = 0
        while i < MAX_PLAYERS:
            c = {**self.players_list[i], **other[i]}
            self.increased_score_players.append(c)
            i += 1
        return print(self.increased_score_players, end='\n\n')
        
    def sorted_score_list(self):
        """Trie la liste des joueurs par leur score total, si égalité de score par leur rang"""
        a = sorted(self.increased_score_players, key=lambda y: y['ranking'], reverse=True)
        self.score_list = sorted(a, key=lambda x: x['score'], reverse=True)
        print(self.score_list)
        self.return_score_list = [[element['id_person'],element['lastname'], element['score']] for element in self.score_list]
        return print(self.return_score_list, end='\n\n')
    
    def create_pairs_players_next(self):
        """Crée les paires de joueurs pour les tours suivants."""
        self.pairs_players_next = []
        i = 0
        j = i+1
        pair = (self.return_score_list[i], self.return_score_list[j])
        self.pairs_players_next.append(pair)
        while i+2 < (MAX_PLAYERS-1):
            i = i+2
            j = i+1
            pair = (self.return_score_list[i], self.return_score_list[j])
            self.pairs_players_next.append(pair)
        return self.pairs_players_next
    
    def end_tournament(self, enddate, endtime):
        """Termine le tournoi"""
        self.enddate = enddate
        self.endtime = endtime
        pass
        
    def prompt_for_classement(self):
        """ Mise à jour par le manager du tournoi des classements de chaque jour
        
        affiche par joueur le nombre total de points gagné lors du tournoi"""
        pass
        
    def prompt_for_comment(self):
        """ Invite à saisir les remarques générales du manager à la fin du tournoi"""
        return input("Saisir votre commentaire sur le tournoi :")
        

