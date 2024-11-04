
from forme import forme
from random import sample
from random import shuffle, randint

def couleur_aleatoire():
    print("\nRandom Color file")
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    hexa = "ABCDEF0123456789"
    return('#' + ''.join(sample(hexa, 6)))


def stars():
    for i in range(5):
        t.fd(5)
        t.right(144)

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



def porte(x,y,couleur):
    print("\nPorte file")
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''
    up()
    goto(x,y)
    left(180)
    forward(30//2)
    left(180)
    down()
    pencolor("black")
    print(couleur)
    fillcolor(couleur)
    begin_fill()
    rectangle(x,y,30,50)
    end_fill()

def rdc(x, y_sol, c_facade, c_porte):
    print("\nRDC File")
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    facade(x, y_sol, c_facade, 0)
    i = randint(1, 3)
    print("i", i)
    if i == 1:
        fenetre(x-25, 10)
        up()

        pendown()
        fenetre(x+10, 10)
        up()

        down()
        porte(x+40, 0, "saddlebrown")
        up()

    elif i == 2:
        fenetre(x-25, 10)
        up()

        down()
        porte(x, 0, "saddlebrown")
        up()

        down()
        fenetre(x+60, 10)
        up()
    elif i == 3:
        porte(x-40, 0, "saddlebrown")
        up()

        down()
        fenetre(x+10, 10)
        up()

        down()
        fenetre(x+50, 10)
        up()


def sol(y_sol):
    print("\nSol file")
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    pensize(3)
    trait(-1000, y_sol, 1000, y_sol)


def toit1(x, y_sol, niveau):
    print("\nToit1 file")
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    up()
    goto(x, y_sol+(60*niveau))
    left(180)
    forward(140//2+10)
    left(180)
    down()
    color("aliceblue")
    begin_fill()
    forward(160)
    left(180-20)
    forward(85)
    left(40)
    forward(85)
    right(200)
    end_fill()

def toit2(x, y_sol, niveau):
    print("\nToit2 file")
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    pensize(4)
    up()
    goto(x, y_sol+(60*niveau))
    backward(280)
    forward(100)
    down()
    color("black")
    begin_fill()
    forward(100)
    forward(85)
    end_fill()


def toit(x, y_sol, niveau):
    print("\nToit file")
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    print("Toit file")
    a = randint(0, 0)
    if a == 0:
        toit1(x, y_sol, niveau)
    else:
        toit2(x, y_sol, niveau)

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


def arbre(n, longueur):
    color('brown')
    if n == 0:
        color('green')
        forward(longueur)
        backward(longueur)
        color('brown')
    else:
        width(n)
        forward(longueur/3)
        left(30)
        arbre(n-1, longueur*2/3)
        right(60)
        arbre(n-1, longueur*2/3)
        left(30)
        backward(longueur/3)
        
def arbre_place(x,y):
    color('brown')
    up()
    goto(x, y)
    setheading(90)  
    down()
    arbre(7,200)
    
