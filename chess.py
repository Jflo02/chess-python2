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
        self.pionBlanc1 = PionBlanc(0, 1)
        self.pionBlanc2 = PionBlanc(1, 1)
        self.pionBlanc3 = PionBlanc(2, 1)
        self.pionBlanc4 = PionBlanc(3, 1)
        self.pionBlanc5 = PionBlanc(4, 1)
        self.pionBlanc6 = PionBlanc(5, 1)
        self.pionBlanc7 = PionBlanc(6, 1)
        self.pionBlanc8 = PionBlanc(7, 1)

        self.tourBlanc1 = TourBlanc(0, 0)
        self.tourBlanc2 = TourBlanc(7, 0)
        
        self.cavalierBlanc1 = CavalierBlanc(1, 0)
        self.cavalierBlanc2 = CavalierBlanc(6, 0)
        
        self.fouBlanc1 = FouBlanc(2, 0)
        self.fouBlanc2 = FouBlanc(5, 0)

        self.roiBlanc = RoiBlanc(3, 0)

        self.dameBlanc = DameBlanc(4, 0)
        
        self.pionNoir1 = PionNoir(0, 6)
        self.pionNoir2 = PionNoir(1, 6)
        self.pionNoir3 = PionNoir(2, 6)
        self.pionNoir4 = PionNoir(3, 6)
        self.pionNoir5 = PionNoir(4, 6)
        self.pionNoir6 = PionNoir(5, 6)
        self.pionNoir7 = PionNoir(6, 6)
        self.pionNoir8 = PionNoir(7, 6)
        
        self.tourNoir1 = TourNoir(0, 7)
        self.tourNoir2 = TourNoir(7, 7)
        
        self.cavalierNoir1 = CavalierNoir(1, 7)
        self.cavalierNoir2 = CavalierNoir(6, 7)

        self.fouNoir1 = FouNoir(2, 7)
        self.fouNoir2 = FouNoir(5, 7)
        
        self.roiNoir = RoiNoir(3, 7)
        
        self.dameNoir = DameNoir(4, 7)
        
         
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


    def ask_coup(self):
        print("quelles sont les coordonnées du pion que tu veux jouer ?")
        pionAbouger = input()
        lettre = self.dicoLettreToPos[pionAbouger[0].upper()]
        chiffre = self.dicoChiffreToPos[pionAbouger[1]]
        pionSurCase = self.quelPionSurCetteCase(lettre, chiffre)
        #on va afficher les cases sur lesquels on peut aller
        """#on verra ça + tard
        print(f"{pionSurCase.nom} peut aller en : ")
        coup_a_afficher = []
        for coups in pionSurCase.get_coups_possibles():
            lettre_coup = self.PosToLettre[coups[0]]
            chiffre_coup = self.PosToChiffre[coups[1]]
            tuple_coup_a_afficher = (lettre_coup, chiffre_coup)
            coup_a_afficher.append(tuple_coup_a_afficher)
        print(coup_a_afficher)
        """
        print(f"Ou veux-tu déplacer {pionSurCase.nom} ? (exemple A5)")
        
        caseVoulu = input()

        lettre_voulu = self.dicoLettreToPos[caseVoulu[0].upper()]
        chiffre_voulu = self.dicoChiffreToPos[caseVoulu[1]]
        while True:
            for coups_possibles in pionSurCase.get_coups_possibles():#ici on regarde si la piece peut aller la ou on le veut
                if lettre_voulu == coups_possibles[0] and chiffre_voulu == coups_possibles[1]:#si oui on la met
                    pionSurCase.coordX = lettre_voulu
                    pionSurCase.coordY = chiffre_voulu
                    break
            break
                

    def quelPionSurCetteCase(self, x, y):
        for pieces in self.tabDesPieces:
            if pieces.coordX == x and pieces.coordY == y:
                break
        return pieces #on return l'indoce de l'objet qu'on souhaite



plateau = Plateau()
plateau.afficher()

for i in range (10):
    plateau.ask_coup()
    plateau.maj_pieces()
    plateau.afficher()
