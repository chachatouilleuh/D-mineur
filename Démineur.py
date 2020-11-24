#Charly Despeyroux

import random

largeur=0
hauteur=0

def demandeDifficulte():
    global largeur
    global hauteur
    difficulté=int(input("Choisissez un niveau facile=1 , moyen=2, difficile=3 :")) 
    if difficulté==1:
        largeur=5
        hauteur=5

    elif difficulté==2:
        largeur=15
        hauteur=15
    else:
        largeur=50
        hauteur=50

def initTableau(largeur,hauteur):
    tableau=[]
    for i in range(hauteur):
        tableau.append([])
        for j in range(largeur):
            tableau[i].append("x")
    return tableau

def initMines(largeur,hauteur):
    tableau=[]
    for i in range(hauteur):
        tableau.append([])
        for j in range(largeur):
            tableau[i].append(0)
    return tableau


def afficher(tableau):
    print("  0 1 2 3 4")
    for i in range(0,len(tableau)):
        print(i, end=" ")
        for j in range(0,len(tableau[0])):
               print (tableau[i][j], end=" ")      
        print("")

def placerbombe(tableau, nbBombe):
    i=0
    while i<nbBombe:
        ligne = random.randint(0,len(tableau)-1)
        colonne = random.randint(0,len(tableau[0])-1)
        if (tableau[ligne][colonne]!="b"):
            tableau[ligne][colonne]="b"
            i += 1


def demineur():
    bombe=0
    tour=0
    i=0
    global largeur
    global hauteur 
    demandeDifficulte()
    
    ligne = largeur
    colonne = hauteur
    nbBombe= (largeur*hauteur)//4


    plateau = initTableau(ligne,colonne)
    plateauMines = initMines(ligne,colonne)

    afficher(plateau)
    afficher(plateauMines)
    #je place les bombes
    placerbombe(plateauMines, nbBombe)
    afficher(plateauMines)


    choixJoueur=0
    #je demande au joueur d'entrer une coordonnée
    while (tour<len(plateau)*len(plateau[0])-bombe and choixJoueur != "b"):
        choixJoueur=0
        print('choisir une ligne :', end=" ")
        x = int(input())
        print('choisir une colonne :', end=" ")
        y = int(input())
        choixJoueur=plateauMines[x][y]
        if choixJoueur == "b":
            print ("T un raT")
        else: 
            print ("Yay, continue !")
            #plateau.replace(choixJoueur)
            #afficher(plateau)
        tour += 1 

demineur()