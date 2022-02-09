"""Tour d'un tournoi."""




from models.match import Match
from models.player import Player


class Round:
    """Tour d'un tournoi."""

    def __init__(self, name_round, startdate, pairs_players=[], startime = None, matchs_round=[], data_round=[], values_list=[]):
        """Initialise le nom du tournoi, la date, les paires de joueurs et les matchs."""

        self.name_round = name_round
        self.startdate = startdate
        self.pairs_players = pairs_players
        self.startime  = startime
        self.enddate = None
        self.endtime = None
        self.matchs_round = matchs_round
        self.data_round = data_round
        self.values_list = values_list

    def create_first_round(self):
        """Affiche les attributs du premier round."""
        
        round= [self.name_round, self.startdate, self.pairs_players]
        return print(round, end='\n\n')
    
    def start_round(self):
        """Affiche heure de début du tour."""
        
        starttime = 0
        return print("heure de début du tour: 0")
       
    def end_round(self):
        """Affiche heure de fin du tour."""
        
        endtime = 0
        return print("heure de fin du tour: 0", end='\n\n')

    def store_matchs_round(self, matchs):
        """Ajoute les résultats des 4 matchs d'un round dans une liste."""
        self.matchs_round.append(matchs)
        return self

    def show_matchs_round(self):
        """Affiche tous les matchs d'un round : données de joueurs et score."""
        return print(self.matchs_round, end='\n\n')
        
    def list_data_round(self):
        """Rassemble les informations d'un round dans une liste.""" #rajouter les dates et heures 
        self.data_round = [self.name_round, self.startdate, self.startime, self.pairs_players, self.enddate, self.endtime, self.matchs_round]
        return self.data_round

    def build_values_dict_match(self):
        """Transforme les instances de data_match sous forme de dictionnaire, pour traitement des scores et tri."""
        
        for players1 in self.matchs_round:
            i = 0
            for i in range(0,4):
                scores = (self.matchs_round[i][0])
                players1.append(scores)
                while i+1 < 4:
                    i = i + 1
                    scores = (self.matchs_round[i][0])
                    players1.append(scores)
            print(players1)
                
        
            j = 0
            for players2 in self.matchs_round:
                for j in range (0,4):
                    scores = (self.matchs_round[j][1])
                    players2.append(scores)
                    while j+1 < 4:
                        j = j + 1
                        scores = (self.matchs_round[j][1])
                        players2.append(scores)
            print(players2)
           
        self.values_list = players1 + players2
        return print(self.values_list)
    
    def show_dict_matchs_round(self):
        """Affiche tous les matchs d'un round : données de joueurs et score comme valeurs d'une dictionnaire."""
        print(self.dict_matchs_round)
        pass
        
    
    def build_list_dict_matchs(self):
        """Affiche une liste de dictionnaires contenant les 8 joueurs avec le score, de chacun, mis à jour."""
        
        key_list = ['id_person', 'lastname', 'score']
        list_dict_matchs = []
        l = 0
        for l in range (0, len(self.values_list)):

            dict_from_list = {k: v for k, v in zip(key_list, self.values_list[l])}
            list_dict_matchs.append(dict_from_list)

            while l+1 < len(self.values_list):
                l = l + 1
                dict_from_list = {k: v for k, v in zip(key_list, self.values_list[l])}
                list_dict_matchs.append(dict_from_list)

        pass


    



       
        


   
          
        
      

       



       
        