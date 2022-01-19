""" Tournoi."""




NUMBER_ROUND = 4
NUMBER_DAY_EVENT = 1


class Tournament:
    """Tournoi."""
    
    
    def __init__(self, name, place, startdate, controller_time):
        
        """Initialise le nom du tournoi, le lieu, le temps de jeu,
        
        les dates et heures et de début, 
        les dates et heures de suspension de tournoi, les dates et heures de repises du tournoi,
        les dates et heures de fin de tournoi,
         et les tours"""
        
        self.name = name
        self.place = place
        self.startdate = startdate
        self.controller_time = controller_time
    
    def new_tournament(self):
        """Créer le nouveau tournoi"""
        
        new_tournoi = {
            "name": self.name,
            "place": self.place,
            "startdate": self.startdate,
            "controller_time": self.controller_time,# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
        }

        
              
        print(new_tournoi)
        return None
        
        """et ajoute à la liste des tournois"""
        pass
        """inscrire le nom du manager du tournoi"""

    def add_manager(self):
        """Ajoute le responsable du tournoi"""
        pass

    def add_player(self):
        """Ajoute une liste de 8 joueurs pour le tournoi"""
        pass
    
    def start_tournament(self, starttime):
        """Démarre un tournoi"""
        self.starttime = starttime
        pass

    def suspend_tournament(self, suspend_date, suspend_time):
        """Suspend le tournoi
        
        si un tournoi est sur plusieurs jours
        si probléme en cours de tournoi
        """ 
        self.suspend_date = suspend_date
        self.suspend_time = suspend_time
        pass

    def continue_tournament(self, continue_date, continue_time):
        """Reprise du tournoi, du jeu"""
        self.continue_date = continue_date
        self.continue_time = continue_time
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



tournoi1 = Tournament("cerise", "crest", "14/01/2022", "bullet")    
tournoi1.new_tournament()
