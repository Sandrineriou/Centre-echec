"""Joueurs d'un tournoi d'échec."""










class Player: 
    """Joueurs d'un tournoi."""
         
    def __init__(self, lastname, firstname, birthdate, gender, ranking=int, score=0):
        """Initialise les données de la personne et le classement du joueur."""
        #j'ai enlevé id_person car redondant avec l'id de tinydb
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
          
    # j'utilise cetteméthode pour sérialisé : il est possible que cetteméthode soit obsolète après intégration de TinyDB : voir à la fin pour la supprimer ou non.
    def serialize_player(self):
        """Sérialise les données du joueur sous forme d'un dictionnaire"""
        self.player_serialized= {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "ranking": self.ranking,
            "score" :self.score
        }
        return self.player_serialized
      
    def deserialize_player(self):
        """Déserialize les instances sérialisées et les transforme en instances utilisables"""
        id_person = self.player_serialized['id_person']
        lastname = self.player_serialized['lastname']
        firstname = self.player_serialized['firstname']
        birthdate = self.player_serialized['birthdate']
        gender = self.player_serialized['gender']
        ranking = self.player_serialized['ranking']
        score = self.player_serialized['score']
        
        self.player_deserialised = Player(
            id_person = id_person,
            lastname = lastname,
            firstname = firstname,
            birthdate = birthdate,
            gender = gender,
            ranking = ranking,
            score = score
        )
        return self.player_deserialised
    
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
        







