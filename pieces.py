class Piece :
    def __init__(self, coordX, coordY):
        self.nom = "pièce"
        self.coordX = coordX
        self.coordY = coordY
        self.affichage = " "

    def get_affichage(self):
        return self.affichage


class PionBlanc(Piece):
    
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Pion Blanc"
        self.affichage = "P"
    
    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        tuple_du_coup = (self.coordX, self.coordY+1)
        coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

    

class PionNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Pion Noir"
        self.affichage = "p"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        tuple_du_coup = (self.coordX, self.coordY-1)
        coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class TourBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Tour Blanche"
        self.affichage = "T"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        for i in range(7):
            coup=(i+1,self.coordY)
            coups_possibles.append(coup)
            coup=(self.coordX,i)
            coups_possibles.append(coup)
        return coups_possibles


class TourNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Tour Noire"
        self.affichage = "t"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        for i in range (8):
            tuple_du_coup = (self.coordX, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY)
            coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer
        

class CavalierBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Blanc"
        self.affichage = "C"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-2), (self.coordX+1, self.coordY-2), (self.coordX+2, self.coordY-1), (self.coordX+2, self.coordY+1), (self.coordX+1, self.coordY+2), (self.coordX-1, self.coordY+2), (self.coordX-2, self.coordY+1), (self.coordX-2, self.coordY-1)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class CavalierNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Noir"
        self.affichage = "c"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-2), (self.coordX+1, self.coordY-2), (self.coordX+2, self.coordY-1), (self.coordX+2, self.coordY+1), (self.coordX+1, self.coordY+2), (self.coordX-1, self.coordY+2), (self.coordX-2, self.coordY+1), (self.coordX-2, self.coordY-1)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class FouBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Fou Blanc"
        self.affichage = "F"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        for i in range (7):
            tuple_du_coup = (self.coordX-i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            #mtn on verifie la cohérence des resulats
            """ #marche pas bien
            for coups in coups_possibles:
                for case in coups:
                    if coups[0] < 0 or coups[0] > 7 or coups[1] < 0 or coups[1] > 7:
                        del coups_possibles[coups_possibles.index(coups)]
                        break
                    """
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer
        

class FouNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.affichage = "f" 

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        for i in range (7):
            tuple_du_coup = (self.coordX-i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer
        


class RoiBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Roi Blanc"
        self.affichage = "R"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-1), (self.coordX, self.coordY-1), (self.coordX+1, self.coordY-1), (self.coordX+1, self.coordY), (self.coordX+1, self.coordY+1), (self.coordX, self.coordY+1), (self.coordX-1, self.coordY+1), (self.coordX-1, self.coordY)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class RoiNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Roi Noir"
        self.affichage = "r"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-1), (self.coordX, self.coordY-1), (self.coordX+1, self.coordY-1), (self.coordX+1, self.coordY), (self.coordX+1, self.coordY+1), (self.coordX, self.coordY+1), (self.coordX-1, self.coordY+1), (self.coordX-1, self.coordY)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class DameBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Dame Blanche"
        self.affichage = "D"

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-1), (self.coordX, self.coordY-1), (self.coordX+1, self.coordY-1), (self.coordX+1, self.coordY), (self.coordX+1, self.coordY+1), (self.coordX, self.coordY+1), (self.coordX-1, self.coordY+1), (self.coordX-1, self.coordY)]
        
        for i in range (7):
            tuple_du_coup = (self.coordX, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY)
            coups_possibles.append(tuple_du_coup)

            tuple_du_coup = (self.coordX-i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
        
        
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class DameNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Dame Noire"
        self.affichage = "d" 

    def get_coups_possibles(self):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-1), (self.coordX, self.coordY-1), (self.coordX+1, self.coordY-1), (self.coordX+1, self.coordY), (self.coordX+1, self.coordY+1), (self.coordX, self.coordY+1), (self.coordX-1, self.coordY+1), (self.coordX-1, self.coordY)]
        
        for i in range (7):
            tuple_du_coup = (self.coordX, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY)
            coups_possibles.append(tuple_du_coup)

            tuple_du_coup = (self.coordX-i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY-i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX+i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
            tuple_du_coup = (self.coordX-i, self.coordY+i)
            coups_possibles.append(tuple_du_coup)
        
        
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer




