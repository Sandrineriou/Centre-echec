"""Déroulement d'un match."""




WIN_POINT = 1
LOSE_POINT = 0
POINTS = [LOSE_POINT, WIN_POINT]
NULL_POINT = 0.50


class Match ():
    """Déroulement d'un match dans un tour."""
    
    def __init__(self,name_tournament, name_round, name_match, pair_players=[], data_match=tuple()):
        """Initialise le nom du match, la paire de joueurs."""
        self.name_tournament = name_tournament
        self.name_round = name_round
        self.name_match = name_match
        self.pair_players = pair_players
        self.data_match = data_match
        

    def serialize_match(self):
        """Sérialize les instances match une fois saisie à la création d'un round."""
        self.match_serialized = {}
        self.match_serialized = {
            'Nom_Tournoi': self.name_tournament,
            'Nom_Round': self.name_round,
            'Match_nom': self.name_match,
            'Match_participants': self.pair_players,
            'Match_resultats': self.data_match
           }
        return self.match_serialized


        
    def designate_players_match(self): 
        """Donne un nom de variable à chaque joueur de la paire attribuée au match."""
        
        self.player1 = [element for element in self.pair_players[0]]
        self.player2 = [element for element in self.pair_players[1]]
        
    def enter_score_match(self):
        """Saisie du score de chaque joueur de la paire, par match."""
        
        print(f"\n \033[4m {self.name_match} : {self.player1},{self.player2}\033[0m \n")
        draw = input("Match Nul ? (O/N) :").upper()
        while draw not in ["O", "N"]:
            draw = input("Match Nul ? (O/N) :")
        if draw == 'O':
            self.player1[2] = self.player2[2] = float(NULL_POINT)
        elif draw =='N':
            print(f"\n {self.player1}")
            while True :
                try:
                    self.player1[2] = int(input("score joueur_1 : "))
                    while self.player1[2] not in POINTS:
                        print('Le score saisit ne correspond pas au point attendu.')
                        self.player1[2] = int(input("score joueur_1 : "))
                    break
                except ValueError:
                    print("OOPS ! On attend un chiffre pour le score joueur_1 : ")
            print(f"\n{self.player2}")
            while True :
                try:
                    self.player2[2] = int(input("score joueur_2 : "))
                    while self.player2[2] not in POINTS:
                        print('Le score saisit ne correspond pas au point attendu.')
                        self.player2[2] = int(input("score joueur_1 : "))
                    break
                except ValueError:
                    print("OOPS ! On attend un chiffre pour le score joueur_2 : ")
               
    def show_data_match(self):
        """Affiche les données du match fini sous forme de tuple."""
        self.data_match = (self.player1, self.player2)
        print(self.data_match, end='\n\n')
        
        return tuple(self.data_match)

    def dict_data_match(self):# j'ai enlevé {self.name_match :tuple(self.data_match)} pour ne laisser que tuple car pb d'extraction pour total score
        """Retourne une liste des résultats par match."""
        
        self.dict_match = tuple(self.data_match)
        return self.dict_match

   

    
    

    
    

      
    
     
       
 
       
        



