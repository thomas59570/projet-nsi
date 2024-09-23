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

