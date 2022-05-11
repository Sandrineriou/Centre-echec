"""Joueurs d'un tournoi d'échec."""


class Player:
    """Joueurs d'un tournoi."""

    def __init__(self, lastname, firstname, birthdate, gender, ranking=int, score=0):
        """Initialise les données de la personne et le classement du joueur."""
        # j'ai enlevé id_person car redondant avec l'id de tinydb
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score

    # j'utilise cetteméthode pour sérialisé : il est possible que cetteméthode soit obsolète après intégration de TinyDB : voir à la fin pour la supprimer ou non.
    def serialize_player(self):
        """Sérialise les données du joueur sous forme d'un dictionnaire"""
        self.player_serialized = {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "ranking": self.ranking,
            "score": self.score
        }
        return self.player_serialized
