"""Ce fichier permet de dessiner des formes à l'aide des fonctions suivantes

+ triangle_equilateral(cote, info_feutre, coordonnees)
+ arc_de_cercle(rayon, angle, info_feutre, coordonnees)
 
 
Exemples d'utilisation :
>>> informations_feutre = {'écriture':'blue', 'fond':'#FF88FF', 'épaisseur':5}
>>> triangle_equilateral(50, informations_feutre, (50,100))
>>> arc_de_cercle(75, 360, informations_feutre, (200,-200))
"""
 
 
# Importation
 
import turtle as trt
import random as rd
 
 
# Déclaration des fonctions privées
 
def nouveau_stylo(ecriture, fond, largeur):
    """Renvoie la référence d'un stylo configuré
 
    :: param ecriture(str)  :: la couleur d'écriture ('red', '#FF0000')
    :: param fond(str)      :: la couleur de fond pour ce stylo
    :: param largeur(int)   :: la largeur du trait
    :: return (Turtle)      :: renvoie un objet de la classe Turtle
 
    """
    feutre = trt.Turtle()
    feutre.color(ecriture)
    feutre.fillcolor(fond)
    feutre.pensize(largeur)
    feutre.speed(5)
    return feutre
 
def deplacer(feutre, x, y):
    """Lève le feutre, déplace le feutre et abaisse le feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param x(int)         :: coordonnée horizontale (abscisse)
    :: param y(int)         :: coordonnée verticale (ordonnée)
    :: return (None)        :: c'est une fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.penup()       # On lève la pointe
    feutre.goto(x, y)  # On déplace le crayon
    feutre.pendown()     # On abaisse la pointe
 
def trace_triangle_equilateral(feutre, cote):
    """Trace un triangle (equilatéral) à l'aide du crayon feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur en pixel des côtés 
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.begin_fill()
    for x in range(3):
        feutre.forward(cote)
        feutre.left(120)
    feutre.end_fill()
    feutre.hideturtle()
 
def trace_arc(feutre, rayon, angle):
    """Trace un arc de cercle à l'aide du crayon feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.begin_fill()
    feutre.circle(rayon, angle)
    feutre.end_fill()
    feutre.hideturtle()
 
 
# Déclarations des fonctions publiques
 
def triangle_equilateral(cote, info_feutre, coordonnees):
    """Trace un triangle (equilatéral) à partir des info_feutre et aux bonnees coordonnées
 
    :: param cote(int)                     :: la valeur en pixel des côtés
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees (par désempaquetage)
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle_equilateral(feutre, cote)
 
    return feutre
 
def arc_de_cercle(rayon, angle, info_feutre, coordonnees):
    """Trace un arc de cercle à partir des info_feutre et aux bonnees coordonnées
 
    :: param rayon(int)                    :: la valeur en pixel du rayon
    :: param angle(int)                    :: la valeur en ° de l'angle
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees (par désempaquetage)
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_arc(feutre, rayon, angle)
 
    return feutre
 
def rectangle(x,y,w,h):
    print("\nRectangle file")
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    up()
    goto(x,y)
    left(180)
    forward(w//2)
    left(180)
    down()
    
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    
# Instructions du programme principal
 
if __name__ == '__main__':
