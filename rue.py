"""Ce fichier permet de dessiner une rue à l'aide des fonctions suivantes :

+ dessiner_rue_aleatoire()
+ dessiner_rue_decrite(rue:dict)
"""


# Importation

from dessiner import triangle_equilateral


# Constantes

LARGEUR_IMMEUBLE = 50


# Fonction privées

def immeuble_aleatoire(numero:int) -> dict:
    informations = {}
    informations['couleur_facade'] = couleur_aleatoire()
    informations['numero'] = numero
    return informations

def couleur_aleatoire() -> str:
    return "red"

def coordonnees_facade(immeuble:dict) -> tuple:
    x_gauche = 30 * immeuble['numero']
    y_bas = 30 * immeuble['numero']
    return (x_gauche, y_bas)

def dessiner_facade(immeuble:dict) -> None:
    # Traduction des données de rue vers dessiner
    crayon = {}
    crayon['écriture'] = "blue"
    crayon['fond'] = immeuble['couleur_facade']
    crayon['épaisseur'] = 5 * immeuble['numero']
    x, y = coordonnees_facade(immeuble)  # désempaquatage du couple
    cote = LARGEUR_IMMEUBLE
    # Demande d'affichage
    triangle_equilateral(cote, crayon, (x,y))

def dessiner_porte(immeuble:dict) -> None:
    # Traduction des données de rue vers dessiner
    crayon = {}
    pass

def dessiner_immeuble(immeuble:dict) -> None:
    dessiner_facade(immeuble)
    dessiner_porte(immeuble)
    # à compléter avec d'autres fonctions pour le reste : toit, fenêtres...






