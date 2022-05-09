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

    def create_list_played_pairs(self):
        """Crée une liste vide qui va cumuler toutes les paires jouées."""
        self.played_pairs = []
        return self.played_pairs
    
    
    
    def store_rounds_tournament(self): # à supprimer ???
        """Ajoute les instances d'un round au tournoi concerné."""

        self.rounds_tournament.append(self.dict_round)
        return self.rounds_tournament

    def show_rounds_tournament(self):
        """Affiche tous les rounds d'un tournoi données,
        et les instances attachées à chaque round.
        """
        print(" c'est le rounds_tournament list avec toutes les infos des orunds d'une tournoi")
        print(self.rounds_tournament, end='\n\n')
        return self.rounds_tournament
    
    def total_score_dict_players(self): 
        """Remplace le score initial du joueur par le score cumulé des matchs et créer une nouvelle liste de joueurs pour le tour suivant."""
        self.increased_score_players = []
        i = 0
        while i < MAX_PLAYERS:
            c = {**self.players_list[i], **self.identifier_sorted[i]}
            self.increased_score_players.append(c)
            i += 1
        print("C'est la inscreased_score_players list")
        print(self.increased_score_players, end='\n\n')
        return self.increased_score_players

    def sorted_score_list(self):
        """Trie la liste des joueurs par leur score total, si égalité de score par leur rang"""
        a = sorted(self.increased_score_players, key=lambda y: y['ranking'], reverse=True)
        self.score_list = sorted(a, key=lambda x: x['score'], reverse=True)
        print("c'est la score_list trié par le score et le rang")
        print(self.score_list)
        return self.score_list

    def return_id_score_list(self):
        """Retourne une liste de l'attribut ID_person des joueurs."""
        self.id_score_list = [element['id_person'] for element in self.score_list]
        print("c'est la id score list")
        print(self.id_score_list)
        return self.id_score_list

    def test_new_pairs(self):
        """Sélectionne une paire,
        compare avec les paires déjà jouées,
        et en fonction applique une des méthode de créaiton de paires.
        """

        self.new_pairs = []
        while True :  
            try :
                j = 1
                pair = [self.id_score_list[0], self.id_score_list[j]]
                if pair not in self.played_pairs:
                    self.new_pairs.append(pair)
                    self.id_score_list.pop(j)
                    self.id_score_list.pop(0)
                else :  
                    if j+1 < len(self.id_score_list):
                        j += 1
                        pair = [self.id_score_list[0], self.id_score_list[j]]
                        if pair not in self.played_pairs:
                            self.new_pairs.append(pair)
                            self.id_score_list.pop(j)
                            self.id_score_list.pop(0)
                        else:            
                            j += 1
                            pair = [self.id_score_list[0], self.id_score_list[j]]
                            if pair not in self.played_pairs:
                                self.new_pairs.append(pair)
                                self.id_score_list.pop(j)
                                self.id_score_list.pop(0)
            except IndexError:
                break
                                
        print("cest la id_score_list qui doit être vide")
        print(self.id_score_list)
        print("c'est la new-pairs qui doit être au nombre de 4 paires avec les ID")
        print(self.new_pairs)
        return self.new_pairs

    def return_pairs_players_next(self):
        """Retourne la liste des paires à joueur avec les attributs nom, prénom et score.""" 
        self.pairs_players = []
        i = 0
        j = 0
        while True:
            pp = []
            for element in self.score_list :
                if element['id_person'] == self.new_pairs[i][j]:
                    p1 = [element['lastname'], element['firstname'], element['score']]
                    pp.append(p1)
                    break
            for element in self.score_list :
                if element['id_person'] == self.new_pairs[i][j+1]:
                    p2 = [element['lastname'], element['firstname'], element['score']]
                    pp.append(p2)
                    break
            self.pairs_players.append(pp)
            
            while i+1 < len(self.new_pairs):
                pp = []
                i += 1
                for element in self.score_list :
                    if element['id_person'] == self.new_pairs[i][j]:
                        p1 = [element['lastname'], element['firstname'], element['score']]
                        pp.append(p1)
                        break
                for element in self.score_list :
                    if element['id_person'] == self.new_pairs[i][j+1]:
                        p2 = [element['lastname'], element['firstname'], element['score']]
                        pp.append(p2)
                        break
                self.pairs_players.append(pp)
            break

        print("c'est la nouvelle pairs players list next")
        print(self.pairs_players)
        return self.pairs_players

    
    def return_sorted_score_list(self):
        """Retourne certains éléments de la score_list."""
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
        
    
    

    
  

