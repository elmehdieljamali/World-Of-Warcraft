import random
from Objet import Objet
from Arme import Arme
from Bouclier import Bouclier
from Nourriture import Nourriture


class Personnage:
    def __init__(self, nom, points_de_vie, endurance, arme=None, bouclier=None):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.endurance = endurance
        self.arme = arme
        self.bouclier = bouclier
        self.inventaire = []

    def attaquer(self, cible):
        if self.arme and self.endurance >= self.arme.endurance_reduction:
            self.endurance -= self.arme.endurance_reduction
            print(f"{self.nom} ({self.points_de_vie} PV) a attaquer {cible.nom} avec {self.arme.nom} ({self.arme.degats} DP). ({self.endurance} ST)")
            cible.recevoir_degats(self.arme.degats)
            
    
    def defendre(self):
        if self.endurance >= self.bouclier.endurance_reduction:
            self.endurance -= self.bouclier.endurance_reduction
            print(f"{self.nom} utilise son bouclier et a maintenant {self.endurance} ST")  
        else:
            print(f"{self.nom} n'a pas de bouclier pour se défendre.")   

    def manger(self, nourriture):
        if nourriture in self.inventaire:
            self.endurance = min(self.endurance + nourriture.endurance_restoration, 100)
            self.inventaire.remove(nourriture)
        else:
            print(f"{self.nom} n'a pas {nourriture.nom} dans son inventaire.")

    def recevoir_degats(self, degats):
        if self.bouclier:
            self.defendre()
            dammage = degats - self.bouclier.defense
            if dammage < 0:
                dammage = 0
            self.points_de_vie -= dammage
        else:
            self.points_de_vie -= degats
        if self.points_de_vie <= 0:
            print(f"{self.nom} a ete terasser et rejoint le cimetière!")
            print("\n")
        else:
            print(f"{self.nom} a maintenant {self.points_de_vie} points de vie.")
            print("\n")

    def remplir_inventaire(self, armes_disponibles, boucliers_disponibles, nourritures_disponibles):
        # Ajouter des armes au hasard, jusqu'à la taille de la liste des armes disponibles
        nombre_armes = random.randint(1, len(armes_disponibles))
        for _ in range(nombre_armes):
            self.inventaire.append(random.choice(armes_disponibles))

        # Ajouter des boucliers au hasard, jusqu'à la taille de la liste des boucliers disponibles
        nombre_boucliers = random.randint(0, len(boucliers_disponibles))
        for _ in range(nombre_boucliers):
            self.inventaire.append(random.choice(boucliers_disponibles))

        # Ajouter de la nourriture au hasard, jusqu'à la taille de la liste des nourritures disponibles
        nombre_nourritures = random.randint(0, len(nourritures_disponibles))
        for _ in range(nombre_nourritures):
            self.inventaire.append(random.choice(nourritures_disponibles))