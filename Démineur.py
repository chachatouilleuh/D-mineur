#listgénérale=[ligne1,ligne2,ligne3]
#ligne1=[]
#ligne2=[]
#ligne3=[]

tableau=[]
largeur="x"
hauteur="x"
def init(largeur, hauteur):
    def tableau():
        difficulté=input("Choisissez un niveau facile=1 , moyen=2, difficile=3 :") 
        if difficulté==1:
            largeur=5
            hauteur=5
        elif difficulté==2:
            largeur=15
            hauteur=15
        else:
            largeur=50
            hauteur=50
    return init(tableau,largeur,hauteur)

def init(tableau,largeur,hauteur):
    for i in hauteur:
        tableau.append([])
        for j in largeur:
            tableau[i].append("x")
    

#initialiser mines
#maj demineur (0,1,2)
#si 0 >>> ouvre la case voisine
#si mine >>> perdu
#si nombre de cases restantes = nombre de mines >>> gagné
#le joueur rentre une info
#input():

