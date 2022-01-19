"""Tour d'un tournoi."""





class Round:
    """ Tour d'un tournoi"""

    def __init__(self, tournament, name, startdate, starttime, enddate, endtime, player):
        """ Initalise le nom, la date et l'heure du tour"""
        self.tournament = self.name.Tournament() # est accroché à un tournoi
        self.name = name #un round
        self.startdate = startdate
        self.starttime = starttime
        self.enddate = enddate
        self.endtime = endtime
        self.player = player.Player()
       
    def start_round(self):
        """Affiche date et heure de départ du tour"""
        pass

       
    def end_round(self):
        """Affiche date et heure de fin du tour"""
        pass
        
    def prompt_for_score(self):
        """Invite à saisir les scores de chaque joueur et match
        
        enregistre les scores"""
        pass
        
        
        