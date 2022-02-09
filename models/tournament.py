""" Tournoi."""


from models.functions import get_ranking
from models.player import Player
from models.round import Round
from models.match import Match

MAX_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_DAY_EVENT = 1


class Tournament:
    """Tournoi."""
    
    
    def __init__(self, name_tournament, place, startdate, controller_time, n_rounds=NUMBER_ROUNDS, players_list=[], rounds_tournament=[]):
         
        """Initialise le nom du tournoi, le lieu, la date de début, le tye de temps de jeu,
        
        une liste de joueur
        
        """
        self.name_tournament = name_tournament
        self.place = place
        self.startdate = startdate
        self.controller_time = controller_time
        self.players_list = players_list
        self.enddate = None
        self.n_rounds = n_rounds
        self.rounds_tournament = rounds_tournament
            
    def new_tournament(self):
        """Créer un nouveau tournoi"""
        
        new_tournament = {
            "name_tournament": self.name_tournament,
            "place": self.place,
            "startdate": self.startdate,
            "controller_time": self.controller_time,# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
            "Number Rounds": self.n_rounds,
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
        ranking_sorted = sorted(self.players_list, key=get_ranking, reverse=True)
        print(ranking_sorted, end='\n\n')
        self.half_list = [
            [[element['id_person'],element['lastname'], element['score']] for element in ranking_sorted[0:4]], 
            [[element['id_person'],element['lastname'], element['score']] for element in ranking_sorted[4:8]]
        ]
        return print(self.half_list)
     
    def create_first_pairs_players(self):
        """Affiche une liste des 4 paires pour le rounds 1"""
        first_pairs_players = []
        j=0
        for j in range (0,4):
            element = (self.half_list[0][j],self.half_list[1][j])
            first_pairs_players.append(element)
        
            while j+1 < 4 :
                j = j + 1
                element = (self.half_list[0][j],self.half_list[1][j])
                first_pairs_players.append(element)
            return first_pairs_players

    def store_rounds_tournament(self, data_round):
        """Ajoute les instances d'un round au tournoi concerné"""
        self.rounds_tournament.append(data_round)
        return self.rounds_tournament

    def show_rounds_tournament(self):
        """Affiche tous les rounds d'un tournoi données, et les instances attachées à chaque round"""
        return print(self.rounds_tournament, end='\n\n')

    def store_dict_score_round_tournament(self):
        """Ajoute le joueurs et son résultat sous forme d'un dictionnaire dans une liste"""
        pass
    
    
    def total_score(self):
        """Ajoute le score du match au score initial du joueur"""
        pass
    
    
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

