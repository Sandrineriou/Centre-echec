"""Déroulement de base du tournoi."""




from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match



"""Création d'un nouveau tournoi."""
tournoi = Tournament("cerise", "crest", "bullet")

tournoi.get_rounds()
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

"""Ordinateur génère des paires selon le modèle Suisse, Tour 1."""
tournoi.sorted_ranking_list()
tournoi.create_first_pairs_players()


"""tour 1"""


round_1 = Round(tournoi.round[0], tournoi.create_first_pairs_players())
round_1.get_matches()
round_1.create_round()

match1 = Match(round_1.name_round, round_1.match[0], tournoi.create_first_pairs_players()[0])
match1.create_match()

match2 = Match(round_1.name_round, round_1.match[1], tournoi.create_first_pairs_players()[1])
match2.create_match()

match3 = Match(round_1.name_round, round_1.match[2], tournoi.create_first_pairs_players()[2])
match3.create_match()

match4 = Match(round_1.name_round, round_1.match[3], tournoi.create_first_pairs_players()[3])
match4.create_match()

round_1.start_round()
round_1.end_round()

match1.enter_score_match()
match1.show_data_match()

match2.enter_score_match()
match2.show_data_match()

match3.enter_score_match()
match3.show_data_match()

match4.enter_score_match()
match4.show_data_match()

round_1.create_new_list_matchs()
round_1.store_matchs_round(match1.list_data_match())
round_1.store_matchs_round(match2.list_data_match())
round_1.store_matchs_round(match3.list_data_match())
round_1.store_matchs_round(match4.list_data_match())

round_1.show_matchs_round()


tournoi.store_rounds_tournament(round_1.list_data_round()) 
tournoi.show_rounds_tournament()

"""Ordinateur génère des paires selon le modèle Suisse, Tour2."""
round_1.create_new_list_scores()
round_1.add_scores_matchs_round()
round_1.build_values_dict_match()
round_1.build_list_dict_matchs()



tournoi.total_score_dict_players(round_1.build_list_dict_matchs())

tournoi.sorted_score_list()
tournoi.create_pairs_players_next()


"""Tour 2."""
round_2 = Round(tournoi.round[1], tournoi.create_pairs_players_next())
round_2.get_matches()
round_2.create_round()

match1 = Match(round_2.name_round, round_2.match[0], tournoi.create_pairs_players_next()[0])
match1.create_match()

match2 = Match(round_2.name_round, round_2.match[1], tournoi.create_pairs_players_next()[1])
match2.create_match()

match3 = Match(round_2.name_round, round_2.match[2], tournoi.create_pairs_players_next()[2])
match3.create_match()

match4 = Match(round_2.name_round, round_2.match[3], tournoi.create_pairs_players_next()[3])
match4.create_match()

round_2.start_round()
round_2.end_round()

match1.enter_score_match()
match1.show_data_match()

match2.enter_score_match()
match2.show_data_match()

match3.enter_score_match()
match3.show_data_match()

match4.enter_score_match()
match4.show_data_match()

round_2.create_new_list_matchs()
round_2.store_matchs_round(match1.list_data_match())
round_2.store_matchs_round(match2.list_data_match())
round_2.store_matchs_round(match3.list_data_match())
round_2.store_matchs_round(match4.list_data_match())

round_2.show_matchs_round()


tournoi.store_rounds_tournament(round_2.list_data_round()) 
tournoi.show_rounds_tournament()




"""Ordinateur génère des paires selon le modèle Suisse, Tour3."""

round_2.create_new_list_scores()
round_2.add_scores_matchs_round()
round_2.build_values_dict_match()



tournoi.total_score_dict_players(round_2.build_list_dict_matchs())
tournoi.sorted_score_list()

tournoi.create_pairs_players_next()




"Tour 3."

round_3 = Round(tournoi.round[2], tournoi.create_pairs_players_next())
round_3.get_matches()
round_3.create_round()

match1 = Match(round_3.name_round, round_2.match[0], tournoi.create_pairs_players_next()[0])
match1.create_match()

match2 = Match(round_3.name_round, round_2.match[1], tournoi.create_pairs_players_next()[1])
match2.create_match()

match3 = Match(round_3.name_round, round_2.match[2], tournoi.create_pairs_players_next()[2])
match3.create_match()

match4 = Match(round_3.name_round, round_2.match[3], tournoi.create_pairs_players_next()[3])
match4.create_match()

round_3.start_round()
round_3.end_round()

match1.enter_score_match()
match1.show_data_match()

match2.enter_score_match()
match2.show_data_match()

match3.enter_score_match()
match3.show_data_match()

match4.enter_score_match()
match4.show_data_match()

round_3.create_new_list_matchs()
round_3.store_matchs_round(match1.list_data_match())
round_3.store_matchs_round(match2.list_data_match())
round_3.store_matchs_round(match3.list_data_match())
round_3.store_matchs_round(match4.list_data_match())

round_3.show_matchs_round()

tournoi.store_rounds_tournament(round_3.list_data_round()) 
tournoi.show_rounds_tournament()

"""Ordinateur génère des paires selon le modèle Suisse, Tour4."""
round_3.create_new_list_scores()
round_3.add_scores_matchs_round()
round_3.build_values_dict_match()

tournoi.total_score_dict_players(round_3.build_list_dict_matchs())
tournoi.sorted_score_list()
tournoi.create_pairs_players_next()

"Tour 4."

round_4 = Round(tournoi.round[3], tournoi.create_pairs_players_next())
round_4.get_matches()
round_4.create_round()

match1 = Match(round_4.name_round, round_2.match[0], tournoi.create_pairs_players_next()[0])
match1.create_match()

match2 = Match(round_4.name_round, round_2.match[1], tournoi.create_pairs_players_next()[1])
match2.create_match()

match3 = Match(round_4.name_round, round_2.match[2], tournoi.create_pairs_players_next()[2])
match3.create_match()

match4 = Match(round_4.name_round, round_2.match[3], tournoi.create_pairs_players_next()[3])
match4.create_match()

round_4.start_round()
round_4.end_round()

match1.enter_score_match()
match1.show_data_match()

match2.enter_score_match()
match2.show_data_match()

match3.enter_score_match()
match3.show_data_match()

match4.enter_score_match()
match4.show_data_match()

round_4.create_new_list_matchs()
round_4.store_matchs_round(match1.list_data_match())
round_4.store_matchs_round(match2.list_data_match())
round_4.store_matchs_round(match3.list_data_match())
round_4.store_matchs_round(match4.list_data_match())

round_4.show_matchs_round()

tournoi.store_rounds_tournament(round_4.list_data_round()) 
tournoi.show_rounds_tournament()

round_4.create_new_list_scores()
round_4.add_scores_matchs_round()
round_4.build_values_dict_match()

tournoi.total_score_dict_players(round_4.build_list_dict_matchs())

"""fin"""