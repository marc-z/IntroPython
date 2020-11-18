import ipyturtle

global current
current = None

def tableau(largeur=300, hauteur=750):
    global current
    current = ipyturtle.Turtle(largeur, hauteur)
    return current

def avancer(longueur):
    current.forward(longueur)

def reculer(longueur):
    current.back(longueur)

def changer_couleur(rouge,vert,bleu):
    current.pencolor(rouge, vert, bleu)

def rouge():
    changer_couleur(255,0,0)

def vert():
    changer_couleur(0,255,0)

def bleu():
    changer_couleur(0,0,255)

def lever_crayon():
    current.penup()

def poser_crayon():
    current.pendown()

def tourner(angle):
    current.left(angle)

def effacer():
    current.reset()
    couleur(0,0,0)

def aller(x,y):
    lever_crayon()
    a,b = current.position()
    angle = current.heading()
    tourner(-angle)
    avancer(x-a)
    tourner(90)
    avancer(y-b)
    tourner(-90+angle)
    poser_crayon()

def regarder_vers(a):
    tourner(a-current.heading())
