from Arme import Arme, Epee, Gourdin

class Personnage:
    def __init__(self, nom, points_de_vie, arme):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.arme = arme


    def attaquer(self, cible):
        if self.arme:
            print(f"{self.nom} ({self.points_de_vie} PV) attaque {cible.nom} avec {self.arme.nom} ({self.arme.degats} DP).")
            cible.recevoir_degats(self.arme.degats)
        

    def recevoir_degats(self, degats):
        
        self.points_de_vie -= degats
        if self.points_de_vie <= 0:
            print(f"{self.nom} a ete terasser et rejoint le cimetière!")
            print("\n")
        else:
            print(f"{self.nom} a maintenant {self.points_de_vie} points de vie.")
            print("\n")

class Hero(Personnage):
    pass

class Monstre(Personnage):
    pass