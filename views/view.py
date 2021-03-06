"""View
Vues de toutes les choix proposées dans l'application.
"""


class ViewMenu:

    def homemenu(self):
        """Affiche les actions disponibles en première interface, niveau principal"""
        return input(
            " \n"
            "Bienvenue sur GTE, Gestionnaire de Tournoi d'Echec \n\n"
            "\033[4m Vous souhaitez \033[0m: \n\n"
            "1/ Gérer le jeu : Taper \033[1m 1 \033[0m \n"
            "\n"
            "2/ Gérer un joueur : Taper \033[1m 2 \033[0m \n"
            "\n"
            "3/ Gérer un participant: Taper \033[1m 3 \033[0m \n"
            "\n"
            "4/ Editer des rapports : Taper \033[1m 4 \033[0m \n"
            "\n"
            "5/ Quitter l'application : Taper \033[1m Q \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
        )

    def gamemenu(self):
        """Affiche les actions disponibles si choix 1(tournoi) est sélectionné au niveau principal."""
        return input(
            "\n"
            "\033[1m Menu du Jeu \033[0m: \n\n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"
            "\033[4m Gérer un tournoi \033[0m: \n"
            "\n"
            "1/ Reprendre un tournoi suspendu : Taper \033[1m 1 \033[0m \n"
            "\n"
            "2/ Préparer un nouveau tournoi : Taper \033[1m 2 \033[0m \n"
            "\n"
            "3/ Inscrire les participants au tournoi : Taper \033[1m 3 \033[0m \n"
            "\n"
            "4/ Démarrer le tournoi : Taper \033[1m 4 \033[0m \n"
            "\n"
            "5/ Ajouter un commentaire sur un tournoi : Taper \033[1m 5 \033[0m \n"
            "\n"
            "6/ Afficher les commentaires d'un tournoi choisi : Taper \033[1m 6 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
        )

    def personmenu(self):
        """Affiche les actions disponibles si choix 2 (joueur) est sélectionné au niveau principal."""
        #  voir si choix d'un menu multiple nécessaire
        return input(
            "\n"
            "\033[1m Menu du Joueur \033[0m: \n\n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"
            "\033[4m Gérer un joueur \033[0m: \n"
            "\n"
            "1/ Rechercher un joueur : Taper \033[1m 1 \033[0m \n"
            "\n"
            "2/ Enregistrer un joueur : Taper \033[1m 2 \033[0m \n"
            "\n"
            "3/ Supprimer un joueur : Taper \033[1m 3 \033[0m \n"
            "\n"
            "4/ Modifier les données d'un joueur : Taper \033[1m 4 \033[0m \n"
            "\n"
            "5/ Mettre à jour le rang un joueur : Taper \033[1m 5 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
            )

    def participant_view(self):
        """Affiche les actions disponibles si choix 3(participant) est sélectionné au niveau principal."""
        return input(
            "\n"
            "\033[1m Menu du Participant \033[0m: \n\n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"
            "\033[4m Gérer un participant \033[0m: \n"
            "\n"
            "1/ Supprimer un participant du tournoi: Taper \033[1m 1 \033[0m \n"
            "\n"
            "2/ Modifier le rang en cours de tournoi, d'un participant inscrit : Taper \033[1m 2 \033[0m \n"
            ""
            "\n"
            "\033[4m Taper votre choix \033[0m: "
            )

    def report_view(self):
        """Affiche les actions disponibles si choix 4(rapport) est sélectionné au niveau principal."""
        return input(
            "\n"
            "\033[1m Menu des rapports \033[0m: \n\n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"
            "\033[4m Sélectionner votre rapport \033[0m: \n"
            "\n"
            "1/ Liste de tous les joueurs par ordre alphabétique: Taper \033[1m 1 \033[0m \n"
            "\n"
            "2/ Liste de tous les joueurs par classement: Taper \033[1m 2 \033[0m \n"
            "\n"
            "3/ Liste de tous les participants d'un tournoi par ordre alphabétique: Taper \033[1m 3 \033[0m \n"
            "\n"
            "4/ Liste de tous les participants d'un tournoi par classement : Taper \033[1m 4 \033[0m \n"
            "\n"
            "5/ Liste de tous les tournois : Taper \033[1m 5 \033[0m \n"
            "\n"
            "6/ Liste de tous les tours d'un tournoi: Taper \033[1m 6 \033[0m \n"
            "\n"
            "7/ Liste de tous les matchs d'un tournoi : Taper \033[1m 7 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
            )


class ViewTournament:
    """Affiche les différents 'inputs' nécessaire à la gestion de données sur un tournoi."""

    def start_tournament_view(self):
        """Affiche un choix pour démarrer un tournoi ou abandonné."""
        return input("\n \033[4m Souhaitez_vous réellement démarrer un tournoi ? (O/N) \033[0m")

    def tournament_view(self):
        """Annonce la saisie des données du Tournoi."""
        print("\033[4m Création d'un nouveau tournoi \033[0m")

    def prompt_name_tournament_view(self):
        return input("\n Nom du Tournoi : ")

    def prompt_place_tournament_view(self):
        return input("Nom de la Ville: ")

    def prompt_controller_time_view(self):
        return input(
            "Choix des règles de temps :\n"
            "Bullet: Taper \033[1m 1 \033[0m \n" "Blitz: Taper \033[1m 2 \033[0m \n" "ou " "Coup rapide : Taper \033[1m 3 \033[0m \n"
            "\033[4m Taper votre choix \033[0m:"
            )

    def search_name_tournament_view(self):
        """Affiche le type de recherche sur le tournoi."""
        print("\n \033[4m Recherche du tournoi par son nom' \033[0m \n")

    def prompt_next_participant_view(self):
        """Annonce un choix entre continuer à intéger un participant."""
        return input("\n Souhaitez-vous ajouter un autre participant au tournoi (O/N): ")

    def None_tournament(self):
        """Affiche l'absence dans les données du tournoi recherché. """
        print("\n \033[4m Le tournoi recherché n'existe pas dans la base' \033[0m : Veuillez vérifier votre saisie et recommencer. \n\n")

    def add_comment_view(self):
        """Annonce la saisie d'un commentaire"""
        return input("Veuillez saisir votre commentaire:\n. (Appuyer sur 'entrée' quand vous avez fini.)\n")

    def truncate_tournaments_table_view(self):
        """Message de vigilance avant suppression de la table 'Tournaments' dans sa totalité."""
        return input(
            "\n------------ATTENTION------------\n"
            "\n \033[4m Si vous continuez, la table 'tournaments_table' sera définitevement effacée.\033[0m \n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "----------------------------------- \n"
            "\n\n Pour continuer : Taper 'O'\033[0m \n\n"
            "Votre choix: "
        )


class ViewRound:
    """Affiche les différents 'inputs' ou annonces nécessaires à la gestion de données sur un round."""

    def create_rounds_view(self):
        """Annonce la création des éléments des rounds du tournoi sélectionné à venir."""
        print("\n...Création des rounds à venir....")

    def round1_view(self):
        """Annonce les éléments du round1 à venir."""
        print("\n \033[4m Données du Round 1 à venir: \033[0m \n")

    def prompt_name_round_view(self):
        return input("\n Nom du tour à créer : ")

    def end_play_round_view(self):
        """Demande confirmation de finir le jeu du round."""
        return input(
            "Souhaitez-vous réellement arrêter le jeu ?\n"
            " Si les matchs sont terminés  : Taper \033[1m O \033[0m\n"
            "....sinon patientez jusqu'à la fin des matchs....\n"
            "\nPour continuer : Taper \033[1m O \033[0m\n"
            )

    def truncate_rounds_table_view(self):
        """Message de vigilance avant suppression de la table 'Rounds' dans sa totalité."""
        return input(
            "\n------------ATTENTION------------\n"
            "\n\n \033[4m Si vous continuez, la table 'rounds_table' sera définitevement effacée.\033[0m \n\n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m"
            "\n ----------------------------------- \n"
            "\nPour continuer : Taper 'O'\033[0m \n\n"
            "Votre choix: "
        )


class ViewMatch:
    """Affiche les différents 'inputs' ou annonces nécessaires à la gestion de données sur un match."""

    def pairs_players_matchs_view(self):
        """Message qui annonce les paires qui vont s'affronter pour les matchs d'un round donné."""
        print("\n \033[4m Noms des joueurs qui vont s'affronter par match:\033[0m \n")

    def score_entry_view(self):
        print("\n\033[1m Veuillez entrer les scores des matches joués : \033[0m\n")

    def truncate_matchs_table_view(self):
        """Message de vigilance avant suppression de la table 'Matchs' dans sa totalité."""
        return input(
            "\n------------ATTENTION------------\n"
            "\n\n \033[4m Si vous continuez, la table 'matchs_table' sera définitevement effacée.\033[0m \n\n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m"
            "\n ----------------------------------- \n"
            "\n Pour continuer : Taper 'O'\033[0m \n\n"
            "Votre choix: "
        )


class ViewParticipant:
    """Affiche les différents 'inputs' nécessaires à la gestion d'un participant."""

    def add_participant_view(self):
        """Choix pour intégrer le participant dans la liste des joueurs du tournoi."""
        return input("\n Confirmer l'intégration du participant recherché (O/N) :")

    def delete_participant_view(self):
        """Choix de suppression d'un participant à confirmer."""
        return input(
            "\n Pour supprimer le participant souhaité : \n"
            "Taper son numéro affiché ci_dessus, avant ses informations \n"
            "\n"
            "\033[4m Taper le numéro choisi: \033[0m: "
            )

    def modify_ranking_participant_view(self):
        """Affiche l'action"""
        print("\n \033[4m Modification du rang du participant dans dans la liste des joueurs \033[0m \n")

    def select_participant_view(self):
        """Choix du participant à sélectionner."""
        return input(
            "\n Pour choisir le participant souhaité : \n"
            "Taper son numéro affiché ci_dessus, devant ses informations \n"
            "\n"
            "\033[4m Taper le numéro choisi: \033[0m: "
            )

    def new_ranking_participant_view(self):
        """Invite à saisir le nouveau rang du participant."""
        return input("Saisir le nouveau classement du participant :")


class ViewPlayer:
    """Affiche les différents 'inputs' nécessaires à la gestion de données sur un joueur."""

    def search_player_view(self):
        """Affiche le type de recherche."""
        print("\n \033[4m Recherche d'un joueur par nom et prénom: \033[0m")

    def add_player_view(self):
        """Annonce la saisie pour créer un joueur."""
        print("\033[4m Création d'un nouveau joueur \033[0m")

    def prompt_add_player_view(self):
        """Affiche le choix de continuer la création du joueur recherché."""
        return input("\n Souhaitez-vous créer le joueur (O/N) :")

    def prompt_lastname_view(self):
        return input("\nSaisir le nom de famille du joueur: ")

    def prompt_firstname_view(self):
        return input("Saisir le prénom du joueur: ")

    def prompt_birthdate_view(self):
        return input("Saisir la date de naissance du joueur(jj/mm/aaaa): ")

    def prompt_gender_view(self):
        return input(
            "Saisir le genre du joueur : \n"
            "genres : H(homme), F(femme), T(trans) : "
            )

    def prompt_ranking_view(self):
        return input("Saisir le classement du joueur: ")

    def prompt_next_add_player(self):
        """Annonce un choix entre continuer à créer un joueur."""
        return input("\n Souhaitez-vous ajouter un autre joueur (O/N): ")

    def delete_player_view(self):
        """Choix de suppression à confirmer."""
        return input(
            "Souhaitez_vous vraiment supprimer les données d'un joueur \n"
            "car une fois supprimer vous ne pourrez plus récupérer les informations \n"
            "\n"
            "\033[4m Taper votre choix(O/N): \033[0m: "
            )

    def truncate_players_table_view(self):
        """Message de vigilance avant suppression de la table player dans sa totalité."""
        return input(
            "\n------------ATTENTION------------\n"
            "\n \033[4m Si vous continuez, la table 'players_table' sera définitevement effacée.\033[0m \n"
            "----------------------------------- \n"
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "----------------------------------- \n"
            "\n\n Pour continuer : Taper 'O'\033[0m \n\n"
            "Votre choix: "
            )

    def modify_data_player_view(self):
        """EN CONSTRUCTION : Choix pour modifier soit le nom, prénom, date de naissance ou genre du joueur."""
        return input(
            "\n"
            "\033[1m Modifier les données d'un joueur \033[0m: \n\n"
            "----------------------------------- \n"
            "\n\n \033[1m En construction, A bientôt\033[0m \n\n"
            "----------------------------------- \n"
            "Taper sur 'entrée' pour continuer"
            )

    def modify_ranking_player_view(self):
        """Affiche l'action"""
        print("\n \033[4m Modification du rang du joueur dans la base de données \033[0m \n")

    def new_ranking_player_view(self):
        """Invite à saisir le nouveau rang du joueur."""
        return input("Saisir le nouveau classement du joueur :")
