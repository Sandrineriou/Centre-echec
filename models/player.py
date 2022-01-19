"""Joueurs d'un tournoi d'échec."""



from actor import Actor


MAX_TOURNAMENTS_PLAYERS = 8

class Player(Actor): 
    """Joueur d'un tournoi."""
         
    def __init__(self, ranking):
        """Initialise les données de la personne et le classement du joueur."""
        self.ranking = ranking
        super().__init__
      
    def add_ranking(self):
        """Ajoute le classement à l'acteur"""
        pass

    def add_tournament_players(self):
        """Ajoute 8 joueurs pour commencer le tournoi."""
        data = Actor.add_actor()
        for joueur in data:
            for i in range(1,MAX_TOURNAMENTS_PLAYERS+1):
                tournament_players = [{}]
                data[i] = tournament_players.append({joueur[i]})
                
                
                return print(tournament_players)
               


    
    def won_player(self): # via match ?
        """gagne le match."""
        pass

    def draw_player(self): #via match 
        """Partie Nulle."""
        pass
    
    def score_tournoi_player(self): # pas là via match
        """Totalise le nombre de point gagné lors d'un tournoi."""
        pass
        
    def ranking_player(self): # pas demandé entrée manuelle : voir la classe Classement qui suit
        """Met à jour le nombre total de point acquis au tournoi avec les points déjà cumulés du joueur."""
        pass

class Ranking(Player): # à voir au fonctionnement si nécessaire un telle classe
    """Classement d'un joueur."""

    def __init__(self, startranking, score, endranking):
        """Initialise le rang initale, le score acquis au tournoi et donc le rang final du joueur"""
        self.startranking = startranking
        self.score = score
        self.endranking = endranking
        
        super().__init__

    def add_score(self):
        """ Ajoute le score total du tournoi au rang initale"""
        pass

    def change_endranking(self): # probléme avec quelle "ranking" modifié : le start ou end ? est-ce n"cessaire de faire cette distinguetion
        """Modifie à tout moment le classement du joueur"""
        pass
        
    
tournament = {'name': 'cerise', 'place': 'crest', 'startdate': '14/01/2022', 'controller_time': 'bullet'}

data1 = {'lastname': 'dupont', 'firstname': 'paul', 'birthdate': '03/05/1945', 'gender': 'T', 'ranking': 28}
data2 = {'lastname': 'dupont', 'firstname': 'pierre', 'birthdate': '03/05/1945', 'gender': 'T', 'ranking': 28}
data3 = {'lastname': 'martin', 'firstname': 'eric', 'birthdate': '12/07/1999', 'gender': 'H', 'ranking': 1235}
data4 = {'lastname': 'boudou', 'firstname': 'amélie', 'birthdate': '02/04/2003', 'gender': 'F', 'ranking': 1098}
data5 = {'lastname': 'minz', 'firstname': 'aurélie', 'birthdate': '13/12/1956', 'gender': 'F', 'ranking': 1355}
data6 = {'lastname': 'zing', 'firstname': 'edouard', 'birthdate': '23/12/1985', 'gender': 'H', 'ranking': 1124}
data7 = {'lastname': 'vindiu', 'firstname': 'shiva', 'birthdate': '17/03/2000', 'gender': 'F', 'ranking': 1278}
data8 = {'lastname': 'papou', 'firstname': 'doudou', 'birthdate': '21/11/1970', 'gender': 'H', 'ranking': 875}
data9 = {'lastname': 'waou', 'firstname': 'elise', 'birthdate': '21/11/1995', 'gender': 'F', 'ranking': 975}

data1.add_tournament_players()
data2.add_tournament_players()
