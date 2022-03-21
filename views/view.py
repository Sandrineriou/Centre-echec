"""Fonctions en lien avec les différents menus proposés par le controller"""
import datetime


class ViewMenu :


    def homemenu():
        return input(
            " \n"
            "Bienvenue sur GTE, Gestionnaire de Tournoi d'Echec \n\n"
            "\033[4m Vous souhaitez \033[0m: \n\n"
            "1/ Gérer le jeu : Taper \033[1m 1 \033[0m \n"
            "\n"
            "2/ Gérer un joueur : Taper \033[1m 2 \033[0m \n"
            "\n"
            "3/ Mise à jour classement joueur : Taper \033[1m 3 \033[0m \n"
            "\n"
            "4/ Editer des rapports : Taper \033[1m 4 \033[0m \n"
            "\n"
            "5/ Quitter l'application : Taper \033[1m Q \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
           
        )

    def gamemenu():
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
            "3/ Ajouter un commentaire sur un tournoi : Taper \033[1m 3 \033[0m \n"
            "\n"
            "\033[4m Taper votre choix \033[0m: "
        )
    
    def playermenu():
        #voir si choix d'un menu multiple nécessaire 
        input(
            "\n"
            "\033[1m Menu du Joueur \033[0m: \n\n"
            "----------------------------------- \n" 
            "Revenir au menu précédent : Taper \033[1m R \033[0m \n"
            "Quitter l'application : Taper \033[1m Q \033[0m \n"
            "----------------------------------- \n"  
            "\033[4m Gérer un joueur \033[0m: \n"
            "1/ Rechercher un joueur et affiche ses données : Taper \033[1m 1 \033[0m \n"
            "2/ Créer un joueur : ")
        pass
        
    
    def update_ranking_view(self):
        pass

    def report_view(self):
        pass

class ViewTournament:

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
    
    def player_view(self):
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
       
    