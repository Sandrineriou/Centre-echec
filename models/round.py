"""Tour d'un tournoi."""



import datetime
from models.match import Match
from models.player import Player


NUMBER_ROUNDS = 4

class Round:
    """Tour d'un tournoi."""

    def __init__(self, name_round, pairs_players=[], startdatetime = None, matchs_round=[], data_round=[], values_list=[], list_dict_matchs=[]):
        """Initialise le nom du tournoi, la date, les paires de joueurs et les matchs."""

        self.name_round = name_round
        self.pairs_players = pairs_players
        self.startdatetime  = startdatetime
        self.enddatetime = None
        self.matchs_round = matchs_round
        self.data_round = data_round
        self.values_list = values_list
        self.list_dict_matchs = list_dict_matchs
    
    def get_matches(self):
        """Crée le nombre de matchs contenus dans un round."""
        self.match = []
        i = 1
        for i in range (1,len(self.pairs_players)+1):
            self.match.append(f"Match{i}")
        print(self.match)     
            
    def create_round(self):
        """Affiche les attributs du round."""
        
        round= {"name_round": self.name_round, "list paires joueurs": self.pairs_players, "list matchs": self.match}
        return print(round, end='\n\n')
   
    def start_round(self):
        """Affiche heure de début du tour."""
        
        self.startdatetime = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")
        return print(f"heure de début du tour {self.name_round} : {self.startdatetime}")
       
    def end_round(self):
        """Affiche date et heure de fin du tour."""
        print(input("Appuyer sur la touche 'Entrée' quand le tour est terminé"))
        self.enddatetime = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")
        return print(f"Date et heure de fin du tour {self.name_round}: {self.enddatetime}", end='\n\n')

    def create_new_list_matchs(self):
        """Crée une lsite vide pour recevoir les matchs d'un round."""
        self.matchs_round = []
        return self.matchs_round
    
    def store_matchs_round(self, matchs):
        """Ajoute les résultats des matchs d'un round dans une liste."""
        return self.matchs_round.append(matchs)

    def show_matchs_round(self):
        """Affiche tous les matchs d'un round : données de joueurs et score."""
        return print(self.matchs_round)
       
        
    def list_data_round(self):
        """Rassemble les informations d'un round dans une liste.""" #rajouter les dates et heures 
        self.data_round = [self.name_round, self.startdatetime, self.enddatetime, self.matchs_round]
        return self.data_round

    def create_new_list_scores(self):
        """Crée une liste pour recevoir les données des paires avec le score additionné"""
        self.new_scores = []
        return self.new_scores

    def add_scores_matchs_round(self):
        """Cumule les scores de round en round"""
        for i in range(len(self.pairs_players)):
            resultat = [self.pairs_players[i][0][2]+self.matchs_round[i][0][2], self.pairs_players[i][1][2]+self.matchs_round[i][1][2]]
            self.new_scores.append(resultat)

            self.new_list = self.matchs_round.copy()
            self.new_list[i][0][2] = self.new_scores[i][0]
            self.new_list[i][1][2] = self.new_scores[i][1]

            return self.new_list
       

    def build_values_dict_match(self):
        """Transforme les instances de data_match sous forme de dictionnaire, pour traitement des scores et tri."""
        players1 = []      
        for i in range(0,len(self.pairs_players)):
            players1.append(self.new_list[i][0])
        players2 = []
        for j in range (0,len(self.pairs_players)):
            players2.append(self.matchs_round[j][1])
        self.values_list = players1 + players2
        return print(self.values_list)

    def build_list_dict_matchs(self):
        """Affiche une liste de dictionnaires contenant les 8 joueurs avec le score du match fini, trié par identifiant."""
        
        key_list = ['id_person', 'lastname', 'score']
        self.list_dict_matchs = []
        
        for l in range (0, len(self.values_list)):

            dict_from_list = {k: v for k, v in zip(key_list, self.values_list[l])}
            self.list_dict_matchs.append(dict_from_list)
        self.identifier_sorted = sorted(self.list_dict_matchs, key=lambda x: x['id_person'])
        return self.identifier_sorted
        
   
    
        

       
        


   
          
        
      

       



       
        