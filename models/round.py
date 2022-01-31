"""Tour d'un tournoi."""



from models.tournament import Tournament


class Round:
    """ Tour d'un tournoi"""

    def __init__(self, name_round, startdate, tournament, players_game=[]):
        """Initialise le nom du tournoi, le nom du tour et la liste de joueur"""

        self.name_round = name_round
        self.startdate = startdate
        self.tournament = tournament
        self.players_game = players_game
        
    def create_first_round(self):
        
        round= [self.name_round, self.startdate, self.tournament, self.players_game]
        return print(round, end='\n\n')
   
       
    def end_round(self):
        """Affiche date et heure de fin du tour"""
        pass
        
    def prompt_for_score(self):
        """Invite à saisir les scores de chaque joueur et match
        
        enregistre les scores"""
        pass
        
        
        