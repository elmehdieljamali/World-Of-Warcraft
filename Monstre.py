from Personnage import Personnage

class Monstre(Personnage):
    def __init__(self, nom, points_de_vie, endurance, force, arme, x, y):
        super().__init__(nom, points_de_vie, endurance, force, arme, x, y)