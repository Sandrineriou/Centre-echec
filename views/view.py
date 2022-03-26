"""View 
Vues de toutes les choix proposées dans l'application.
"""



class ViewMenu :


    def homemenu():
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

    def gamemenu():
        """Affiche les actions disponibles si choix 1(tournoi) est sélectionné au niveau principal."""
        return input(
            "\n"
            "\033[1m Menu du Jeu \033[0m: \n\n"
            "----------------------------------- \n" 
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"  
            "\033[4m Gérer un tournoi \033[0m: \n"
            "1/ Reprendre un tournoi suspendu : Taper \033[1m 1 \033[0m \n"
            "2/ Créer un tournoi : Taper \033[1m 2 \033[0m \n"
            "3/ Inscrire les joueurs au tournoi : Taper \033[1m 3 \033[0m \n"
            "4/ Démarrer le tournoi : Taper \033[1m 3 \033[0m \n"
            "5/ Ajouter un commentaire sur un tournoi : Taper \033[1m 5 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
        )
    
    def personmenu():
        """Affiche les actions disponibles si choix 2 (joueur) est sélectionné au niveau principal."""
        #voir si choix d'un menu multiple nécessaire 
        return input(
            "\n"
            "\033[1m Menu du Joueur \033[0m: \n\n"
            "----------------------------------- \n" 
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"  
            "\033[4m Gérer un joueur \033[0m: \n"
            "1/ Rechercher un joueur : Taper \033[1m 1 \033[0m \n"
            "2/ Créer un joueur : Taper \033[1m 2 \033[0m \n"
            "3/ Supprimer un joueur : Taper \033[1m 3 \033[0m \n"
            "4/ Modifier les données d'un joueur : Taper \033[1m 4 \033[0m \n"
            "5/ Mettre à jour le rang un joueur : Taper \033[1m 5 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
            )
        
 
    def update_ranking_view():
        pass

    def report_view():
        """Affiche les actions disponibles si choix 4(rapport) est sélectionné au niveau principal."""
        return input(
            "\n"
            "\033[1m Menu des rapports \033[0m: \n\n"
            "----------------------------------- \n" 
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"  
            "\033[4m Sélectionner votre rapport \033[0m: \n"
            "1/ Liste de tous les joueurs par ordre alphabétique: Taper \033[1m 1 \033[0m \n"
            "2/ Liste de tous les joueurs par classement: Taper \033[1m 2 \033[0m \n"
            "3/ Liste de tous les participants d'un tournoi par ordre alphabétique: Taper \033[1m 3 \033[0m \n"
            "4/ Liste de tous les participants d'un tournoi par classement : Taper \033[1m 4 \033[0m \n"
            "5/ Liste de tous les tournois : Taper \033[1m 5 \033[0m \n"
            "6/ Liste de tous les tours d'un tournoi: Taper \033[1m 6 \033[0m \n"
            "7/ Liste de tous les matchs d'un tournoi : Taper \033[1m 7 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
            )

class ViewTournament:
    """Affiche les différents 'inputs' nécessaire à la gestion de données sur un tournoi."""

    def tournament_view(self):
        """Annonce la saisie des données du Tournoi."""
        
        print("\033[4m Création d'un nouveau tournoi \033[0m")
        
    def prompt_name_tournament_view(self):
        return input("Nom du Tournoi : ")
        
    def prompt_place_tournament_view(self):
        return input("Nom de la Ville: ")
        
   
    def prompt_controller_time_view(self):
        return input(
        "Choix des règles de temps :\n" 
        "Bullet: Taper \033[1m 1 \033[0m \n" "Blitz: Taper \033[1m 2 \033[0m \n" "ou " "Coup rapide : Taper \033[1m 3 \033[0m \n"
        "\033[4m Taper votre choix \033[0m: "
        )
        
class ViewPlayer:
    """Affiche les différents 'inputs' nécessaire à la gestion de données sur un joueur."""
    
    def search_player_view(self):
        """Affiche le type de recherche."""
        print("\n \033[4m Recherche d'un joueur par ses nom et prénom' \033[0m \n")
    
    def add_player_view(self):
        """Annonce la saisie pour créer un joueur."""
        
        print("\033[4m Création d'un nouveau joueur \033[0m")
    
    def prompt_lastname_view(self):
        return input("Saisir le nom de famille du joueur: ")
 
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
        return input("Souhaitez-vous ajouter un autre joueur (O/N): ")

    def delete_player_view(self):
        """Choix de suppression à confirmer."""
        return input(
            "Souhaitez_vous vraiment supprimer les données d'un joueur \n"
            "car une fois supprimer vous ne pourrez plus récupérer les informations \n"
            "\n"
            "\033[4m Taper votre choix(O/N): \033[0m: "
            )
    def modify_data_player_view(self):
        """Choix pour modifier soit le nom, prénom, date de naissance ou genre du joueur."""
        return input(
             "\n"
            "\033[1m Modifier les données d'un joueur \033[0m: \n\n"
            "----------------------------------- \n" 
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "----------------------------------- \n" 
            "\n\n \033[1m En construction, A bientôt\033[0m \n\n"
            "Taper R"
            )
    def modify_ranking_player_view(self):
        """Affiche l'action"""
        print("\n \033[4m Modification du rang \033[0m \n")

    def new_ranking_player_view(self):
        return input("\n Saisir le nouveau classement du joueur :")


class ViewReport:
    """Affiche les différents 'inputs' nécessaire à la gestion de données pour afficher les reports."""
    
  