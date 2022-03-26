"""Déroulement de base du tournoi."""




from views.view import ViewMenu, ViewTournament, ViewPlayer
from controllers.controller import MainMenus, ControlTournament, ControlPlayer


def main():
    
    """Ouverture de l'application"""
    view = ViewMenu()
    menu = MainMenus(view)
    menu.openmainscreen() #écran niveau 1 : Accueil
    


  
   
main()


   




