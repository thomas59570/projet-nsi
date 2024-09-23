from turtle import *
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    print("\nFacade file")
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    up()
    pencolor("black")
    fillcolor(couleur)
    y = y_sol + niveau * 60

    goto(x, y)
    begin_fill()
    rectangle(x, y, 140, 60)
    end_fill()
    up()


from facade import facade
from random import shuffle, randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle


def etage(x, y_sol, couleur, niveau):
    print("\n Etage file")
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    y = y_sol + niveau * 60
    # dessin des murs
    facade(x, y_sol, couleur, niveau)
    # dessin des 3 Eléments
    for i in range(3):
        i = randint(1, 2)
        print("i", i)
        if i == 1:
            fenetre(x-25, y+15)
        else:
            fenetre_balcon(x-25, y)
        x += 40




from random import sample

def couleur_aleatoire():
    print("\nRandom Color file")
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    hexa = "ABCDEF0123456789"
    return('#' + ''.join(sample(hexa, 6)))



from rectangle import rectangle
from turtle import *


def fenetre(x, y):
    print("\n Fenetre file")
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    up()
    goto(x-15, y)
    down()
    pencolor("black")
    fillcolor("white")
    begin_fill()
    rectangle(x-15, y, 30, 30)
    end_fill()

    up()



def fenetre_balcon(x, y):
    print("\nFenetre Balcon file")
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    up()
    goto(x-15, y)
    down()
    pencolor("black")
    fillcolor("white")
    begin_fill()
    rectangle(x-15, y, 30, 50)
    end_fill()
    up()
    pencolor("black")
    left(90)

    trait((xcor() - 4.2), ycor(),
          (xcor() - 4.2), ycor())

    trait(xcor(), ycor(),
          xcor(), (ycor() + 25))

    # For loop pour les barreaux
    for i in range(9):

        trait((xcor() + 4.2), ycor() - 25,
              (xcor() + 4.2), ycor())

    right(90)
    rectangle(x - 15, y, 38.4, 25)
