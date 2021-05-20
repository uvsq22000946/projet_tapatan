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
# Fonctionnement :
#
# Choisissez le premier joueur si vous jouer contre
# un autre humain sinon choisissez partie contre IA
# dans la fentetre de bienvenue qui a tendance a rester
# en arriere plan.
# Lorsque vous jouer contre l'IA, vous etes automatiquement
# le joueur 1 et rouge. Durant la partie vous devrez cliquez
# sur les noeuds pour placer 3 pions puis les deplacer
# de la meme maniere. Le reste respecte les ragles du
# Tapatan.
#
# But :
#
# Aligner trois pions de sa couleur. Vous avez
# 3 pions pour ce faire. Une fois placer vous devez
# les deplacer en suivant les lignes blanches
# Vous ne pouvez pas passer votre tour
#
# Specificiter :
#
# Pour des raisons pratique, le jeu se deroule
# comme sur un vrai plateau. Il est donc possible
# de deplacer les pions meme sur des cases pourtant
# inaccessible.

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
compteur_objet = []

###############################
# Fonctions


def affiche_terrain():
    """Affiche le terrain"""
    compteur_objet.append(canvas.create_line((100, 100), (100, 400),
                          fill="white"))
    compteur_objet.append(canvas.create_line((100, 100), (400, 100),
                          fill="white"))
    compteur_objet.append(canvas.create_line((100, 100), (400, 400),
                          fill="white"))
    compteur_objet.append(canvas.create_line((400, 400), (100, 400),
                          fill="white"))
    compteur_objet.append(canvas.create_line((400, 400), (400, 100),
                          fill="white"))
    compteur_objet.append(canvas.create_line((100, 400), (400, 100),
                          fill="white"))
    compteur_objet.append(canvas.create_line((100, 250), (400, 250),
                          fill="white"))
    compteur_objet.append(canvas.create_line((250, 100), (250, 400),
                          fill="white"))


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
        compteur_objet.append(tableau[i][j][1])
        couleur = "red"
        label_joueur.config(text="Joueur rouge", fg=couleur)
    else:
        tableau[i][j].append(canvas.create_oval((x - 25, y - 25),
                                                (x + 25, y + 25),
                                                fill=couleur))
        tableau[i][j][0] = 1
        couleur = "blue"
        compteur_objet.append(tableau[i][j][1])
        label_joueur.config(text="Joueur bleu", fg=couleur)
    nombre_de_pion += 1
    checking_colonne()
    checking_ligne()
    checking_diagonal()
    checking_diagonal_inverse()


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
    compteur_objet.append(tableau[i2][j2][1])


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

    label_joueur.grid(column=2, row=0)
    affiche_terrain()


def joueur1_bleu():
    """Definie le joueur rouge comme premier joueur"""
    global couleur, label_joueur
    couleur = "blue"
    fenetre_de_bienvenue.destroy()
    label_joueur = tk.Label(racine, text="Joueur bleu",
                            font=("Helvatica", "30"), bg="black", fg=couleur)

    label_joueur.grid(column=2, row=0)
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
    canvas.unbind('<Button-1>')
    canvas.bind('<Button-1>', clic_IA)
    joueur1_rouge()


def clic_IA(event):
    clic(event)
    if nombre_de_pion <= 5:
        placement()


def disponiblite():
    """Renvoie une liste contenent des
    listes d'elements [x, y] etant les
    coordonnées des places disponibles
    sur le plateau"""
    disponible = []
    for x in range(0, 3):
        for y in range(0, 3):
            if tableau[x][y][0] == -1:
                disponible.append([x, y])
    return disponible


def placement():
    """Place des pions aléatoirement sauf
    si l'IA peut gagner ou perdre"""
    disponible = disponiblite()
    for liste in disponible:
        w, x, y, z = checking_IA(liste)
        match = placement_de_IA(w, x, y, z)
        if match is True:
            placer_pion(liste[0], liste[1])
            return
    r = rd.randint(0, len(disponible) - 1)
    i, j = disponible[r][0], disponible[r][1]
    placer_pion(i, j)


def checking_IA(liste):
    ligne = 0
    colonne = 0
    diagonal = 0
    diagonal_inverse = 0
    for x in range(1, 4):
        ligne += tableau[liste[0]][x - 1][0]
        colonne += tableau[x - 1][liste[1]][0]
        diagonal += tableau[x - 1][x - 1][0]
        diagonal_inverse += tableau[-x][x - 1][0]
    return ligne, colonne, diagonal, diagonal_inverse


def placement_de_IA(w, x, y, z):
    """Place les pions de facon a eviter de perdre la partie"""
    ligne, colonne, diagonal, diagonal_inverse = w, x, y, z
    if ligne + 2 == 3 or colonne + 2 == 3:
        return True
    elif diagonal_inverse + 2 == 3 or diagonal + 2 == 3:
        return True
    else:
        return False


def deplacement_de_IA():
    """Si il y a un coup gagnant a faire, IA le fait."""
    for x in range(3):
        for y in range(3):
            pass

###############################
# Sauvegarde


def savegarde():
    """Sauvegarde la disposition du terrain"""
    fic = open("save", "w")
    for x in range(3):
        for y in range(3):
            caractere = str(tableau[x][y][0])
            fic.write(caractere + "\n")
    fic.close()


def charger():
    """Charge la disposition du terrain"""
    global tableau
    fic = open("save", "r")
    delete_all()
    affiche_terrain()
    tableau = []
    tempo = []
    for row in fic:
        tempo.append(int(row))
    for x in range(0, 9, 3):
        ligne = []
        for y in range(3):
            unit = []
            unit.append(tempo[x + y])
            ligne.append(unit)
        tableau.append(ligne)
    recreation()
    fic.close()


def recreation():
    """Recrée le terrain apres le chargement"""
    for i in range(3):
        for j in range(3):
            x, y = i * 150 + 100, j * 150 + 100
            if tableau[i][j][0] == 1:
                tableau[i][j].append(canvas.create_oval(x - 25, y - 25,
                                                        x + 25, y + 25,
                                                        fill="red"))
                compteur_objet.append(tableau[i][j][1])
            elif tableau[i][j][0] == 2:
                tableau[i][j].append(canvas.create_oval(x - 25, y - 25,
                                                        x + 25, y + 25,
                                                        fill="blue"))
                compteur_objet.append(tableau[i][j][1])


def delete_all():
    """Supprime tout les elements du terrain"""
    for items in range(len(compteur_objet)):
        canvas.delete(items)

###############################
# Programme principal


racine = tk.Tk()
racine.config(bg="black")

first_player()
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH, bg="black")
boutton_save = tk.Button(racine, text="Sauvegarder", font=("Helvatica", "20"),
                         bg="black", fg="White", command=savegarde)
boutton_charger = tk.Button(racine, text="Charger", font=("Helvatica", "20"),
                            bg="black", fg="white", command=charger)
affiche_terrain()

canvas.grid(column=0, row=0, columnspan=2)
boutton_save.grid(column=0, row=2)
boutton_charger.grid(column=1, row=2)
tableau_terrain()
canvas.bind('<Button-1>', clic)
racine.mainloop()
