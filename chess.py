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
        self.placer_pieces()  
        self.dicoLettreToPos = { "A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7 }
        self.dicoChiffreToPos = { "8" : 0, "7" : 1, "6" : 2, "5" : 3, "4" : 4, "3" : 5, "2" : 6, "1" : 7}
        self.dicoLettreToPiece = {"P" : "ton Pion", "T" : "ta Tour", "C" : "ton Cavalier", "D" : "ta Dame", "R" : "ton Roi", "F" : "ton Fou"}

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

    def placer_pieces(self):
        pionBlanc = PionBlanc()
        pionNoir = PionNoir()
        tourBlanc = TourBlanc()
        tourNoir = TourNoir()
        cavalierBlanc = CavalierBlanc()
        cavalierNoir = CavalierNoir()
        fouNoir = FouNoir()
        fouBlanc = FouBlanc()
        roiNoir = RoiNoir()
        roiBlanc = RoiBlanc()
        dameNoir = DameNoir()
        dameBlanc = DameBlanc()
        #on place les pions
        for i in range (0,8):
            self.tableau[1][i] = pionNoir.get_affichage()
            self.tableau[6][i] = pionBlanc.get_affichage()
        #on place les tours
        self.tableau[0][0] = self.tableau[0][7] = tourNoir.get_affichage()
        self.tableau[7][0] = self.tableau[7][7] = tourBlanc.get_affichage()
        #puis ainsi de suite
        self.tableau[0][1] = self.tableau[0][6] = cavalierNoir.get_affichage()
        self.tableau[7][1] = self.tableau[7][6] = cavalierBlanc.get_affichage()

        self.tableau[0][2] = self.tableau[0][5] = fouNoir.get_affichage()
        self.tableau[7][2] = self.tableau[7][5] = fouBlanc.get_affichage()

        self.tableau[0][3] = roiNoir.get_affichage()
        self.tableau[7][3] = roiBlanc.get_affichage()

        self.tableau[0][4] = dameNoir.get_affichage()
        self.tableau[7][4] = dameBlanc.get_affichage()

    def ask_coup(self):
        print("quelles sont les coordonnées du pion que tu veux jouer ?")
        pionAbouger = input()
        lettre = self.dicoLettreToPos[pionAbouger[0].upper()]
        chiffre = self.dicoChiffreToPos[pionAbouger[1]]
        pionSurCase = self.tableau[chiffre][lettre]
        print(f"Ou veux-tu déplacer {self.dicoLettreToPiece[pionSurCase.upper()]} ? (exemple A5)")
        caseVoulu = input()
        lettreVoulu = self.dicoLettreToPos[caseVoulu[0].upper()]
        chiffreVoulu = self.dicoChiffreToPos[caseVoulu[1]]



plateau = Plateau()
plateau.afficher()
plateau.ask_coup()