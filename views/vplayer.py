"""View player"""



def prompt_for_manager(self):
        """prompt for tout ça!."""        
        
        """Prompt for the player's family_name"""
        lastname = input("Saisir le nom de famille du joueur: ")
        if not lastname:
            print("Le Nom de famille est obligatoire")
        lastname = input("Saisir le nom de famille du joueur: ")
        
        return lastname
   
        """Prompt for the player's firstname"""
        firstname = input("saisir le prénom du joueur: ")
        if not firstname:
            return print("Le prénom du joueur est obligatoire")
        firstname = input("saisir le prénom du joueur: ")
        return firstname
       
        """Prompt for the player's birthdate"""
        birthdate = input("saisir la de naissance du joueur: ")
        if not birthdate:
            return print("la date de naissance est obligatoire")
        birthdate = input("saisir la de naissance du joueur: ")   
        
        return birthdate

        """Prompt for the player's gender"""
        print("genres : H (homme), F(femme), T(trans)")
        gender = input("saisir le genre du joueur (choix ci_dessus): ")
        if not gender:
            return print("Le genre du joueur est obligatoire")
        gender = input("saisir le genre du joueur (choix ci_dessus): ")    
        
        return gender        

        """Prompt for the player's ranking"""
        ranking = input("saisir le classement du joueur: ")
        if not ranking:
            return 0
        
        return ranking