from turtle import *
import turtle
import random

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


def rectangle1(x,y,c_facade):
    
    goto(x,y)
    for i in range(2):
        forward(2000)
        right(90)
        forward(170)
        right(90)

def trait(x1,y1,x2,y2):
    print("\nTrait file")
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    
    up()
    goto(x1, y1)
    down()
    goto(x2, y2)
