#4 classes
#une class plateau
#ds celui ci un max de methodes utilitaires ( l afficher ...)
#
#Une classe (abstraite ou pas) qui représente une piece
import random
import time
from pieces import *

class Plateau:
    def __init__(self):
        self.tableau = []
        self.create()
        
        self.dicoLettreToPos = { "A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7 }
        self.dicoChiffreToPos = { "8" : 0, "7" : 1, "6" : 2, "5" : 3, "4" : 4, "3" : 5, "2" : 6, "1" : 7}
        self.PosToLettre = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H"}
        self.PosToChiffre = {0 : "8", 1 : "7", 2 : "6", 3 : "5", 4 : "4", 5 : "3", 6 : "2", 7 : "1"}
        self.pionBlanc1 = PionBlanc(0, 6)
        self.pionBlanc2 = PionBlanc(1, 6)
        self.pionBlanc3 = PionBlanc(2, 6)
        self.pionBlanc4 = PionBlanc(3, 6)
        self.pionBlanc5 = PionBlanc(4, 6)
        self.pionBlanc6 = PionBlanc(5, 6)
        self.pionBlanc7 = PionBlanc(6, 6)
        self.pionBlanc8 = PionBlanc(7, 6)

        self.tourBlanc1 = TourBlanc(0, 7)
        self.tourBlanc2 = TourBlanc(7, 7)
        
        self.cavalierBlanc1 = CavalierBlanc(1, 7)
        self.cavalierBlanc2 = CavalierBlanc(6, 7)
        
        self.fouBlanc1 = FouBlanc(2, 7)
        self.fouBlanc2 = FouBlanc(5, 7)

        self.roiBlanc = RoiBlanc(3, 7)

        self.dameBlanc = DameBlanc(4, 7)
        
        self.pionNoir1 = PionNoir(0, 1)
        self.pionNoir2 = PionNoir(1, 1)
        self.pionNoir3 = PionNoir(2, 1)
        self.pionNoir4 = PionNoir(3, 1)
        self.pionNoir5 = PionNoir(4, 1)
        self.pionNoir6 = PionNoir(5, 1)
        self.pionNoir7 = PionNoir(6, 1)
        self.pionNoir8 = PionNoir(7, 1)
        
        self.tourNoir1 = TourNoir(0, 0)
        self.tourNoir2 = TourNoir(7, 0)
        
        self.cavalierNoir1 = CavalierNoir(1, 0)
        self.cavalierNoir2 = CavalierNoir(6, 0)

        self.fouNoir1 = FouNoir(2, 0)
        self.fouNoir2 = FouNoir(5, 0)
        
        self.roiNoir = RoiNoir(3, 0)
        
        self.dameNoir = DameNoir(4, 0)
        
         
        self.tabDesPieces = [self.pionBlanc1, self.pionBlanc2,self.pionBlanc3, self.pionBlanc4, self.pionBlanc5, self.pionBlanc6, self.pionBlanc7, self.pionBlanc8, self.tourBlanc1, self.tourBlanc2, self.cavalierBlanc1, self.cavalierBlanc2, self.fouBlanc1, self.fouBlanc2, self.roiBlanc, self.dameBlanc, self.pionNoir1, self.pionNoir2,self.pionNoir3, self.pionNoir4, self.pionNoir5, self.pionNoir6, self.pionNoir7, self.pionNoir8, self.tourNoir1, self.tourNoir2, self.cavalierNoir1, self.cavalierNoir2, self.fouNoir1, self.fouNoir2, self.roiNoir, self.dameNoir]

        self.maj_pieces()

    def create(self):
       
        for i in range (8):
            self.tableau.append([" ", " ", " ", " ", " ", " ", " ", " "])

    def afficher(self):#on affiche le tableau de 8 cases
        repr =' '+' '+' A'+' B'+' C'+' D'+' E'+' F'+' G'+' H'+'\n' + ' ' + ' ' +'—'+'—'+ '—'+ '—'+ '—'+ '—'+ '—'+ '—'+ '—' + '—'+ '—'+ '—'+ '—'+ '—'+ '—'+ '—'+ '—' '\n'
        reprLignes = ""
        for i in range (8):#pour chaque lignes du tableau 
            lignes=self.tableau[i]   
            
            for j in range (8):#pour chaque case de la ligne
                reprLignes = reprLignes + str(lignes[j]) + " " # on écrit ds la chaine de crctr les caractr précedents et on rajoute le caractere de la case suivante, puis on met un espace pr etre aérer
            repr = repr + str(8-i) + '| ' + reprLignes + '|' + "\n" #on ajoute la chaine de la ligne i à la representation globale du tableau (puis on \n)
            reprLignes = ""#on efface la valeur de la ligne pour passer à la ligne du dessous
        repr = repr + '  ' + '—'+ '—'+ '—'+ '—'+ '—'+ '—'+ '—' + '—'+ '—'+ '—' + '—'+ '—' + '—'+ '—'+ '—' + '—'+ '—'
        print(repr)#à la fin on affiche la représentation globale du tableau, avec toutes les lignes

    def maj_pieces(self): #on suppr l'affichage de toutes les pieces et on remet les pieces à leurs à leurs coordonnées
        self.tableau = []
        for i in range (8):
            self.tableau.append([" ", " ", " ", " ", " ", " ", " ", " "])
        
        for piece in self.tabDesPieces:
            self.tableau[piece.coordY][piece.coordX] = piece.get_affichage()

    def is_saisie_correct(self, entree):
        if len(entree) > 2 or len(entree) == 1:
            return False
        cles_lettres = self.dicoLettreToPos.keys()
        cles_chiffres = self.dicoChiffreToPos.keys()
        if entree[0].upper() in cles_lettres and entree[1] in cles_chiffres:
            return True
        else:
            return False

    def bouger(self, couleur):
        move_ok = False
        if self.checkEchec(couleur):
            print("Tu es en echec !")
        while move_ok is False:
            while True:#dmd le coup et trouve quel pion est sur la case+gestion erreurs/triche
                try:
                    while True:#gere les erreurs de saisie des coordonnées
                        print("Quelles sont les coordonnées de la pièce que tu veux jouer ?\nTu peux entrer !help pour lister tous tes coups\nTu peux entrer afficher pour afficher le plateau")
                        pionAbouger = input()
                        if pionAbouger == "!help":
                            self.maj_pieces()
                            print(self.ensembleDesCoups(couleur))
                            print("\n")
                            continue
                        if pionAbouger == "afficher":
                            self.maj_pieces()
                            self.afficher()
                            continue
                        if self.is_saisie_correct(pionAbouger):
                            break 
                        else:
                            print("Erreur de saisie, réessaye ")
                
                    lettre = self.dicoLettreToPos[pionAbouger[0].upper()]
                    chiffre = self.dicoChiffreToPos[pionAbouger[1]]
                    pionSurCase = self.quelPionSurCetteCase(lettre, chiffre)

                    if pionSurCase.couleur != couleur:
                        print("Ce pion n'est pas a toi ! Recommence \n")
                    else:
                        break

                except AttributeError:
                    print("Il n y a rien sur cette case")
                except IndexError:
                    print("Erreur, réessaye")
            print(f"La liste des coups disponibles pour {pionSurCase.nom} en {pionAbouger} est :")

            print(self.mouvements_possibles(pionSurCase.get_coups_possibles(self.tableau)))
            
            
            while True:#gere erreur de saisie case de destination
                try:
                    print(f"Ou veux-tu déplacer {pionSurCase.nom} ? (exemple A5)")            
                    caseVoulu = input()
                    if self.is_saisie_correct(caseVoulu):
                        break 
                    else:
                        print("Erreur de saisie, réessaye ")
                except IndexError:
                    print("Erreur, réessaye")
            lettre_voulu = self.dicoLettreToPos[caseVoulu[0].upper()]
            chiffre_voulu = self.dicoChiffreToPos[caseVoulu[1]]
            backup_x_piece = pionSurCase.coordX
            backup_y_piece = pionSurCase.coordY
            
            #deplacement des autres pieces si possible on regarde si on doit en manger une
            for coups_possibles in pionSurCase.get_coups_possibles(self.tableau):
                #on va regarder si on est sur une piece avant de bouger pr pvr la suppr
                for pieces in self.tabDesPieces:#on regarde pour chaque piece
                    if (pieces.coordX == coups_possibles[0]) & (pieces.coordY == coups_possibles[1]) & (pionSurCase.couleur != pieces.couleur):#si les co d un piece correspondent à un coup possible & color != :
                        for possible_stroke in pionSurCase.get_coups_possibles(self.tableau):#pr chaque coup possible (anti cheat)
                            try:#on empeche les erreurs liés à la couleur pr les cases vides
                                if (lettre_voulu == possible_stroke[0]) & (chiffre_voulu == possible_stroke[1]) & (pionSurCase.couleur != self.quelPionSurCetteCase(possible_stroke[0], possible_stroke[1]).couleur):
                                    pieceAremove = self.quelPionSurCetteCase(lettre_voulu, chiffre_voulu)
                                    self.tabDesPieces.remove(pieceAremove)
                                    
                                    pionSurCase.coordX = lettre_voulu
                                    pionSurCase.coordY = chiffre_voulu
                                    self.maj_pieces()
                                    #promotion des pions
                                    if pionSurCase.affichage == "P" and pionSurCase.coordY == 0:
                                        newPion = self.promotion(pionSurCase, couleur)
                                        self.tabDesPieces.remove(pionSurCase)
                                        self.tabDesPieces.append(newPion)
                                        self.maj_pieces()
                                        pionSurCase = self.quelPionSurCetteCase(newPion.coordX, newPion.coordY)
                                    if pionSurCase.affichage == "p" and pionSurCase.coordY == 7:
                                        newPion = self.promotion(pionSurCase, couleur)
                                        self.tabDesPieces.remove(pionSurCase)
                                        self.tabDesPieces.append(newPion)
                                        self.maj_pieces()
                                        pionSurCase = self.quelPionSurCetteCase(newPion.coordX, newPion.coordY)

                                    if self.checkEchec(couleur):
                                        print("tu seras en echec si tu fais ça")
                                        pionSurCase.coordX = backup_x_piece
                                        pionSurCase.coordY = backup_y_piece
                                        self.maj_pieces()
                                        
                                    else:
                                        move_ok = True
                            except:
                                pass

                if lettre_voulu == coups_possibles[0] and chiffre_voulu == coups_possibles[1]:#si on est pas sur une autre piece : on se déplace normalement
                    pionSurCase.coordX = lettre_voulu
                    pionSurCase.coordY = chiffre_voulu
                    self.maj_pieces()
                    if pionSurCase.affichage == "P" and pionSurCase.coordY == 0:
                        newPion = self.promotion(pionSurCase, couleur)
                        self.tabDesPieces.remove(pionSurCase)
                        self.tabDesPieces.append(newPion)
                        self.maj_pieces()
                    if pionSurCase.affichage == "p" and pionSurCase.coordY == 7:
                        newPion = self.promotion(pionSurCase, couleur)
                        self.tabDesPieces.remove(pionSurCase)
                        self.tabDesPieces.append(newPion)
                        self.maj_pieces()

                    if self.checkEchec(couleur):
                        print("tu seras en echec si tu fais ça")
                        pionSurCase.coordX = backup_x_piece
                        pionSurCase.coordY = backup_y_piece
                        self.maj_pieces()
                        #promotion des pions
                    
                    else:
                        move_ok = True
                    break
            #annonce que coup impossible
            if move_ok is False:
                print("Coup impossible, réessaye")

    def quelPionSurCetteCase(self, x, y):
        for pieces in self.tabDesPieces:
            if pieces.coordX == x and pieces.coordY == y:
                return pieces
        
    def checkEchec(self, couleur):
        if couleur == "blanc":
            for pieces in self.tabDesPieces:
                if pieces.couleur != couleur:
                    for coups_possibles in pieces.get_coups_possibles(self.tableau):
                        if self.roiBlanc.coordX == coups_possibles[0] and self.roiBlanc.coordY == coups_possibles[1]:
                            return True
        elif couleur == "noir":
            for pieces in self.tabDesPieces:
                if pieces.couleur != couleur:
                    for coups_possibles in pieces.get_coups_possibles(self.tableau):
                        if self.roiNoir.coordX == coups_possibles[0] and self.roiNoir.coordY == coups_possibles[1]:
                            return True
        return False
                        
    def is_echec_et_mat(self, couleur):
        nb_coups_en_echec = 0
        if couleur == "blanc":
            for coups_possibles in self.roiBlanc.get_coups_possibles(self.tableau):#pr chaque CP du R
                coup_en_echec = 0
                for pieces in self.tabDesPieces:#on regarde chaq piece
                    if pieces.couleur != couleur:#on garde que les pieces adverses
                        for coups_pieces in pieces.get_coups_possibles(self.tableau):#si un coup de cette piece met le R en echec
                            if coup_en_echec == 0:
                                if coups_possibles[0] == coups_pieces[0] and coups_possibles[1] == coups_pieces[1]:
                                    #si le coup posisble du RoiNoir sera en echec:
                                    coup_en_echec = 1 #et la on doit changer de coup
                nb_coups_en_echec+=coup_en_echec
                

        elif couleur == "noir":
            for coups_possibles in self.roiNoir.get_coups_possibles(self.tableau):#pr chaque CP du R
                coup_en_echec = 0
                for pieces in self.tabDesPieces:#on regarde chaq piece
                    if pieces.couleur != couleur:#on garde que les pieces adverses
                        for coups_pieces in pieces.get_coups_possibles(self.tableau):#si un coup de cette piece met le R en echec
                            if coup_en_echec == 0:
                                if coups_possibles[0] == coups_pieces[0] and coups_possibles[1] == coups_pieces[1]:
                                    #si le coup posisble du RoiNoir sera en echec:
                                    coup_en_echec = 1 #et la on doit changer de coup
                nb_coups_en_echec+=coup_en_echec

        if nb_coups_en_echec == len(self.roiNoir.get_coups_possibles(self.tableau)):
            return True
        if nb_coups_en_echec == len(self.roiBlanc.get_coups_possibles(self.tableau)):
            return True

        return False

    def mouvements_possibles(self, tab):
        jolie_string = ""
        for coups in tab:
            lettre = str(self.PosToLettre[coups[0]])
            chiffre = str(self.PosToChiffre[coups[1]])
            jolie_string +=  lettre + chiffre + ", "
        return jolie_string

    def ensembleDesCoups(self,couleur):
        jolie_str2 = ""
        for pieces in self.tabDesPieces:
            if pieces.couleur == couleur and len(pieces.get_coups_possibles(self.tableau)) > 0:
                posX = self.PosToLettre[pieces.coordX]
                posY = self.PosToChiffre[pieces.coordY]
                jolie_str1 = pieces.nom + " en " + str(posX) + str(posY) + " peut aller en : "
                for coups in pieces.get_coups_possibles(self.tableau):
                    lettre = str(self.PosToLettre[coups[0]])
                    chiffre = str(self.PosToChiffre[coups[1]])
                    case = lettre + chiffre + ', '
                    jolie_str1 += case
                
                jolie_str2 += "\n" + jolie_str1
                jolie_str1 = ""
            
        return jolie_str2
  
    def promotion(self, pion, couleur):
        if couleur == "blanc":
            dicoPromotion = {1 : DameBlanc(pion.coordX, pion.coordY), 2 : TourBlanc(pion.coordX, pion.coordY), 3: CavalierBlanc(pion.coordX, pion.coordY), 4 : FouBlanc(pion.coordX, pion.coordY)}
            print("Promotion du Pion, comment voulez vous Promouvoir votre Pion ?")
            print("1) Dame\n2) Tour\n3) Cavalier \n4) Fou")
            choix = int(input())
            nouvellePiece = dicoPromotion[choix]
            print(nouvellePiece)

        if couleur == "noir":
            dicoPromotion = {1 : DameNoir(pion.coordX, pion.coordY), 2 : TourNoir(pion.coordX, pion.coordY), 3: CavalierNoir(pion.coordX, pion.coordY), 4 : FouNoir(pion.coordX, pion.coordY)}
            print("Promotion du Pion, comment voulez vous Promouvoir votre Pion ?")
            print("1) Dame\n2) Tour\n3) Cavalier \n4) Fou")
            choix = int(input())
            nouvellePiece = dicoPromotion[choix]
            print(nouvellePiece)

        return nouvellePiece

    def ia_random(self, couleur):

        while True:
            #en premier on choisit une piece random
            while True:#ici on while jusqua jouer une piece noire
                pieceAbouger = random.choice(self.tabDesPieces)
                if pieceAbouger.couleur == couleur and len(pieceAbouger.get_coups_possibles(self.tableau)) >0 :
                    break
            lettre = self.PosToLettre[pieceAbouger.coordX]
            chiffre = self.PosToChiffre[pieceAbouger.coordY]
            jolie_string= str(lettre) + str(chiffre)
            print(f"L'IA joue {pieceAbouger.nom} en {jolie_string}")

            #on va s'occuper de le placer sur une case aléatoire mtn
            coups_possibles = pieceAbouger.get_coups_possibles(self.tableau)#on a un tab de tuples (x,y)
            caseRandom = random.choice(coups_possibles)
            lettre = self.PosToLettre[caseRandom[0]]
            chiffre = self.PosToChiffre[caseRandom[1]]
            jolie_string= str(lettre) + str(chiffre)
            print(f"Il met {pieceAbouger.nom} en {jolie_string}")
            pieceAbouger.coordX = caseRandom[0]
            pieceAbouger.coordY = caseRandom[1]
            self.maj_pieces()
            break

    def deux_ia_random(self, couleur):
        
        while True:
            #en premier on choisit une piece random
            while True:#ici on while jusqua jouer une piece noire
                pieceAbouger = random.choice(self.tabDesPieces)
                if pieceAbouger.couleur == couleur and len(pieceAbouger.get_coups_possibles(self.tableau)) >0 :
                    break
            #on va s'occuper de le placer sur une case aléatoire mtn
            coups_possibles = pieceAbouger.get_coups_possibles(self.tableau)#on a un tab de tuples (x,y)
            caseRandom = random.choice(coups_possibles)
            pieceAbouger.coordX = caseRandom[0]
            pieceAbouger.coordY = caseRandom[1]
            self.maj_pieces()
            break

plateau = Plateau()
plateau.afficher()
listeJouerPossibles = [1,2,3]
while True:#on gere les erreurs de saisie
    print("Vous voulez jouer :")
    print("1) Contre un autre joueur\n2) Contre une Ia aléatoire\n3) 2 IA l'une contre l'autre 500 fois (pas 10 000 pour des soucis de temps et de performance)")
    
    try:
        jouer = int(input())
        if jouer in listeJouerPossibles:
            break
        else:
            print("Erreur, réessayer")
    except ValueError:
        print("Erreur, réessayer")


if jouer == 1:
    print("Vous jouer contre un joueur")
    while True:

        print("Au tour du joueur Blanc : \n")

        if plateau.is_echec_et_mat("blanc") is True and plateau.checkEchec("blanc") is True:
            print("Echec et mat pour le joueur Blanc")
            break
        plateau.bouger("blanc")
        plateau.maj_pieces()
        plateau.afficher()
        
        print("Au tour du joueur Noir : \n")
        
        if plateau.is_echec_et_mat("noir") is True and plateau.checkEchec("noir") is True:
            print("Echec et mat pour le joueur Noir")
            break
        plateau.bouger("noir")
        plateau.maj_pieces()
        plateau.afficher()

elif jouer == 2:
    print("Vous jouer contre une IA")
    print("Vous jouez les blancs, l'IA les noirs")
    while True:
        print("Au tour du joueur (Blanc) : \n")

        if plateau.is_echec_et_mat("blanc") is True and plateau.checkEchec("blanc") is True:
            print("Echec et mat pour le joueur (Blanc)")
            break
        plateau.bouger("blanc")
        plateau.maj_pieces()
        plateau.afficher()

        print("Au tour de l'IA (Noir) : \n")
        
        if plateau.is_echec_et_mat("noir") is True and plateau.checkEchec("noir") is True:
            print("Echec et mat pour l'IA")
            break
        plateau.ia_random("noir")
        plateau.maj_pieces()
        plateau.afficher()

elif jouer ==3:
    print("Deux IA vont jouer ensemble")
    victoireBlanc = 0
    victoireNoir = 0

    for i in range (500):
        plateau = Plateau()
        while True:
            #au tour de l ia blanc            

            if plateau.is_echec_et_mat("blanc") is True and plateau.checkEchec("blanc") is True:
                print(f"blanc : {victoireBlanc}")
                victoireNoir +=1
                break
            plateau.deux_ia_random("blanc")
            plateau.maj_pieces()

            #au tour de l ia noir            
            if plateau.is_echec_et_mat("noir") is True and plateau.checkEchec("noir") is True:
                print(f"noir : {victoireNoir}")
                victoireBlanc +=1
                break
            plateau.deux_ia_random("noir")
            plateau.maj_pieces()
    percentBlanc = victoireBlanc * 0.2
    percentNoir = victoireNoir * 0.2
    print(f"L'IA Blanche a gagné {victoireBlanc} fois soit {percentBlanc} % des parties")
    print(f"L'IA Noire a gagné {victoireNoir} fois soit {percentNoir} % des parties")