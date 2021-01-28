class Piece :
    def __init__(self, coordX, coordY):
        self.nom = "pièce"
        self.coordX = coordX
        self.coordY = coordY
        self.affichage = " "
        self.couleur = " "

    def get_affichage(self):
        return self.affichage

class PionBlanc(Piece):
    
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Pion Blanc"
        self.affichage = "P"
        self.couleur = "blanc"
    
    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        
        #si case devant est libre
        if self.coordY-1 >=0 and board[self.coordY-1][self.coordX] == " ":
            tuple_du_coup = (self.coordX, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        
        if self.coordY-1 >=0 and self.coordX+1 <8 and board[self.coordY-1][self.coordX+1] != " " and board[self.coordY-1][self.coordX+1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX+1, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        
        
        if self.coordY-1 >=0 and self.coordX-1 >=0 and board[self.coordY-1][self.coordX-1] != " " and board[self.coordY-1][self.coordX-1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX-1, self.coordY-1)
            coups_possibles.append(tuple_du_coup)

        if self.coordY == 6 and board[self.coordY-2][self.coordX] == " ":
            tuple_du_coup = (self.coordX, self.coordY-2)
            coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class PionNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Pion Noir"
        self.affichage = "p"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        tuple_du_coup = (self.coordX, self.coordY+1)
        if self.coordY+1 <8:
            if board[self.coordY+1][self.coordX] == " ":
                coups_possibles.append(tuple_du_coup)
        try:
            if board[self.coordY+1][self.coordX+1] != " " and self.coordX+1 <8 and board[self.coordY+1][self.coordX+1] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX+1, self.coordY+1)
        except:
            pass
        try:
            if board[self.coordY+1][self.coordX-1] != " " and self.coordX-1 >=0 and board[self.coordY+1][self.coordX-1] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX-1, self.coordY+1)
                coups_possibles.append(tuple_du_coup)
        except:
            pass
        if self.coordY == 1 and board[self.coordY+2][self.coordX] == " ":
            tuple_du_coup = (self.coordX, self.coordY+2)
            coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class TourBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Tour Blanche"
        self.affichage = "T"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []

        #coup de la tour en haut
        for i in range(1, 8):
            
            if self.coordY-i >=0:
                if board[self.coordY-i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY-i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY-i][self.coordX] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX, self.coordY-i)
                        coups_possibles.append(coup)
                    break
                

        #coup de la tour en bas
        for i in range(1, 8):
            if self.coordY+i <8:
                if board[self.coordY+i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY+i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY+i][self.coordX] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX, self.coordY+i)
                        coups_possibles.append(coup)
                    break
            

        #coup de la tour a gauche
        for i in range(1, 8):  
            if self.coordX-i >=0:
                if board[self.coordY][self.coordX-i] == " ":
                    coup = (self.coordX-i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX-i, self.coordY)
                        coups_possibles.append(coup)
                    break
    
        #coup de la tour a droite
        for i in range(1, 8):
            if self.coordX+i <8:
                if board[self.coordY][self.coordX+i] == " ":
                    coup = (self.coordX+i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX+i, self.coordY)
                        coups_possibles.append(coup)
                    break
            
        return coups_possibles

class TourNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Tour Noire"
        self.affichage = "t"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []

        #coup de la tour en haut
        for i in range(1, 8):
            
            if self.coordY-i >=0:
                if board[self.coordY-i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY-i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY-i][self.coordX] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX, self.coordY-i)
                        coups_possibles.append(coup)
                    break
                

        #coup de la tour en bas
        for i in range(1, 8):
            if self.coordY+i <8:
                if board[self.coordY+i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY+i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY+i][self.coordX] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX, self.coordY+i)
                        coups_possibles.append(coup)
                    break
            

        #coup de la tour a gauche
        for i in range(1, 8):  
            if self.coordX-i >=0:
                if board[self.coordY][self.coordX-i] == " ":
                    coup = (self.coordX-i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX-i, self.coordY)
                        coups_possibles.append(coup)
                    break
    
        #coup de la tour a droite
        for i in range(1, 8):
            if self.coordX+i <8:
                if board[self.coordY][self.coordX+i] == " ":
                    coup = (self.coordX+i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX+i, self.coordY)
                        coups_possibles.append(coup)
                    break
            
        return coups_possibles

class CavalierBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Blanc"
        self.affichage = "C"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        if self.coordX-1 >= 0 and self.coordY-2 >=0 and board[self.coordY-2][self.coordX-1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX-1, self.coordY-2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+1 <8 and self.coordY-2 >=0 and board[self.coordY-2][self.coordX+1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX+1, self.coordY-2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+2 <8 and self.coordY-1 >=0 and board[self.coordY-1][self.coordX+2] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX+2, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+2 <8 and self.coordY+1 <8 and board[self.coordY+1][self.coordX+2] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX+2, self.coordY+1)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+1 <8 and self.coordY+2 <8 and board[self.coordY+2][self.coordX+1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX+1, self.coordY+2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX-1 >=0 and self.coordY+2 <8 and board[self.coordY+2][self.coordX-1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX-1, self.coordY+2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX-2 >=0 and self.coordY+1 <8 and board[self.coordY+1][self.coordX-2] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX-2, self.coordY+1)
            coups_possibles.append(tuple_du_coup)
        if self.coordX-2 >=0 and self.coordY-1 >=0 and board[self.coordY-1][self.coordX-2] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX-2, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class CavalierNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Noir"
        self.affichage = "c"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        if self.coordX-1 >= 0 and self.coordY-2 >=0 and board[self.coordY-2][self.coordX-1] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX-1, self.coordY-2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+1 <8 and self.coordY-2 >=0 and board[self.coordY-2][self.coordX+1] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX+1, self.coordY-2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+2 <8 and self.coordY-1 >=0 and board[self.coordY-1][self.coordX+2] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX+2, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+2 <8 and self.coordY+1 <8 and board[self.coordY+1][self.coordX+2] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX+2, self.coordY+1)
            coups_possibles.append(tuple_du_coup)
        if self.coordX+1 <8 and self.coordY+2 <8 and board[self.coordY+2][self.coordX+1] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX+1, self.coordY+2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX-1 >=0 and self.coordY+2 <8 and board[self.coordY+2][self.coordX-1] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX-1, self.coordY+2)
            coups_possibles.append(tuple_du_coup)
        if self.coordX-2 >=0 and self.coordY+1 <8 and board[self.coordY+1][self.coordX-2] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX-2, self.coordY+1)
            coups_possibles.append(tuple_du_coup)
        if self.coordX-2 >=0 and self.coordY-1 >=0 and board[self.coordY-1][self.coordX-2] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX-2, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class FouBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Fou Blanc"
        self.affichage = "F"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []

        #en haut a gauche
        for i in range (1,8):

            if self.coordX-i >= 0 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX-i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

            
        #en haut a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX+i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX+i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a gauche
        for i in range (1,8):
            if self.coordX-i >=0 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX-i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer
        
class FouNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Fou Noir"
        self.affichage = "f"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []

        #en haut a gauche
        for i in range (1,8):

            if self.coordX-i >= 0 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX-i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

            
        #en haut a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX+i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX+i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a gauche
        for i in range (1,8):
            if self.coordX-i >=0 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX-i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer
        
class RoiBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Roi Blanc"
        self.affichage = "R"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []        
        
        if self.coordX-1 >=0 and board[self.coordY][self.coordX-1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX-1, self.coordY)
            coups_possibles.append(tuple_du_coup)
        if self.coordY+1 <8 and self.coordX-1 >=0 and board[self.coordY+1][self.coordX-1] not in ["P", "T", "C", "F", "R", "D"]:
                tuple_du_coup = (self.coordX-1, self.coordY+1)
                coups_possibles.append(tuple_du_coup)
        if self.coordY-1 >=0 and self.coordX-1 >=0 and board[self.coordY-1][self.coordX-1] not in ["P", "T", "C", "F", "R", "D"]:
                tuple_du_coup = (self.coordX-1, self.coordY-1)
                coups_possibles.append(tuple_du_coup)

        if self.coordX+1 <8 and self.coordX+1 <8 and board[self.coordY][self.coordX+1] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX+1, self.coordY)
            coups_possibles.append(tuple_du_coup)
        if self.coordY-1 >=0 and self.coordX+1 <8 and board[self.coordY-1][self.coordX+1] not in ["P", "T", "C", "F", "R", "D"]:
                tuple_du_coup = (self.coordX+1, self.coordY-1)
                coups_possibles.append(tuple_du_coup)
        if self.coordY+1 <8 and self.coordX+1 <8 and board[self.coordY+1][self.coordX+1] not in ["P", "T", "C", "F", "R", "D"]:
                tuple_du_coup = (self.coordX+1, self.coordY+1)
                coups_possibles.append(tuple_du_coup)

        if self.coordY-1 >=0 and board[self.coordY-1][self.coordX] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        if self.coordY+1 <8 and board[self.coordY+1][self.coordX] not in ["P", "T", "C", "F", "R", "D"]:
            tuple_du_coup = (self.coordX, self.coordY+1)
            coups_possibles.append(tuple_du_coup) 

        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class RoiNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Roi Noir"
        self.affichage = "r"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []        
        
        if self.coordX-1 >=0 and board[self.coordY][self.coordX-1] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX-1, self.coordY)
            coups_possibles.append(tuple_du_coup)
        if self.coordY+1 <8 and self.coordX-1 >=0 and board[self.coordY+1][self.coordX-1] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX-1, self.coordY+1)
                coups_possibles.append(tuple_du_coup)
        if self.coordY-1 >=0 and self.coordX-1 >=0 and board[self.coordY-1][self.coordX-1] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX-1, self.coordY-1)
                coups_possibles.append(tuple_du_coup)

        if self.coordX+1 <8 and self.coordX+1 <8 and board[self.coordY][self.coordX+1] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX+1, self.coordY)
            coups_possibles.append(tuple_du_coup)
        if self.coordY-1 >=0 and self.coordX+1 <8 and board[self.coordY-1][self.coordX+1] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX+1, self.coordY-1)
                coups_possibles.append(tuple_du_coup)
        if self.coordY+1 <8 and self.coordX+1 <8 and board[self.coordY+1][self.coordX+1] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX+1, self.coordY+1)
                coups_possibles.append(tuple_du_coup)

        if self.coordY-1 >=0 and board[self.coordY-1][self.coordX] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX, self.coordY-1)
            coups_possibles.append(tuple_du_coup)
        if self.coordY+1 <8 and board[self.coordY+1][self.coordX] not in ["p", "t", "c", "f", "r", "d"]:
            tuple_du_coup = (self.coordX, self.coordY+1)
            coups_possibles.append(tuple_du_coup) 

        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

class DameBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Dame Blanche"
        self.affichage = "D"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []        
        
        #coup du fou blanc
        #en haut a gauche
        for i in range (1,8):

            if self.coordX-i >= 0 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX-i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

            
        #en haut a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX+i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX+i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a gauche
        for i in range (1,8):
            if self.coordX-i >=0 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                        tuple_du_coup = (self.coordX-i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        

        #coup de la tour blanche
        #coup de la tour en haut
        for i in range(1, 8):
            
            if self.coordY-i >=0:
                if board[self.coordY-i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY-i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY-i][self.coordX] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX, self.coordY-i)
                        coups_possibles.append(coup)
                    break
                

        #coup de la tour en bas
        for i in range(1, 8):
            if self.coordY+i <8:
                if board[self.coordY+i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY+i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY+i][self.coordX] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX, self.coordY+i)
                        coups_possibles.append(coup)
                    break
            

        #coup de la tour a gauche
        for i in range(1, 8):  
            if self.coordX-i >=0:
                if board[self.coordY][self.coordX-i] == " ":
                    coup = (self.coordX-i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX-i, self.coordY)
                        coups_possibles.append(coup)
                    break
    
        #coup de la tour a droite
        for i in range(1, 8):
            if self.coordX+i <8:
                if board[self.coordY][self.coordX+i] == " ":
                    coup = (self.coordX+i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX+i, self.coordY)
                        coups_possibles.append(coup)
                    break

        return coups_possibles

class DameNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Dame Noire"
        self.affichage = "d" 
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        #coup du fou noir
        #en haut a gauche
        for i in range (1,8):

            if self.coordX-i >= 0 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX-i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

            
        #en haut a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY-i >=0:
                if board[self.coordY-i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY-i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY-i][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX+i, self.coordY-i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a droite
        for i in range (1,8):
            if self.coordX+i < 8 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX+i] == " ":
                    tuple_du_coup = (self.coordX+i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX+i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break

        #en bas a gauche
        for i in range (1,8):
            if self.coordX-i >=0 and self.coordY+i <8:
                if board[self.coordY+i][self.coordX-i] == " ":
                    tuple_du_coup = (self.coordX-i, self.coordY+i)
                    coups_possibles.append(tuple_du_coup)
                else:
                    if board[self.coordY+i][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                        tuple_du_coup = (self.coordX-i, self.coordY+i)
                        coups_possibles.append(tuple_du_coup)
                    break
        
        
        #coup de la tour noire
        #coup de la tour en haut
        for i in range(1, 8):
            
            if self.coordY-i >=0:
                if board[self.coordY-i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY-i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY-i][self.coordX] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX, self.coordY-i)
                        coups_possibles.append(coup)
                    break
                

        #coup de la tour en bas
        for i in range(1, 8):
            if self.coordY+i <8:
                if board[self.coordY+i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY+i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY+i][self.coordX] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX, self.coordY+i)
                        coups_possibles.append(coup)
                    break
            

        #coup de la tour a gauche
        for i in range(1, 8):  
            if self.coordX-i >=0:
                if board[self.coordY][self.coordX-i] == " ":
                    coup = (self.coordX-i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX-i, self.coordY)
                        coups_possibles.append(coup)
                    break
    
        #coup de la tour a droite
        for i in range(1, 8):
            if self.coordX+i <8:
                if board[self.coordY][self.coordX+i] == " ":
                    coup = (self.coordX+i, self.coordY)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX+i, self.coordY)
                        coups_possibles.append(coup)
                    break
        
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer




