"""Acteur qui dirige le tournoi = Manager"""

from .actor import Actor

class Manager(Actor):
    """Acteur qui gère un tournoi
    
    enregistre les données
    """

    def __init__(self, access_code, tounament):
        self.access_code = access_code
        self.tournament = self.name.Tournament()
        super().__init__

    
    def new_access_code(self):
        """création du 1er mot de passe à l'enregistrement de la personne"""
        pass

    def change_access_code(self):
        """Modifie le mot de passe du manager"""

    def add_actor(self):#bof
        """Ajoute des acteurs dans la base"""
    
    def select_actor(self):#bof
        """recherche une personne dans la base"""
        pass
    
    def select_category(self):#bof
        """Choix entre joueur ou manager""" 
        pass

    def add_tournament_player(self):#bof
        """Ajoute 8 joueurs au tournoi"""
        pass

