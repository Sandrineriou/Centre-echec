"""Joueurs d'un tournoi d'échec."""










class Player: 
    """Joueurs d'un tournoi."""
         
    def __init__(self, id_person, lastname, firstname, birthdate, gender, ranking):
        """Initialise les données de la personne et le classement du joueur."""
        self.id_person = id_person
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = 0
    
   
        
    def add_player(self):
        player = {
            "id_person": self.id_person,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "ranking": self.ranking,
            "score" :self.score
        }
        return player
    
    def won_player(self): # via match ?
        """gagne le match."""
        pass

    def draw_player(self): #via match 
        """Partie Nulle."""
        pass
    
    def score_tournoi_player(self): 
        """Totalise le nombre de point gagné lors d'un tournoi."""
        
        
    def ranking_player(self): # pas demandé entrée manuelle : voir la classe Classement qui suit
        """Met à jour le nombre total de point acquis au tournoi avec les points déjà cumulés du joueur."""
        pass






class Ranking(Player): # à voir au fonctionnement si nécessaire un telle classe
    """Classement d'un joueur."""

    def __init__(self, startranking, score, endranking):
        """Initialise le rang initale, le score acquis au tournoi et donc le rang final du joueur"""
        super().__init__
        self.startranking = startranking
        self.score = score
        self.endranking = endranking
        pass
        
        

    def add_score(self):
        """ Ajoute le score total du tournoi au rang initale"""
        pass

    def change_endranking(self): # probléme avec quelle "ranking" modifié : le start ou end ? est-ce n"cessaire de faire cette distinguetion
        """Modifie à tout moment le classement du joueur"""
        pass
        







