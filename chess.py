#4 classes
#une class plateau
#ds celui ci un max de methodes utilitaires ( l afficher ...)
#
#Une classe (abstraite ou pas) qui représente une piece
#test pr le commit kj
import random
import time
from pieces import *

class Plateau:
    def __init__(self):
        self.tableau = []
        self.create()
        # self.placer_pieces()     

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




plateau = Plateau()
plateau.placer_pieces()
plateau.afficher()
