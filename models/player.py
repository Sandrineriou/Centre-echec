"""Joueurs d'un tournoi d'échec."""





from models.actor import Actor
from models.functions import get_ranking, get_lastname



class Player: 
    """Joueurs d'un tournoi."""
         
    def __init__(self, players=[]):
        """Initialise une liste d'acteurs."""
        self.players = players
    
    def add_actors(self, actor):
        """Ajoute les données des acteurs dans une liste"""
        actor = {
            "id_person": actor.id_person,
            "lastname": actor.lastname,
            "firstname": actor.firstname,
            "ranking": actor.ranking
        }
        self.players.append(actor)
        
    def return_players(self):
        """Retourne une liste de joueurs pour le tournoi"""
      
        return print([actor for actor in self.players], end='\n\n')

    def sorted_list(self, players_game=[]):
        self.players_game = players_game
        players_game = sorted(self.players, key=get_ranking, reverse=True)
        print(players_game, end='\n\n')
        
        return players_game

    


    def won_player(self): # via match ?
        """gagne le match."""
        pass

    def draw_player(self): #via match 
        """Partie Nulle."""
        pass
    
    def score_tournoi_player(self): # pas là via match
        """Totalise le nombre de point gagné lors d'un tournoi."""
        pass
        
    def ranking_player(self): # pas demandé entrée manuelle : voir la classe Classement qui suit
        """Met à jour le nombre total de point acquis au tournoi avec les points déjà cumulés du joueur."""
        pass






class Ranking(Player): # à voir au fonctionnement si nécessaire un telle classe
    """Classement d'un joueur."""

    def __init__(self, startranking, score, endranking):
        """Initialise le rang initale, le score acquis au tournoi et donc le rang final du joueur"""
        super().__init__
        self.startranking = startranking
        self.score = score
        self.endranking = endranking
        pass
        
        

    def add_score(self):
        """ Ajoute le score total du tournoi au rang initale"""
        pass

    def change_endranking(self): # probléme avec quelle "ranking" modifié : le start ou end ? est-ce n"cessaire de faire cette distinguetion
        """Modifie à tout moment le classement du joueur"""
        pass
        







