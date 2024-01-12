
import random
from Objet import Objet
from Arme import Arme
from Bouclier import Bouclier
from Nourriture import Nourriture

class PersonnageFactory:
    @staticmethod
    def create_personnage(nom, points_de_vie, endurance, force, x, y, arme=None, bouclier=None):
        return Personnage(nom, points_de_vie, endurance, force, x, y, arme, bouclier)

class Personnage:
    def __init__(self, nom, points_de_vie, endurance, force, x, y, arme=None, bouclier=None):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.max_points_de_vie = points_de_vie
        self.endurance = endurance
        self.max_endurance = endurance
        self.force = force
        self.x = x
        self.y = y
        self.arme = arme
        self.bouclier = bouclier
        self.inventaire = []

    def attaquer(self, cible):
        if self.arme and self.endurance > 0:
            cout_endurance = (self.arme.longeur * self.arme.poids) / (1000 * self.force)
            if self.endurance >= cout_endurance:
                self.endurance -= cout_endurance
                degats_effectifs = self.arme.degats + (self.force / 10)
                print(f"{self.nom} attaque {cible.nom} causant {degats_effectifs} de dégâts. Endurance restante : {self.endurance}")
                cible.recevoir_degats(degats_effectifs)
            else:
                print(f"{self.nom} est trop fatigué pour attaquer.")
        else:
            print(f"{self.nom} ne peut pas attaquer sans arme ou sans endurance.")

    
    def defendre(self):
        if self.bouclier and self.endurance > 0:
            cout_endurance = self.bouclier.poids / (100 * self.force)
            if self.endurance >= cout_endurance:
                self.endurance -= cout_endurance
                print(f"{self.nom} utilise son bouclier. Endurance restante : {self.endurance}")
            else:
                print(f"{self.nom} est trop fatigué pour se défendre.")
        else:
            print(f"{self.nom} ne peut pas se défendre sans bouclier ou sans endurance.")

    def manger(self, nourriture):
        if nourriture in self.inventaire:
            self.endurance = min(self.endurance + nourriture.endurance_restoration, 100)
            self.inventaire.remove(nourriture)
        else:
            print(f"{self.nom} n'a pas {nourriture.nom} dans son inventaire.")

    def deplacer(self, direction):
        # Consommation d'endurance en fonction de la charge et de la force
        poids_total = sum([objet.poids for objet in self.inventaire])
        cout_endurance = poids_total / (self.force * 1000)
        if self.endurance >= cout_endurance:
            if direction == "Nord":
                self.y += 1
            elif direction == "Sud":
                self.y -= 1
            elif direction == "Est":
                self.x += 1
            elif direction == "Ouest":
                self.x -= 1
            self.endurance -= cout_endurance
            print(f"{self.nom} se déplace vers {direction} à la position ({self.x}, {self.y}).")
        else:
            print(f"{self.nom} est trop fatigué pour se déplacer.")

    def dormir(self):
        self.points_de_vie = min(self.points_de_vie + 1, self.max_points_de_vie)
        self.endurance = min(self.endurance + 2, self.max_endurance)
        print(f"{self.nom} dort et récupère de l'énergie.")
    
    def fuir(self):
        directions = ["Nord", "Sud", "Est", "Ouest"]
        random.shuffle(directions)  # Mélanger les directions pour choisir aléatoirement

        for direction in directions:
            cout_endurance = self.calculer_cout_endurance() * 2  # Coût doublé pour la fuite
            if self.endurance >= cout_endurance:
                self.deplacer(direction)
                self.deplacer(direction)  # Se déplacer deux fois dans la même direction
                break
        else:
            print(f"{self.nom} est trop fatigué pour fuir.")

    def calculer_cout_endurance(self):
        # Calculer le coût d'endurance en fonction de la charge et de la force
        poids_total = sum([objet.poids for objet in self.inventaire])
        cout_endurance = poids_total / (self.force * 1000)
        return cout_endurance
    
    # def recevoir_degats(self, degats):
    #     if self.bouclier:
    #         self.defendre()
    #         dammage = degats - self.bouclier.defense
    #         if dammage < 0:
    #             dammage = 0
    #         self.points_de_vie -= dammage
    #     else:
    #         self.points_de_vie -= degats
    #     if self.points_de_vie <= 0:
    #         print(f"{self.nom} a ete terasser et rejoint le cimetière!")
    #         print("\n")
    #     else:
    #         print(f"{self.nom} a maintenant {self.points_de_vie} points de vie.")
    #         print("\n")

    def recevoir_degats(self, degats):
        if self.bouclier and self.endurance > 0:
            cout_endurance = self.bouclier.poids / (100 * self.force)
            if self.endurance >= cout_endurance:
                self.endurance -= cout_endurance
                self.defendre()  # Déplacer cette ligne ici
                dammage = degats - self.bouclier.defense
                if dammage < 0:
                    dammage = 0
                self.points_de_vie -= dammage
            else:
                print(f"{self.nom} est trop fatigué pour se défendre.")
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

# Utilisation de la factory pour créer un personnage
arthur = PersonnageFactory.create_personnage("Arthur", 100, 100, 20, 0, 0, epee, bouclier)
lancelot = PersonnageFactory.create_personnage("Lancelot", 120, 80, 25, 2, 2, epee, bouclier)
gawain = PersonnageFactory.create_personnage("Gawain", 110, 90, 22, 1, 1, epee, bouclier)
perceval = PersonnageFactory.create_personnage("Perceval", 105, 95, 18, 3, 3, epee, bouclier)

