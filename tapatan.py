###############################
# Groupe : MIASHS TD2
# Maxime Ebran
# Marie-Ange MESKINE
# Victoire Maga
# Sedra Ramarosaona
# Saïdou Barry
# Eskender Ayadi
#
# https://github.com/uvsq22000946/projet_tapatan
###############################

###############################
# Import des librairies

import tkinter as tk
import random as rd

###############################
# Constantes

HEIGHT = 500
WIDTH = 500


###############################
# Variables globales

tableau = []
nombre_de_pion = 0

###############################
# Fonctions


def affiche_terrain():
    """Affiche le terrain"""
    canvas.create_line((100, 100), (100, 400), fill="white")
    canvas.create_line((100, 100), (400, 100), fill="white")
    canvas.create_line((100, 100), (400, 400), fill="white")
    canvas.create_line((400, 400), (100, 400), fill="white")
    canvas.create_line((400, 400), (400, 100), fill="white")
    canvas.create_line((100, 400), (400, 100), fill="white")
    canvas.create_line((100, 250), (400, 250), fill="white")
    canvas.create_line((250, 100), (250, 400), fill="white")


def conversion(x, y):
    x = (x - 75) // 150
    y = (y - 75) // 150
    return x, y


def tableau_terrain():
    """Genere le tableau correspondant au terrain"""
    for x in range(3):
        ligne = []
        for y in range(3):
            ligne.append([-1])
        tableau.append(ligne)


def clic(event):
    """Si il y a moins de 6 pions ajoute un 
    pion sur la case cibler sinon deplace un pion"""
    i, j = conversion(event.x, event.y)
    if nombre_de_pion <= 5:
        if tableau[i][j][0] != -1:
            pass
        else:
            placer_pion(event)


def second_clic(event):
    """Sauvegarde les coordonnees du clic precendant"""

def placer_pion(event):
    """Si le joueur actuel a moins de trois pion, 
    place un nouveau pion de sa couleur"""
    global nombre_de_pion, couleur
    i, j = conversion(event.x, event.y)
    x, y = i * 150 + 100, j * 150 + 100
    print(tableau)
    nombre_de_pion += 1
    if couleur == "blue":
        tableau[i][j].append(canvas.create_oval((x - 25, y - 25), (x + 25, y + 25), fill=couleur))
        tableau[i][j][0] = 2
        couleur = "red"
    else:
        tableau[i][j].append(canvas.create_oval((x - 25, y - 25), (x + 25, y + 25), fill=couleur))
        tableau[i][j][0] = 1
        couleur = "blue"


def deplacer_pion(event):
    """Si il y a deja six pions, la phase 
    de deplacement commence"""
    i, j = conversion(event.x, event.y)
    x, y = i * 150 + 100, j * 150 + 100
    if tableau[i][j][0] == -1:
        pass
    else:
        pass
        

def joueur1_rouge():
    """Definie le joueur rouge comme premier joueur"""
    global couleur
    couleur = "red"
    fenetre_de_bienvenue.destroy()

def joueur1_bleu():
    """Definie le joueur rouge comme premier joueur"""
    global couleur
    couleur = "blue"
    fenetre_de_bienvenue.destroy()

def first_player():
    """Choisie le premier joueur"""
    global fenetre_de_bienvenue
    fenetre_de_bienvenue = tk.Toplevel(racine, bg="black")
    label = tk.Label(fenetre_de_bienvenue, text="Bienvenue sur Tapatan \n Choisissez le joueur 1", font=("Helvatica, 20"), bg="black", fg="white")
    boutton_rouge = tk.Button(fenetre_de_bienvenue, text="Rouge", font=("helvatica, 25"), bg="black", fg="red", command=joueur1_rouge)
    boutton_bleu = tk.Button(fenetre_de_bienvenue, text="Bleu", font=("helvatica, 25"), bg="black", fg="blue", command=joueur1_bleu)

    label.grid(row= 0)
    boutton_rouge.grid(row= 1)
    boutton_bleu.grid(row=2)

###############################
# Programme principal

racine = tk.Tk()

first_player()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH, bg="black")
affiche_terrain()

canvas.grid()
tableau_terrain()
print(tableau)
canvas.bind('<Button-1>', clic)
racine.mainloop()