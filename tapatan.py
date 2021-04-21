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

    

def placer_pion(event):
    """Si le joueur actuel a moins de trois pion, 
    place un nouveau pion de sa couleur"""
    global nombre_de_pion, couleur
    i, j = conversion(event.x, event.y)
    x, y = i * 150 + 100, j * 150 + 100
    print(tableau)
    if nombre_de_pion <= 0:
        nombre_de_pion += 1
        couleur = first_player()
        tableau[i][j].append(canvas.create_oval((x - 25, y - 25), (x + 25, y + 25), fill=couleur))
        if couleur == "blue":
            tableau[i][j][0] = 1
        else:
            tableau[i][j][0] = 2

    elif nombre_de_pion <= 5:
        nombre_de_pion += 1
        if couleur == "blue":
            couleur = "red"
            tableau[i][j].append(canvas.create_oval((x - 25, y - 25), (x + 25, y + 25), fill=couleur))
        else:
            couleur = "blue"
            tableau[i][j].append(canvas.create_oval((x - 25, y - 25), (x + 25, y + 25), fill=couleur))

def first_player():
    choix = rd.randint(1, 2)
    if choix == 1:
        return "blue"
    if choix == 2:
        return "red"

###############################
# Programme principal

racine = tk.Tk()

canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH, bg="black")
affiche_terrain()

canvas.grid()
tableau_terrain()
print(tableau)
canvas.bind('<Button-1>', placer_pion)
racine.mainloop()