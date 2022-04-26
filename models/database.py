"""Base de données Tinydb  -  Gestion des données."""


from pprint import pprint
from tinydb import TinyDB, Query, where


from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match




db = TinyDB('db.json')
players_table = db.table('players')
tournaments_table = db.table('tournaments')
rounds_table = db.table('rounds')
matchs_table = db.table('matchs')


class DataPlayer:
    """Classe qui gère les opérations de la base en lien avec le joueur :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un joueur.
    """
    db = TinyDB('db.json')
    players_table = db.table('players')
    
    
    def saving_data_player(self):
        """Sauvegarde les instances créées du joueur dans la base tinydb."""
        players_table.insert(self.player_serialized)
    
    def search_player(self):
        """Affiche le joueur de la base portant le nom et prénom saisie"""
        return players_table.search((where('lastname') == self.lastname)and(where('firstname') == self.firstname))
    
    def get_id_player(self):
        """Retourne le numéro d'identifiant du joueur rehcerché."""
       
        
        for element in DataPlayer.search_player(self):
            self.num_id = element.doc_id
            return self.num_id
        

    def search_lastname_player(self):
        """Affiche les joueurs de la base portant le nom saisie."""
        return players_table.search(where('lastname') == self.lastname)

    
    def search_all_players(self):
        """Affiche tous les joueurs de la base."""
        print('\n'f"Il y a {len(players_table)} joueurs incrits dans la base."'\n')
        self.all = players_table.all()
        return self.all
        

    def sorted_all_players_alpha(self):
        """Affiche tous les joueurs de la base par ordre alphabétique(nom)"""
        self.alpha_sorted = sorted(self.all, key=lambda x: x['lastname'])
        for element in self.alpha_sorted:
            print("Joueur: ID "f'{element.doc_id}', element['lastname'], element['firstname'],"Né le :" , element['birthdate'],
                element['gender'], "classement: ", element['ranking']
            )

    def delete_player(self):
        """Supprime 1 joueur recherché"""
        User = Query()
        return players_table.remove((User.lastname == self.lastname) and (User.firstname == self.firstname))

    def truncate_players_table(self):
        """Efface toutes les données de la table 'Player(mise à zéro)."""
        return players_table.truncate()
    
    def update_ranking_player(self):# modifier pour mettre l'ID en recherche plutot que le nom ou sinon rajouter le prénom
        
        return players_table.update({'ranking':self.new_ranking}, doc_ids=[DataPlayer.get_id_player(self)])


class DataTournament:
    """Classe qui gère les opérations de la base en lien avec le tournoi :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un tournoi.
    """    
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')

    def saving_data_tournament(self):
        """Sauvegarde les instances créées dans la base tinydb."""
        tournaments_table.insert(self.tournament_serialized)
 
    def search_all_tournaments(self):
        """Affiche tous les tournois inscrits dans la base."""
        print('\n'f"Il y a {len(tournaments_table)} tournois incrits dans la base."'\n')
        self.all = tournaments_table.all()
        return self.all
    
    def search_by_name_tournament(self):
        """Affiche les informations en lien avec le nom du tournoi."""
        return tournaments_table.search(where("Nom_tournoi") == self.name_tournament)

    def search_rounds_tournamant(self):
        pass

    def update_data_rounds_tournament(self):
        """Met à jour le contenu de l'attibut 'détails-tours'de tournament."""
        User = Query()
        return (tournaments_table.update({'Detail_tours': self.rounds_tournament}, User.Nom_tournoi == self.name_tournament))

    def update_players_list_tournament(self):
        User = Query()
        print(tournaments_table.update({'Liste_joueurs': self.players_list}, User.Nom_tournoi == self.name_tournament))
    
    def truncate_tournaments_table(self):
        """Efface toutes les données de la table 'Tournaments'(mise à zéro)."""
        return tournaments_table.truncate()


class DataRound:
    """Classe qui gère les opérations de la base en lien avec un round d'un tournoi :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un round.
    """
    db = TinyDB('db.json')
    rounds_table = db.table('rounds')

    def saving_data_round(self):
        """Sauvegarde les instances créées dans la base tinydb."""
        rounds_table.insert(self.round_serialized)

    def search_by_nametournament_round(self):
        return rounds_table.search(where("Nom_tournoi") == self.name_tournament)

    def search_specific_round(self):
        User = Query()
        return rounds_table.search((User.Nom_tournoi == self.name_tournament) and (User.Nom_Round == self.name_round))
    
    def update_pairs_players_round(self):
        """Met à jour la liste des paires de participants dans un round donné."""
        User = Query()
        return rounds_table.update({'Round_paires': self.pairs_players}, ((User.Nom_tournoi == self.name_tournament) and (User.Round_nom == self.name_round)))
    
    def update_start_round(self):
        """Met à jour la date et heure de démarrage du round concerné."""
        User = Query()
        return rounds_table.update({'Round_debut': self.startdatetime}, ((User.Nom_tournoi == self.name_tournament) and (User.Round_nom == self.name_round)))

    def update_end_round(self):
        """Met à jour la date et l'heure de l'arrêt de jeu du round concerné."""
        User = Query()
        return rounds_table.update({'Round_fin': self.enddatetime}, ((User.Nom_tournoi == self.name_tournament) and (User.Round_nom == self.name_round)))

    def update_matchs_round(self):
        """Met à jour l'attribut 'Round_matches' après un tour de jeu."""
        User = Query()
        return rounds_table.update({'Round_matches': self.matchs_round}, ((User.Nom_tournoi == self.name_tournament) and (User.Round_nom == self.name_round)))

    def truncate_rounds_table(self):
        """Efface toutes les données de la table 'Rounds'(mise à zéro)."""
        return rounds_table.truncate()


class DataMatch:
    """Classe qui gère les opérations de la base en lien avec un match d'un round d'un tournoi :
    toutes requêtes nécessaires et disponibles pour 
    créer, éditer, modifier, supprimer
    les données d'un match.
    """

    db = TinyDB('db.json')
    matchs_table = db.table('matchs')

    def saving_data_match(self):
        """Sauvegarde les instances créées dans la base tinydb."""
        matchs_table.insert(self.match_serialized)
    
    def search_by_nametournament_matchs(self):
        return matchs_table.search(where("Nom_Tournoi") == self.name_tournament)

    def search_match(self):
        User = Query()
        return matchs_table.search((User.Nom_tournoi == self.name_tournament) and (User.Nom_Round == self.name_round) and (User.Match_nom == self.name_match))
        
        
    
    def search_all_matchs(self):
        """Affiche tous les matchs inscrits dans la base."""
        print('\n'f"Il y a {len(matchs_table)} matchs incrits dans la base.")
    
    def update_pair_players_match(self):
        """Met à jour la paire de joueur pour un match donné."""
        User = Query()
        return matchs_table.update(
            {'Match_participants': self.pair_players},
            ((User.Nom_tournoi == self.name_tournament) and (User.Nom_Round == self.name_round) and (User.Match_nom == self.name_match))
        )
       
    def update_data_match(self):
        """Met à jour les scores du match donné."""
        User = Query()
        return matchs_table.update({'Match_resultats': tuple(self.data_match)},
         ((User.Nom_tournoi == self.name_tournament) and (User.Nom_Round == self.name_round) and (User.Match_nom == self.name_match))
         )

    def truncate_matchs_table(self):
        """Efface toutes les données de la table 'Matchs'(mise à zéro)."""
        return matchs_table.truncate()