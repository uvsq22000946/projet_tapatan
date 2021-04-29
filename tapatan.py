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
first_clic = []

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
    global first_clic
    i, j = conversion(event.x, event.y)
    if nombre_de_pion <= 5:
        if tableau[i][j][0] != -1:
            pass
        else:
            placer_pion(i, j)
    else:
        if tableau[i][j][0] == -1:
            if first_clic == []:
                pass
            else:
                deplacer_pion(first_clic[0], first_clic[1], i, j)
                first_clic = []
        else:
            if first_clic == []:
                first_clic.append(i)
                first_clic.append(j)
            else:
                pass
    checking_colonne()
    checking_ligne()
    checking_diagonal()
    checking_diagonal_inverse()


def placer_pion(i, j):
    """Si le joueur actuel a moins de trois pion,
    place un nouveau pion de sa couleur"""
    global nombre_de_pion, couleur
    x, y = i * 150 + 100, j * 150 + 100
    if couleur == "blue":
        tableau[i][j].append(canvas.create_oval((x - 25, y - 25),
                                                (x + 25, y + 25),
                                                fill=couleur))
        tableau[i][j][0] = 2
        couleur = "red"
        label_joueur.config(text="Joueur rouge", fg=couleur)
    else:
        tableau[i][j].append(canvas.create_oval((x - 25, y - 25),
                                                (x + 25, y + 25),
                                                fill=couleur))
        tableau[i][j][0] = 1
        couleur = "blue"
        label_joueur.config(text="Joueur bleu", fg=couleur)
    nombre_de_pion += 1


def deplacer_pion(i1, j1, i2, j2):
    """Si il y a deja six pions, la phase
    de deplacement commence"""
    global couleur
    x, y = i2 * 150 + 100, j2 * 150 + 100
    canvas.delete(tableau[i1][j1][1])
    if tableau[i1][j1][0] == 1:
        tableau[i2][j2][0] = 1
        couleur = "red"
        label_joueur.config(text="Joueur bleu", fg="blue")
    else:
        tableau[i2][j2][0] = 2
        couleur = "blue"
        label_joueur.config(text="Joueur rouge", fg="red")
    tableau[i1][j1][0] = -1
    tableau[i1][j1] = tableau[i1][j1][:-1]
    tableau[i2][j2].append(canvas.create_oval((x - 25, y - 25),
                                              (x + 25, y + 25), fill=couleur))


def checking_colonne():
    """Si trois pions sont alligner verticalement,
    la partie se termine"""
    for x in range(3):
        win = []
        for y in range(3):
            if tableau[x][y][0] == 1:
                win.append(1)
            elif tableau[x][y][0] == 2:
                win.append(2)
        if win.count(1) == 3:
            victoire("rouge")
        elif win.count(2) == 3:
            victoire("bleu")


def checking_ligne():
    """Si trois pions sont alligner horizontalement,
    la partie se termine"""
    for y in range(3):
        win = []
        for x in range(3):
            if tableau[x][y][0] == 1:
                win.append(1)
            elif tableau[x][y][0] == 2:
                win.append(2)
        if win.count(1) == 3:
            victoire("rouge")
        elif win.count(2) == 3:
            victoire("bleu")


def checking_diagonal():
    """Si trois pions sont allignes en diagonnal,
    la partie se termine"""
    win = []
    for x in range(3):
        if tableau[x][x][0] == 1:
            win.append(1)
        elif tableau[x][x][0] == 2:
            win.append(2)
    if win.count(1) == 3:
        victoire("rouge")
    elif win.count(2) == 3:
        victoire("bleu")


def checking_diagonal_inverse():
    """Si trois pions sont allignes en diagonnal,
    la partie se termine"""
    win = []
    for x in range(1, 4):
        if tableau[-x][x - 1][0] == 1:
            win.append(1)
        elif tableau[-x][x - 1][0] == 2:
            win.append(2)
    if win.count(1) == 3:
        victoire("rouge")
    elif win.count(2) == 3:
        victoire("bleu")


def victoire(couleur):
    print("Le joueur", couleur, "a gagner")


def joueur1_rouge():
    """Definie le joueur rouge comme premier joueur"""
    global couleur, label_joueur
    couleur = "red"
    fenetre_de_bienvenue.destroy()
    label_joueur = tk.Label(racine, text="Joueur rouge",
                            font=("Helvatica", "30"), bg="black", fg=couleur)

    label_joueur.grid(column=1, row=0)
    affiche_terrain()


def joueur1_bleu():
    """Definie le joueur rouge comme premier joueur"""
    global couleur, label_joueur
    couleur = "blue"
    fenetre_de_bienvenue.destroy()
    label_joueur = tk.Label(racine, text="Joueur bleu",
                            font=("Helvatica", "30"), bg="black", fg=couleur)

    label_joueur.grid(column=1, row=0)
    affiche_terrain()


def first_player():
    """Choisie le premier joueur"""
    global fenetre_de_bienvenue
    fenetre_de_bienvenue = tk.Toplevel(racine, bg="black")
    label = tk.Label(fenetre_de_bienvenue,
                     text="Bienvenue sur Tapatan \n Choisissez le joueur 1",
                     font=("Helvatica, 20"), bg="black", fg="white")
    boutton_rouge = tk.Button(fenetre_de_bienvenue, text="Rouge",
                              font=("helvatica, 25"), bg="black",
                              fg="red", command=joueur1_rouge)
    boutton_bleu = tk.Button(fenetre_de_bienvenue, text="Bleu",
                             font=("helvatica, 25"), bg="black",
                             fg="blue", command=joueur1_bleu)
    boutton_contre_IA = tk.Button(fenetre_de_bienvenue,
                                  text="Partie contre l'IA",
                                  font=("Helvatica", "25"),
                                  bg="black", fg="white",
                                  command=partie_contre_IA)

    label.grid(row=0)
    boutton_rouge.grid(row=1)
    boutton_bleu.grid(row=2)
    boutton_contre_IA.grid(row=3)

###############################
# Fonctions IA


def partie_contre_IA():
    """Lance une partie contre l'IA"""
    pass


def placement():
    """Place des pions aléatoirement sauf
    si l'IA peut gagner ou perdre"""
    jouer = False
    while jouer != True:
        x, y = rd.randint(1, 3), rd.randint(1, 3)
        if tableau[x][y] == -1:
            placer_pion(x, y)
            jouer = True


###############################
# Programme principal

racine = tk.Tk()
racine.config(bg="black")

first_player()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH, bg="black")
affiche_terrain()

canvas.grid()
tableau_terrain()
canvas.bind('<Button-1>', clic)
racine.mainloop()
