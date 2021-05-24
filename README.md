# projet_tapatan
Projet noté du S2 L1 MIASHS
 
 
 # Fonctionnement :

 Choisissez le premier joueur si vous jouer contre un autre humain sinon choisissez partie contre IA dans la fentetre de bienvenue qui a tendance a rester en arriere plan. Lorsque vous jouer contre l'IA, vous etes automatiquement le joueur 1 et rouge. Durant la partie vous devrez cliquez sur les noeuds pour placer 3 pions puis les deplacer de la meme maniere. Le reste respecte les règles du Tapatan.

# But :

 Aligner trois pions de sa couleur. Vous avez 3 pions pour ce faire. Une fois placer vous devez les deplacer en suivant les lignes blanches Vous ne pouvez pas passer votre tour.

# Specificiter :

 Pour des raisons pratique, le jeu se deroule comme sur un vrai plateau. Il est donc possible de deplacer les pions meme sur des cases pourtant inaccessible.

# Creation du programme :

 Le programme est fait sur 2 canvas. Une canvas que l'on pourrait qualifier de "Paramètre" qui sert à choisir les couleur de chaque joueur ou de choisir de jouer contre l'IA si l'on est seul. Ensuite il y a la Seconde canvas où il y a le plateau de jeu et où l'on joue directement. 

# caractéristiques problématiques :

 Lorsque l'on joue contre l'IA, après avoir palcer les 3pions, l'IA ne reponds plus donc si on decide de déplacer les pions pour pouvoir evantuellement gagner nous devons aussi le faire directement pour ceux des pions bleu; donc on se retrouve dans une situation comme ci on jouait à deuc ( car on controle les pions rouge et bleu ).
