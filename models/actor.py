"""Acteurs enregistrés dans la base"""


class Actor():
    """toute personne en lien avec le jeu,
    
    joueurs,
    managers,
    """

    def __init__(self, id_person, lastname, firstname, birthdate, gender, ranking):
        """Initialise les données de la personne et le classement du joueur."""
        self.id_person = id_person
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    
        
   