"""Déroulement d'un match."""


WIN_POINT = 1
LOSE_POINT = 0
NULL_POINT = 0.50


class Match ():
    """Déroulement d'un match dans un tour."""
    
    def __init__(self, name, pairplayers, startdate, starttime, enddate, endtime):
        """Initialise la paire de joueur et les résultats"""
        self.name = name
        self.pairplayers = pairplayers
        self.startdate = startdate
        self.starttime = starttime
        self.enddate = enddate
        self.endtime = endtime

    def give_name_match(self):
        
        name = input("Donner un nom au match (1,2,3): ")
        
        return print(name)
    
    def add_pairplayers(self):
        """Ajoute la paire de joueur qui va s'affronter"""
        pass
    
    def start_match(self):
        """Ajoute date et et heure de début"""
        pass

    def end_match(self):
        """Ajoute date et heure de fin"""
    
    def score_match(self):
        """Inscrit le score à chaque joueur de la paire"""
        """null = input("Match Nul : (Y/n)")
        
        if n is not null:"""

        winner = input("Inscire le nom du gagnant de la paire: ")#
        pass #voir comment inscrire le socre : auto, manuel
        loser = input("Inscrire le nom du perdant de la paire: ")
        pass
     
       
 
       
        """print(f'"Dans le {name}, {player} ont gagné {NUL_POINT} chacun")"""

        return print(f"{winner} : {WIN_POINT}, {loser} : {LOSE_POINT}")
        

match1 = Match(name="matcha", player="dupont")
match1.score_match()



