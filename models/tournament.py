""" Déroulement d'un Tournoi."""

import datetime
from itertools import combinations
from re import I

MAX_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_DAY_EVENT = 1


class Tournament:
    """Tournoi."""

    def __init__(self, name_tournament, place, controller_time, startdate=datetime.datetime.now().strftime("%d/%m/%Y"),
                 n_rounds=NUMBER_ROUNDS, players_list=[], rounds_tournament=[], score_list=[]):

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
        self.score_list= score_list
        self.comment = None

    def get_rounds(self):
        """Créer la liste des dictionnaires de rounds à venir,
        et créer chaque clé (nom du round).
        """
        self.rounds_tournament = []
        i = 1
        for i in range(1, NUMBER_ROUNDS+1):
            while True:
                dico = {f"ROUND_{i}": {}}
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
            "Date_fin": self.enddate,
            "Type": self.controller_time,  # choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
            "Nombre_tours": self.n_rounds,
            "Liste_joueurs": self.players_list,
            "Detail_tours": self.rounds_tournament,
            "Scores_finaux": self.score_list,
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

        self.ranking_sorted = sorted(self.players_list, key=lambda x: x['ranking'], reverse=True)

        self.half_list = [tuple(
            [[element['lastname'], element['firstname'], element['score']] for element in self.ranking_sorted[0:4]]),
            tuple([[element['lastname'], element['firstname'], element['score']] for element in self.ranking_sorted[4:8]])
        ]
        return self.half_list

    def create_first_pairs_players(self):
        """Affiche une liste des 4 paires pour le rounds 1."""

        self.pairs_players = []
        j = 0
        while j < NUMBER_ROUNDS:
            element = (self.half_list[0][j], self.half_list[1][j])
            self.pairs_players.append(tuple(element))
            j += 1
        return self.pairs_players

    def create_list_played_pairs(self):
        """Crée une liste vide qui va cumuler toutes les paires jouées."""
        self.played_pairs = []
        return self.played_pairs

    def store_rounds_tournament(self):  # à supprimer ???
        """Ajoute les instances d'un round au tournoi concerné."""

        self.rounds_tournament.append(self.dict_round)
        return self.rounds_tournament

    def show_rounds_tournament(self):  # utilité ? effacé de store rouinds tournament à voir
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
        return self.increased_score_players

    def sorted_score_list(self):
        """Trie la liste des joueurs par leur score total, si égalité de score par leur rang"""
        a = sorted(self.increased_score_players, key=lambda y: y['ranking'], reverse=True)
        self.score_list = sorted(a, key=lambda x: x['score'], reverse=True)
        return self.score_list

    def return_id_score_list(self):
        """Retourne une liste de l'attribut ID_person des joueurs."""
        self.id_score_list = [element['id_person'] for element in self.score_list]
        return self.id_score_list

    def new_associate_pairs(self):
        """Associe le joueur 1 avec le 2 tant que c'est possible, cesse une fois qu la conditions n'est plus bonne."""
        
        self.new_pairs = []
        while True:
            try:
                pair = [self.id_score_list[0], self.id_score_list[1]]
                if tuple(pair) not in self.played_pairs:
                    self.new_pairs.append(tuple(pair))
                    self.id_score_list.pop(1)
                    self.id_score_list.pop(0)
                else :
                    break
            except IndexError:
                break
        return self.id_score_list

    def combinations_pairs(self):
        """Propose toutes les combinations possibles avec les paires non jouées restantes."""

        self.no_played_pairs = []
        for element in list(combinations(self.id_score_list, 2)):
            while True:
                if element not in self.played_pairs:
                    self.no_played_pairs.append(element)
                break
        return self.no_played_pairs
      
    def new_pairs_next(self):
        """Crée de nouvelles paires à l'aide des combinaisons possibles non jouées."""
        while True:
            while self.id_score_list != []:
                self.new_pairs.append(self.no_played_pairs[0])
                
                for element in self.no_played_pairs[0]:
                    
                    self.id_score_list.remove(element)
                Tournament.combinations_pairs(self)
            break
      
        return self.new_pairs

    def return_pairs_players_next(self):
        """Retourne la liste des paires à joueur avec les attributs nom, prénom et score."""
        self.pairs_players = []
        i = 0
        j = 0
        while True:
            pp = []
            for element in self.score_list:
                if element['id_person'] == self.new_pairs[i][j]:
                    p1 = [element['lastname'], element['firstname'], element['score']]
                    pp.append(p1)
                    break
            for element in self.score_list:
                if element['id_person'] == self.new_pairs[i][j+1]:
                    p2 = [element['lastname'], element['firstname'], element['score']]
                    pp.append(p2)
                    break
            self.pairs_players.append(pp)

            while i+1 < len(self.new_pairs):
                pp = []
                i += 1
                for element in self.score_list:
                    if element['id_person'] == self.new_pairs[i][j]:
                        p1 = [element['lastname'], element['firstname'], element['score']]
                        pp.append(p1)
                        break
                for element in self.score_list:
                    if element['id_person'] == self.new_pairs[i][j+1]:
                        p2 = [element['lastname'], element['firstname'], element['score']]
                        pp.append(p2)
                        break
                self.pairs_players.append(pp)
            break
        return self.pairs_players

    

    def end_tournament(self):
        """Termine le tournoi"""
        self.enddate = datetime.datetime.now().strftime("%d/%m/%Y")
