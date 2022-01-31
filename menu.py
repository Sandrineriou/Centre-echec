"""Déroulement de base du tournoi."""




from models.tournament import Tournament
from models.actor import Actor
from models.player import Player
from models.round import Round
from models.pairplayer import PairPlayers
from models.game import Game


"""Création d'un nouveau tournoi."""
tournament = Tournament("cerise", "crest", "14/01/2022", "bullet")
tournament.new_tournament() 

""" Ajouter 8 joueurs."""

actor1 = Actor(1, "dupont", "paul", "03/05/1945", "T", 28)
actor2 = Actor(2, "dupont", "pierre", "03/05/1945", "T", 28)
actor3 = Actor(3, "martin", "eric", "12/07/1999", "H", 1235)
actor4 = Actor(4, "boudou", "amélie", "02/04/2003", "F", 1098)
actor5 = Actor(5, "minz", "aurélie", "13/12/1956", "F", 1355)
actor6 = Actor(6, "zing", "edouard", "23/12/1985", "H", 1124)
actor7 = Actor(7, "vindiu", "shiva", "17/03/2000", "F", 1278)
actor8 = Actor(8,"papou", "doudou", "21/11/1970", "H", 875)


players = Player()


player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()
player7 = Player()
player8 = Player()


player1.add_actors(actor1)
player2.add_actors(actor2)
player3.add_actors(actor3)
player4.add_actors(actor4)
player5.add_actors(actor5)
player6.add_actors(actor6)
player7.add_actors(actor7)
player8.add_actors(actor8)


players.return_players()

players.game = Player()
players_game = (players.sorted_list())









"""L'ordinateur génère des paires de joueurs pour le premier tour."""
# création du premier tour :
round = Round("Round 1", "22/02/22", tournament.name, players_game)

round.create_first_round()

players_game = PairPlayers(players.sorted_list())
players_game.create_pairs_round1()













