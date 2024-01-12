from Objet import Objet

class Nourriture(Objet):
    def __init__(self, nom, poids, endurance_restoration):
        super().__init__(nom, poids)
        self.endurance_restoration = endurance_restoration