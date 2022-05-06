""" Déroulement d'un Tournoi."""

import datetime
from pprint import pprint





from models.player import Player
from models.round import Round
from models.match import Match

MAX_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_DAY_EVENT = 1


class Tournament:
    """Tournoi."""
    
    
    def __init__(self, name_tournament, place, controller_time, startdate=datetime.datetime.now().strftime("%d/%m/%Y"), 
                n_rounds=NUMBER_ROUNDS, players_list=[], rounds_tournament=[], list_dict_matchs=[]):
         
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
        self.comment = None
            
    def get_rounds(self):
        """Créer la liste des dictionnaires de rounds à venir,
        et créer chaque clé (nom du round).
        """
        self.rounds_tournament = [] 
        i = 1
        for i in range (1,NUMBER_ROUNDS+1):
            while True :
                dico = {f"ROUND_{i}" :{}}
                self.rounds_tournament.append(dico)
                break
        return self.rounds_tournament    
    
    def serialize_tournament(self):
        """Sérialize les instances tournoi une fois saisie à la création d'un tournoi."""

        self.tournament_serialized = {}
        self.tournament_serialized = {
            "Nom_tournoi": self.name_tournament,
            "Lieu": self.place,
            "Date_debut": self.startdate,
            "Date_fin" : self.enddate,
            "Type": self.controller_time,# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
            "Nombre_tours": self.n_rounds,
            "Liste_joueurs": self.players_list,
            "Detail_tours" : self.rounds_tournament,
            "Detail_matchs" : self.list_dict_matchs,
            "Commentaires": self.comment
        }
        return (self.tournament_serialized)

   
 
 
    def build_list_players(self):
        
        self.players_list.append()
        return self.players_list

    def return_list_players(self):
        return print(self.players_list, end='\n\n')

    def sorted_ranking_list(self):
        """Trie la liste des joueurs par leur rang, 
        affiche une liste avec une liste des rangs supérieurs et une liste des rangs inférieurs.
        """

        self.ranking_sorted = sorted(self.players_list, key=lambda x:x['ranking'], reverse=True)
        
        self.half_list = [tuple(
            [[element['lastname'], element['firstname'], element['score']] for element in self.ranking_sorted[0:4]]), 
            tuple([[element['lastname'], element['firstname'], element['score']] for element in self.ranking_sorted[4:8]])
        ]
        return self.half_list
     
    def create_first_pairs_players(self):
        """Affiche une liste des 4 paires pour le rounds 1."""

        self.pairs_players = []
        j=0
        while j < NUMBER_ROUNDS :
            element = (self.half_list[0][j],self.half_list[1][j])
            self.pairs_players.append(tuple(element))
            j += 1
        return self.pairs_players
    
    def store_rounds_tournament(self): # à supprimer ???
        """Ajoute les instances d'un round au tournoi concerné."""

        self.rounds_tournament.append(self.dict_round)
        return self.rounds_tournament

    def show_rounds_tournament(self):
        """Affiche tous les rounds d'un tournoi données,
        et les instances attachées à chaque round.
        """
        return print(self.rounds_tournament, end='\n\n')
    
    def total_score_dict_players(self): 
        """Remplace le score initial du joueur par le score cumulé des matchs et créer une nouvelle liste de joueurs pour le tour suivant."""
        self.increased_score_players = []
        i = 0
        while i < MAX_PLAYERS:
            c = {**self.players_list[i], **self.identifier_sorted[i]}
            self.increased_score_players.append(c)
            i += 1
        return print(self.increased_score_players, end='\n\n')
        
    def sorted_score_list(self):
        """Trie la liste des joueurs par leur score total, si égalité de score par leur rang"""
        a = sorted(self.increased_score_players, key=lambda y: y['ranking'], reverse=True)
        self.score_list = sorted(a, key=lambda x: x['score'], reverse=True)
        print(self.score_list)
        self.return_score_list = [[element['lastname'],element['firstname'], element['score']] for element in self.score_list]
        return print(self.return_score_list, end='\n\n')
    
    def create_pairs_players_next(self):
        """Crée les paires de joueurs pour les tours suivants."""
        self.pairs_players = []
        i = 0
        j = i+1
        pair = [self.return_score_list[i], self.return_score_list[j]]
        self.pairs_players.append(tuple(pair))
        while i+2 < (MAX_PLAYERS-1):
            i = i+2
            j = i+1
            pair = [self.return_score_list[i], self.return_score_list[j]]
            self.pairs_players.append(tuple(pair))
        print("c'est la self pairs players next:")
        print(self.pairs_players)
        return self.pairs_players
    
    def end_tournament(self, enddate, endtime):
        """Termine le tournoi"""
        self.enddate = datetime.datetime.now().strftime("%d/%m/%Y")
        
        
  

