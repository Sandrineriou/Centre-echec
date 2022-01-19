"""Déroulement de base du tournoi."""





"""Création d'un nouveau tournoi."""

class Tournoi:
    """Tournoi."""
    
    
    def __init__(self, name, place, start_date, controller_time):
        """Initialise le nom du tournoi, le lieu, les dates et les tours"""
        self.name = name
        self.place = place
        self.start_date = start_date
        self.controller_time = controller_time
       
    
    def create_tournoi(self):
        """créer un nouveau tournoi"""
        new_tournoi = []
        name = new_tournoi.append(self.name)
        place = new_tournoi.append(self.place)
        start_date = new_tournoi.append(self.start_date)
        controller_time = new_tournoi.append(self.controller_time)# choix entre bullet <=1 min et blitz < 5 min coup rapide < 30 minutes
              
        print(new_tournoi)
        return None




    """ Ajouter huit joueurs."""
class Person:
    """Joueurs inscrits dans la base de données"""

    def __init__(self, familyname, surname, birthdate, gender, ranking):
        """Initialise les données de la personne"""
        self.familyname = familyname
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    def add_data_player(self): # va dans person : à requalifier en "actor'"
        """Ajoute un joueur dans la base de données."""
        
        
        data= {"familyname": self.familyname,
                    "surname": self.surname,
                    "birthdate":self .birthdate,
                    "gender" : self.gender,
                    "ranking": self.ranking
                }
        
        return print(data)

    def serialis_players():
        """Obtiens une liste de 8 joueurs pour un tournoi."""
        

      




 

"""L'ordinateur génère des paiers de joueurs pour le premier tour."""
pass

"""Lorsque le tour est terminé, entrer les résultats"""
pass

"""Répétez les étapes 3 et 4 pour les tours suivants, jusqu'à ce que tous les tours soient joués et que le tournoi soit terminé"""
pass


tournoi1 = Tournoi("cerise", "crest", "14/01/2022", "bullet")
tournoi1.create_tournoi()



person1 = Person("dupont", "paul", "03/05/1945", "T", 28)
person2 = Person("dupont", "pierre", "03/05/1945", "T", 28)
person3 = Person("martin", "eric", "12/07/1999", "H", 1235)
person4 = Person("boudou", "amélie", "02/04/2003", "F", 1098)
person5 = Person("minz", "aurélie", "13/12/1956", "F", 1355)
person6 = Person("zing", "edouard", "23/12/1985", "H", 1124)
person7 = Person("vindiu", "shiva", "17/03/2000", "F", 1278)
person8 = Person("papou", "doudou", "21/11/1970", "H", 875)
person9 = Person("waou", "elise", "21/11/1995", "F", 975)

person1.add_data_player()
person2.add_data_player()
person3.add_data_player()
person4.add_data_player()
person5.add_data_player()
person6.add_data_player()
person7.add_data_player()
person8.add_data_player()
person9.add_data_player()




person1.get_tournoi_player()