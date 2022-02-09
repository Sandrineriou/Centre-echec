"""Déroulement de base du tournoi."""




from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match



"""Création d'un nouveau tournoi."""
tournoi = Tournament("cerise", "crest", "14/01/2022", "bullet")
tournoi.new_tournament()

player1 = Player(1, "dupont", "paul", "03/05/1945", "T", 28)
player2 = Player(2, "dupont", "pierre", "03/05/1945", "T", 28)
player3 = Player(3, "martin", "eric", "12/07/1999", "H", 1235)
player4 = Player(4, "boudou", "amélie", "02/04/2003", "F", 1098)
player5 = Player(5, "minz", "aurélie", "13/12/1956", "F", 1355)
player6 = Player(6, "zing", "edouard", "23/12/1985", "H", 1124)
player7 = Player(7, "vindiu", "shiva", "17/03/2000", "F", 1278)
player8 = Player(8,"papou", "doudou", "21/11/1970", "H", 875)


""" Ajouter 8 joueurs.""" 
tournoi.build_list_players(player1.add_player())
tournoi.build_list_players(player2.add_player())
tournoi.build_list_players(player3.add_player())
tournoi.build_list_players(player4.add_player())
tournoi.build_list_players(player5.add_player())
tournoi.build_list_players(player6.add_player())
tournoi.build_list_players(player7.add_player())
tournoi.build_list_players(player8.add_player())

tournoi.return_list_players()

"""Ordinateur génère des paires selon le modèle Suisse"""
tournoi.sorted_ranking_list()
tournoi.create_first_pairs_players()


"""tour 1"""
round_1 = Round("Round_1", tournoi.startdate, tournoi.create_first_pairs_players())
round_1.create_first_round()

match1 = Match('Match_1', tournoi.create_first_pairs_players()[0])
match1.create_match()

match2 = Match('Match_2', tournoi.create_first_pairs_players()[1])
match2.create_match()

match3 = Match('Match_3', tournoi.create_first_pairs_players()[2])
match3.create_match()

match4 = Match('Match_4', tournoi.create_first_pairs_players()[3])
match4.create_match()

round_1.start_round()
round_1.end_round()

match1.enter_score_match()
match1.add_data_match()


match2.enter_score_match()
match2.add_data_match()


match3.enter_score_match()
match3.add_data_match()


match4.enter_score_match()
match4.add_data_match()

round_1.store_matchs_round(match1.list_data_match())
round_1.store_matchs_round(match2.list_data_match())
round_1.store_matchs_round(match3.list_data_match())
round_1.store_matchs_round(match4.list_data_match())

round_1.show_matchs_round()

tournoi.store_rounds_tournament(round_1.list_data_round()) 
tournoi.show_rounds_tournament()


"""Ordinateur génère des paires selon le modèle Suisse, Tour2."""

round_1.build_values_dict_match()






"""Tour 2."""




