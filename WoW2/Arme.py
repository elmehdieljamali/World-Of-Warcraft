from Objet import Objet

class Arme(Objet):
    def __init__(self, nom, poids, degats, longueur):
        super().__init__(nom, poids)
        self.degats = degats
        self.longeur = longueur
        self.endurance_reduction = poids*longueur/10000