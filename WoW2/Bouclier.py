from Objet import Objet

class Bouclier(Objet):
    def __init__(self, nom, poids, defense):
        super().__init__(nom, poids)
        self.defense = defense
        self.endurance_reduction = poids/1000