"""Déroulement de base du tournoi."""

from views.view import ViewMenu, ViewTournament
from controllers.controller import MainMenus, ControlTournament

def main():
    
    """Ouverture de l'application"""
    view = ViewMenu()
    menu = MainMenus(view)
    menu.openmainscreen() #écran niveau 1 : Accueil
    


  
   
main()


   




