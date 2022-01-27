"""Déroulement de base du tournoi."""




from models.tournament import Tournament
from models.actor import Actor
from models.player import Players



"""Création d'un nouveau tournoi."""
tournoi = Tournament("cerise", "crest", "14/01/2022", "bullet")
tournoi.new_tournament() 





""" Ajouter joueurs."""

actor1 = Actor(1, "dupont", "paul", "03/05/1945", "T", 28)
actor2 = Actor(2, "dupont", "pierre", "03/05/1945", "T", 28)
actor3 = Actor(3, "martin", "eric", "12/07/1999", "H", 1235)
actor4 = Actor(4, "boudou", "amélie", "02/04/2003", "F", 1098)
actor5 = Actor(5, "minz", "aurélie", "13/12/1956", "F", 1355)
actor6 = Actor(6, "zing", "edouard", "23/12/1985", "H", 1124)
actor7 = Actor(7, "vindiu", "shiva", "17/03/2000", "F", 1278)
actor8 = Actor(8,"papou", "doudou", "21/11/1970", "H", 875)
actor9 = Actor(9, "waou", "elise", "21/11/1995", "F", 975)

actor1.add_actor()
actor2.add_actor()
actor3.add_actor()
actor4.add_actor()
actor5.add_actor()
actor6.add_actor()
actor7.add_actor()
actor8.add_actor()
actor9.add_actor()

player1 = Players(actor1)
player2 = Players(actor2)

player1.get_players()
player2.get_players()







"""L'ordinateur génère des paires de joueurs pour le premier tour."""
pass

"""Lorsque le tour est terminé, entrer les résultats"""
pass

"""Répétez les étapes 3 et 4 pour les tours suivants, jusqu'à ce que tous les tours soient joués et que le tournoi soit terminé"""
pass


