import random
from Objet import Objet
from Arme import Arme
from Bouclier import Bouclier
from Nourriture import Nourriture
from Personnage import Personnage
from Monstre import Monstre
from Hero import Hero


# def verifier_nouvelle_position(personnage, direction, zone_jeu):
#     directions = ["Nord", "Sud", "Est", "Ouest"]
#     random.shuffle(directions)  # Mélanger les directions pour plus de variabilité

#     for dir in directions:
#         nouvelle_x, nouvelle_y = personnage.x, personnage.y

#         if dir == "Nord" and personnage.y > 0:
#             nouvelle_y -= 1
#         elif dir == "Sud" and personnage.y < len(zone_jeu) - 1:
#             nouvelle_y += 1
#         elif dir == "Est" and personnage.x < len(zone_jeu[0]) - 1:
#             nouvelle_x += 1
#         elif dir == "Ouest" and personnage.x > 0:
#             nouvelle_x -= 1

#         # Vérifier que les nouvelles coordonnées sont dans les limites de la matrice
#         if 0 <= nouvelle_x < len(zone_jeu[0]) and 0 <= nouvelle_y < len(zone_jeu):
#             if zone_jeu[nouvelle_y][nouvelle_x] is None:
#                 return nouvelle_x, nouvelle_y

#     print(f"{personnage.nom} est entouré et ne peut pas se déplacer.")
#     return personnage.x, personnage.y

def verifier_nouvelle_position(personnage, direction, zone_jeu):
    directions = ["Nord", "Sud", "Est", "Ouest"]
    random.shuffle(directions)  # Mélanger les directions pour plus de variabilité

    for dir in directions:
        nouvelle_x, nouvelle_y = personnage.x, personnage.y

        if dir == "Nord" and personnage.y > 0:
            nouvelle_y -= 1
        elif dir == "Sud" and personnage.y < len(zone_jeu) - 1:
            nouvelle_y += 1
        elif dir == "Est" and personnage.x < len(zone_jeu[0]) - 1:
            nouvelle_x += 1
        elif dir == "Ouest" and personnage.x > 0:
            nouvelle_x -= 1

        # Vérifier que les nouvelles coordonnées sont dans les limites de la matrice
        if 0 <= nouvelle_x < len(zone_jeu[0]) and 0 <= nouvelle_y < len(zone_jeu):
            if zone_jeu[nouvelle_y][nouvelle_x] is None:
                # Mettre à jour la matrice seulement si les nouvelles coordonnées sont valides
                zone_jeu[personnage.y][personnage.x] = None
                zone_jeu[nouvelle_y][nouvelle_x] = personnage
                personnage.x, personnage.y = nouvelle_x, nouvelle_y
                return nouvelle_x, nouvelle_y

    print(f"{personnage.nom} est entouré et ne peut pas se déplacer.")
    return personnage.x, personnage.y

    
def sont_adjacents(perso1, perso2):
    return abs(perso1.x - perso2.x) <= 1 and abs(perso1.y - perso2.y) <= 1

def demarrer_(equipe_attaquante, equipe_defense, zone_jeu):
    for attaquant in equipe_attaquante.values():
        ennemi_proche = False
        defenseur_proche = None

        # Vérifier s'il y a un ennemi adjacent
        for defenseur in equipe_defense.values():
            if sont_adjacents(attaquant, defenseur):
                ennemi_proche = True
                defenseur_proche = defenseur
                break

        if ennemi_proche:
            # Probabilités : 80% attaquer, 20% fuir
            action = random.choices(["attaquer", "fuir"], [80, 20], k=1)[0]
            if action == "attaquer" and defenseur_proche:
                attaquant.attaquer(defenseur_proche)
                if defenseur_proche.points_de_vie > 0:
                    defenseur_proche.attaquer(attaquant)
                return ("combat", attaquant, defenseur_proche)
            elif action == "fuir":
                attaquant.fuir()
                return ("fuir", attaquant)
        else:
            # Probabilités : 60% déplacer, 10% manger, 10% dormir, 20% rencontre aléatoire
            action = random.choices(["deplacer", "manger", "dormir", "rencontre"], [60, 10, 10, 20], k=1)[0]
            if action == "deplacer":
                direction = random.choice(["Nord", "Sud", "Est", "Ouest"])
                return ("deplacer", attaquant, direction)
            elif action == "manger":
                if attaquant.inventaire:  # Assurez-vous que l'inventaire n'est pas vide
                    nourriture = random.choice(attaquant.inventaire)
                    attaquant.manger(nourriture)
                return ("manger", attaquant)
            elif action == "dormir":
                attaquant.dormir()
                return ("dormir", attaquant)
            elif action == "rencontre":
                return ("rencontre", attaquant)  # Ajoutez le traitement de la rencontre dans votre programme

    return ("rien", None)


def attaquer(equipe_attaquant, equipe_defenseur, zone_jeu):
    for attaquant in equipe_attaquant.values():
        for defenseur in equipe_defenseur.values():
            if sont_adjacents(attaquant, defenseur):
                print(f"{attaquant.nom} ({attaquant.points_de_vie} PV) ({attaquant.endurance} ST) va affronter {defenseur.nom} avec {defenseur.arme.nom} ({defenseur.arme.degats} DP) ({defenseur.endurance} ST).\n\n")
                attaquant.attaquer(defenseur)

                if defenseur.points_de_vie > 0:
                    defenseur.attaquer(attaquant)

                # Mise à jour de la condition de vie et élimination du personnage si nécessaire
                if attaquant.points_de_vie <= 0:
                    del equipe_attaquant[attaquant.nom]
                    zone_jeu[attaquant.y][attaquant.x] = None

                if defenseur.points_de_vie <= 0:
                    del equipe_defenseur[defenseur.nom]
                    zone_jeu[defenseur.y][defenseur.x] = None


def verifier_eliminés(equipe, nom_equipe):
    if not equipe:
        print(f"L'equipe {nom_equipe} est eliminee. Fin du jeu !")
        return True  # Renvoie True si l'équipe est éliminée
    return False  # Renvoie False sinon


def main():

    zone_jeu = [[None for _ in range(10)] for _ in range(10)]

    # Création des armes et des personnages
    epee = Arme("Excalibur", 10, 100, 3000)
    gourdin = Arme("Gourdin de Géant", 15, 150, 5000)
    heros = Hero("Arthur", 100, 100, 20, random.randint(0, 9), random.randint(0, 9), epee)
    monstre = Monstre("Grendel", 120, 80, 15, random.randint(0, 9), random.randint(0, 9), gourdin)
    bouclier = Bouclier("Bouclier doree", 8, 80)
    nourriture = Nourriture("Baie", 1, 20)

    armes = [epee, gourdin]
    heros_liste = [heros]
    monstres_liste = [monstre]
    boucliers = [bouclier]

    equipes = {
        "Equipe Héros": {
            "Arthur": heros,
        },
        "Equipe Monstres": {
            "Grendel": monstre,
        }
    }

    zone_jeu[heros.y][heros.x] = heros
    zone_jeu[monstre.y][monstre.x] = monstre

    attribut_aleatoire = bool(random.getrandbits(1))
    print(f"lES MONSTRES ET LES HEROS VONT S AFFRONTER\n")  
    print(f"__________________________________________\n")  

    while not (verifier_eliminés(equipes["Equipe Héros"], "Equipe Héros") or verifier_eliminés(equipes["Equipe Monstres"], "Equipe Monstres")):
    
        action_effectuee = demarrer_(equipes["Equipe Héros"], equipes["Equipe Monstres"], zone_jeu)
        

        # Mettre à jour la matrice si un déplacement a eu lieu
        if action_effectuee[0] == "deplacer":
            personnage, direction = action_effectuee[1], action_effectuee[2]
            nouvelle_x, nouvelle_y = verifier_nouvelle_position(personnage, direction, zone_jeu)
            
            if (nouvelle_x, nouvelle_y) != (personnage.x, personnage.y):
                zone_jeu[personnage.y][personnage.x] = None
                zone_jeu[nouvelle_y][nouvelle_x] = personnage
                personnage.x, personnage.y = nouvelle_x, nouvelle_y

        
        

if __name__ == "__main__":
    main()