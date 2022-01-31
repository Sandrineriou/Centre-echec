"""Génération des paires de joueurs"""

from models.player import Player


class PairPlayers:
    """Gestion des paires de joueurs"""

    def __init__(self, players_game=[]):
        """Initialise la liste des joueurs"""
        self.players_game = players_game

    def create_pairs_round1(self, pairs_round1 = []):
        """Crée une liste comprenant la moitié des joueurs au classement supérieurs et l'autre moitié au classement inférieurs"""
        self.pairs_round1 = pairs_round1

        upper_half = self.players_game[0:4]
        lower_half = self.players_game[4:8]
        print([upper_half], [lower_half], end='\n\n')
       
        half = [[list(element.values()) for element in upper_half], [list(element.values()) for element in lower_half]]
        
        print(half, end='\n\n')
                
        pairs_round1 = [[half[0][0], half[1][0]], [half[0][1], half[1][1]], [half[0][2], half[1][2]], [half[0][3], half[1][3]]]
          
        return print(pairs_round1, end='\n\n')

       
        

    

        
   



