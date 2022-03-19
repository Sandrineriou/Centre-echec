"""Déroulement d'un match."""



WIN_POINT = 1
LOSE_POINT = 0
NULL_POINT = 0.50


class Match ():
    """Déroulement d'un match dans un tour."""
    
    def __init__(self,round, name_match, pair_players=[], data_match=tuple(), list_matchs=[]):
        """Initialise le nom du match, la paire de joueurs."""
        self.round = round
        self.name_match = name_match
        self.pair_players = pair_players
        self.data_match = data_match
        self.list_matchs = list_matchs

        
    def create_match(self): 
        """Assigne une paire de joueur au match."""
        
        self.player1 = [element for element in self.pair_players[0]]
        self.player2 = [element for element in self.pair_players[1]]
        return print(f"{self.round} - {self.name_match} : {self.player1},{self.player2}", end='\n\n')
    
    def enter_score_match(self):
        """Saisie du score de chaque joueur de la paire, par match."""
        
        print(f"{self.name_match} : {self.player1},{self.player2}")
        draw = input("Match Nul ? (o/n) :")
        while draw not in ["o", "n"]:
            draw = input("Match Nul ? (o/n) :")
        if draw == 'o':
            self.player1[2] = self.player2[2] = float(NULL_POINT)
        elif draw =='n':
            print(f"{self.player1}")
            while True :
                try:
                    self.player1[2] = int(input("score joueur_1 : "))
                    break
                except ValueError:
                    print("OOPS ! On attend un chiffre pour le score joueur_1 : ")
            print(f"{self.player2}")
            while True :
                try:
                    self.player2[2] = int(input("score joueur_2 : "))
                    break
                except ValueError:
                    print("OOPS ! On attend un chiffre pour le score joueur_2 : ")
               
    def show_data_match(self):
        """Affiche les données du match fini sous forme de tuple."""
        self.data_match = (self.player1, self.player2)
        return print(tuple(self.data_match), end='\n\n')

    def list_data_match(self):
        """Retourne une liste des résultats par match."""
        
        self.list_match = [element for element in self.data_match]
        return tuple(self.list_match)

   

    
    

    
    

      
    
     
       
 
       
        



