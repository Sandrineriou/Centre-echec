"""Personne inscrite dans la base de données"""



class Actor:
    """Personne inscrite dans la base de données"""

    def __init__(self, lastname, firstname, birthdate, gender, ranking):
        """Initialise les données de la personne"""
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking #doit aller dans "Player"
        

    def add_actor(self): 
        """Ajoute une personne dans la base de données."""
        
        data = {"lastname": self.lastname,
            "firstname": self.firstname,
            "birthdate":self .birthdate,
            "gender" : self.gender,
            "ranking": self.ranking
        }   
        
        
        return print(data)

person1 = Actor("dupont", "paul", "03/05/1945", "T", 28)
person2 = Actor("dupont", "pierre", "03/05/1945", "T", 28)
person3 = Actor("martin", "eric", "12/07/1999", "H", 1235)
person4 = Actor("boudou", "amélie", "02/04/2003", "F", 1098)
person5 = Actor("minz", "aurélie", "13/12/1956", "F", 1355)
person6 = Actor("zing", "edouard", "23/12/1985", "H", 1124)
person7 = Actor("vindiu", "shiva", "17/03/2000", "F", 1278)
person8 = Actor("papou", "doudou", "21/11/1970", "H", 875)
person9 = Actor("waou", "elise", "21/11/1995", "F", 975)

person1.add_actor()
person2.add_actor()
person3.add_actor()
person4.add_actor()
person5.add_actor()
person6.add_actor()
person7.add_actor()
person8.add_actor()
person9.add_actor()
