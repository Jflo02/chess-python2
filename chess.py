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

        self.roiBlanc = RoiBlanc(0, 4)#A REMETTRE EN 3,7 !!!!

        self.dameBlanc = DameBlanc(4, 7)
        
        self.pionNoir1 = PionNoir(1, 2)#A REMETTRE EN 0,1 !!!!
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
        while move_ok is False:
            while True:#dmd le coup et trouve quel pion est sur la case+gestion erreurs/triche
                while True:#gere les erreurs de saisie des coordonnées
                    print("Quelles sont les coordonnées de la pièce que tu veux jouer ?")
                    pionAbouger = input()
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
            print("MISE EN PLACE ton pion peut aller en :")
            print(pionSurCase.get_coups_possibles(self.tableau))

            
            while True:#gere erreur de saisie case de destination
                print(f"Ou veux-tu déplacer {pionSurCase.nom} ? (exemple A5)")            
                caseVoulu = input()
                if self.is_saisie_correct(caseVoulu):
                    break 
                else:
                    print("Erreur de saisie, réessaye ")
            lettre_voulu = self.dicoLettreToPos[caseVoulu[0].upper()]
            chiffre_voulu = self.dicoChiffreToPos[caseVoulu[1]]

            #pion blanc manger en diagonale
            if pionSurCase.affichage == "P":
                if chiffre_voulu == pionSurCase.coordY-1:#useless
                    if (lettre_voulu == pionSurCase.coordX+1) or (lettre_voulu == pionSurCase.coordX-1):
                        for pieces in self.tabDesPieces:
                            if (pieces.coordX == lettre_voulu) and pieces.coordY == chiffre_voulu:
                                if (pionSurCase.couleur != pieces.couleur):
                                    try:
                                        pieceAremove = self.quelPionSurCetteCase(lettre_voulu, chiffre_voulu)
                                        self.tabDesPieces.remove(pieceAremove)
                                        pionSurCase.coordX = lettre_voulu
                                        pionSurCase.coordY = chiffre_voulu
                                        break
                                    except:
                                        pass
            #pion noir manger en diagonale
            if pionSurCase.affichage == "p":
                if chiffre_voulu == pionSurCase.coordY+1:#useless
                    if (lettre_voulu == pionSurCase.coordX+1) or (lettre_voulu == pionSurCase.coordX-1):
                        for pieces in self.tabDesPieces:
                            if (pieces.coordX == lettre_voulu) and pieces.coordY == chiffre_voulu:
                                if (pionSurCase.couleur != pieces.couleur):
                                    try:
                                        pieceAremove = self.quelPionSurCetteCase(lettre_voulu, chiffre_voulu)
                                        self.tabDesPieces.remove(pieceAremove)
                                        pionSurCase.coordX = lettre_voulu
                                        pionSurCase.coordY = chiffre_voulu
                                        break
                                    except:
                                        pass

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
                                    move_ok = True
                            except:
                                pass

                if lettre_voulu == coups_possibles[0] and chiffre_voulu == coups_possibles[1]:#si on est pas sur une autre piece : on se déplace normalement
                    pionSurCase.coordX = lettre_voulu
                    pionSurCase.coordY = chiffre_voulu
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
            print("Je test la condition d echec")
            for pieces in self.tabDesPieces:
                if pieces.couleur != couleur:
                    for coups_possibles in pieces.get_coups_possibles(self.tableau):
                        if self.roiBlanc.coordX == coups_possibles[0] and self.roiBlanc.coordY == coups_possibles[1]:
                            print("Le roi blanc est en echec")
                            return True
        elif couleur == "noir":
            print("Je test la condition d echec")
            for pieces in self.tabDesPieces:
                if pieces.couleur != couleur:
                    for coups_possibles in pieces.get_coups_possibles(self.tableau):
                        if self.roiNoir.coordX == coups_possibles[0] and self.roiNoir.coordY == coups_possibles[1]:
                            print("Le roi noir est en echec")
                            return True
                        


plateau = Plateau()
plateau.afficher()

while True:
    print("Au tour du joueur Blanc : \n")

    
    plateau.checkEchec("blanc")
    plateau.bouger("blanc")
    plateau.maj_pieces()
    plateau.afficher()
    

    print("Au tour du joueur Noir : \n")

    plateau.bouger("noir")
    plateau.maj_pieces()
    plateau.afficher()
    
