""" Tournoi."""

import datetime

from models.player import Player
from models.round import Round
from models.match import Match

MAX_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_DAY_EVENT = 1


class Tournament:
    """Tournoi."""
    
    
    def __init__(self, name_tournament, place, controller_time,startdate=datetime.datetime.now().strftime("%d/%m/%Y"), n_rounds=NUMBER_ROUNDS, players_list=[], rounds_tournament=[], list_dict_matchs=[]):
         
        """Initialise le nom du tournoi, le lieu, la date de début, le tye de temps de jeu,
        
        une liste de joueur
        
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
            
    def get_rounds(self):
        """Affiche la liste des rounds à venir"""
        self.round = [] 
        i = 1
        for i in range (1,NUMBER_ROUNDS+1):
            self.round.append(f"Round_{i}")
        print(self.round)     
    
    def new_tournament(self):
        """Créer un nouveau tournoi"""
        
        new_tournament = {
            "name_tournament": self.name_tournament,
            "place": self.place,
            "startdate": self.startdate,
            "controller_time": self.controller_time,# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
            "Number Rounds": self.n_rounds,
            "list_rounds" : self.round,
            "players_list": self.players_list,
        }
        return  print(new_tournament, end='\n\n')
 
    def build_list_players(self, player):
        self.players_list.append(player)
        return self.players_list

    def return_list_players(self):
        return print(self.players_list, end='\n\n')

    def sorted_ranking_list(self):
        """Trie la liste des joueurs par leur rang, et affiche une liste avec une liste des rangs supérieurs et une liste des rangs inférieurs"""
        self.ranking_sorted = sorted(self.players_list, key=lambda x:x['ranking'], reverse=True)
        print(self.ranking_sorted, end='\n\n')
        self.half_list = [
            [[element['id_person'],element['lastname'], element['score']] for element in self.ranking_sorted[0:4]], 
            [[element['id_person'],element['lastname'], element['score']] for element in self.ranking_sorted[4:8]]
        ]
        return self.half_list
     
    def create_first_pairs_players(self):
        """Affiche une liste des 4 paires pour le rounds 1"""
        self.first_pairs_players = []
        j=0
        for j in range (0,NUMBER_ROUNDS):
            element = (self.half_list[0][j],self.half_list[1][j])
            self.first_pairs_players.append(element)
        
            while j+1 < NUMBER_ROUNDS :
                j = j + 1
                element = (self.half_list[0][j],self.half_list[1][j])
                self.first_pairs_players.append(element)
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

    def total_score_dict_players(self, other): # en attente de savoir si je garde
        """Remplace le score initial du joueur par le score cumulé des matchs et créer une nouvelle liste de joueurs pour le tour suivant."""
        self.increased_score_players = []
        i = 0
        for i in range(0,1):
            c = {**self.players_list[i], **other[i]}
            self.increased_score_players.append(c)
            while i+1 < MAX_PLAYERS:
                i = i+1
                c = {**self.players_list[i], **other[i]}
                self.increased_score_players.append(c)
        print(self.increased_score_players, end='\n\n')
        
      
    def sorted_score_list(self):
        """Trie la liste des joueurs par leur score total, si égalité de score par leur rang"""
        self.score_list = sorted(self.increased_score_players, key=lambda x: x['score'], reverse=True)
        print(self.score_list)
        self.return_score_list = [[element['id_person'],element['lastname'], element['score']] for element in self.score_list]
        return print(self.return_score_list, end='\n\n')
    
    def create_pairs_players_next(self):
        """Crée les paires de joueurs pour les tours suivants."""
        self.pairs_players_next = []
        i = 0
        j = i + 1
        pair = (self.return_score_list[i], self.return_score_list[j])
        self.pairs_players_next.append(pair)
        while i+2 < (MAX_PLAYERS-1):
            i = i+2
            j=i+1
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
        
    def prompt_for_remarks(self):
        """ Invite à saisir les remarques générales du manager à la fin du tournoi"""
        pass

