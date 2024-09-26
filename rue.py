"""Ce fichier permet de dessiner une rue à l'aide des fonctions suivantes :

+ dessiner_rue_aleatoire()
+ dessiner_rue_decrite(rue:dict)
"""

BATMAN : 

#initialize method
bat = turtle.Turtle()

#size of pointer and pen
bat.turtlesize(1, 1, 1)
bat.pensize(3)

#screen info
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("BATMAN")

#colour
bat.color("black", "black")


#begin filling color
bat.begin_fill()

#turn1
bat.left(90)   # turn pointer direction to left of 90'
bat.circle(50, 85) #draw circle of radius = 50 and 85'
bat.circle(15, 110)
bat.right(180)

#turn 2
bat.circle(30, 150)
bat.right(5)
bat.forward(10) #draw forward line of 10 units

#turn 3
bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

#turn 4
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

#turn5
bat.forward(30)
bat.left(55)
bat.forward(10)

#reverse

#turn 5
bat.forward(10)
bat.left(55)
bat.forward(30)

#turn 4

bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)

#turn 3
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

#turn 2
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

#turn 1
bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

#end color filling
bat.end_fill()

    #end the turtle method
turtle.done()


ciel étoilé:

import turtle
import random
  
  
# creating turtle object
t = turtle.Turtle()
  
# to activate turtle graphics Screen
w = turtle.Screen()
  
# setting speed of turtle
t.speed(300)
  
# giving the background color of turtle
# graphics screen
w.bgcolor("black")
  
# giving the color of pen to our turtle
# for drawing
t.color("white")
  
# giving title to our turtle graphics window
w.title("Starry Sky")
  
# making function to draw the stars
def stars():
    for i in range(5):
        t.fd(10)
        t.right(144)
  
  
# loop for making number of stars
for i in range(90):
    
    # generating random integer values for x and y
    x = random.randint(-640, 640)
    y = random.randint(-330, 330)
      
    # calling the function stars to draw the 
    # stars at random x,y value
    stars()
      
    # took up the turtle's pen
    t.up()
      
    # go at the x,y coordinate generated above
    t.goto(x, y)
      
    # took down the pen to draw
    t.down()
  
# for making our moon tooking up the pen
t.up()
  
# going at the specific coordinated
t.goto(0, 170)
  
# took down the pen to start drawing
t.down()
  
# giving color to turtle's pen
t.color("white")
  
# start filling the color
t.begin_fill()
  
# making our moon
t.circle(40)
  
# stop filling the color
t.end_fill()
  
# after drawing hidding the turtle from
# the window
t.hideturtle()
  
# terminated the window after clicking
w.exitonclick()

def immeuble(x, y_sol):
    print("\n Immeuble file")
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''

    # Nombre d'étage (aléatoire)
    nb_etage = randint(0, 4) # random entre 0 et 4
    print("Nombre d'étage", nb_etage)

    #Couleurs des éléments (aléatoire)
    c_facade = couleur_aleatoire()
    c_porte = couleur_aleatoire()

    # Dessin du RDC
    rdc(x, y_sol, c_facade, c_porte)

    # Dessin des étages
    for niveau in range(nb_etage):
      etage(x, y_sol, c_facade, niveau+1)

    # Dessin du toit
    toit(x, y_sol, nb_etage+1)
