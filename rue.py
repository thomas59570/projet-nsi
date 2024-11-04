
from elements import elements


def cree_ciel1():
    for i in range(400):
        
        # generating random integer values for x and y
        x = random.randint(-970, 970)
        y = random.randint(200, 500)
          
        # took up the turtle's pen
        t.up()
          
        # go at the x,y coordinate generated above
        t.goto(x, y)
        
        # took down the pen to draw
       
        t.down()
      # calling the function stars to draw the 
        # stars at random x,y value
        stars()
    # for making our moon tooking up the pen
    t.up()
      
    # going at the specific coordinated
    t.goto(850, 350)
      
    # took down the pen to start drawing
    t.down()
      
    # giving color to turtle's pen
    t.color("white")
      
    # start filling the color
    t.begin_fill()
      
    # making our moon
    t.circle(70)
      
    # stop filling the color
    t.end_fill()
    
    t.penup()

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


def route():
    turtle.tracer(0)
    turtle.penup()
    turtle.goto(-1000,0)
    turtle.pendown()
    pencolor('white')
    width(5)
    begin_fill()
    print(rectangle1(-1000,0,'white'))
    end_fill()
    print(rectangle(-1130,-95,150,30))
    begin_fill()
    print(rectangle(-830,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(-530,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(-230,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(70,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(370,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(670,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(970,-95,150,30))
    end_fill()
    begin_fill()
    print(rectangle(1270,-95,150,30))
    end_fill()

def main():
    print("Main file\n")

    turtle.clear()
    turtle.setup(800, 600)
    turtle.tracer(0)

    # On définit la hauteur du sol
    y_sol = 0

    # Dessin du sol de la rue
    sol(y_sol)

    # Dessin des 4 immeubles
    for i in range(11):
      immeuble(-875+(i*175), y_sol)
    

