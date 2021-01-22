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
        tuple_du_coup = (self.coordX, self.coordY-1)
        if board[self.coordY-1][self.coordX] == " ":
            coups_possibles.append(tuple_du_coup)
        try:
            if board[self.coordY-1][self.coordX+1] != " ":
                tuple_du_coup = (self.coordX+1, self.coordY-1)
                coups_possibles.append(tuple_du_coup)
        except:
            pass
        try:
            if board[self.coordY-1][self.coordX-1] != " ":
                tuple_du_coup = (self.coordX-1, self.coordY-1)
                coups_possibles.append(tuple_du_coup)
        except:
            pass
        if self.coordY == 6:
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
        if board[self.coordY+1][self.coordX] == " ":
            coups_possibles.append(tuple_du_coup)
        try:
            if board[self.coordY+1][self.coordX+1] != " " and self.coordX+1 <8 and board[self.coordY+i][self.coordX] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX+1, self.coordY+1)
        except:
            pass
        try:
            if board[self.coordY+1][self.coordX-1] != " " and self.coordX-1 >=0 and board[self.coordY+i][self.coordX] not in ["p", "t", "c", "f", "r", "d"]:
                tuple_du_coup = (self.coordX-1, self.coordY+1)
                coups_possibles.append(tuple_du_coup)
        except:
            pass
        if self.coordY == 1:
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
            try:
                if board[self.coordY-i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY-i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY-i][self.coordX] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX, self.coordY-i)
                        coups_possibles.append(coup)
                    break
            except:
                pass

        #coup de la tour en bas
        for i in range(1, 8):
            try:
                if board[self.coordY+i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY+i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY+i][self.coordX] in ["p", "t", "c", "f", "r", "d"]:
                        coup = (self.coordX, self.coordY+i)
                        coups_possibles.append(coup)
                    break
            except:
                pass

        #coup de la tour a gauche
        for i in range(1, 8):
            try:
                if self.coordX-i >=0:
                    if board[self.coordY][self.coordX-i] == " ":
                        coup = (self.coordX-i, self.coordY)
                        coups_possibles.append(coup)
                    else:
                        if board[self.coordY][self.coordX-i] in ["p", "t", "c", "f", "r", "d"]:
                            coup = (self.coordX-i, self.coordY)
                            coups_possibles.append(coup)
                        break
            except:
                pass

        #coup de la tour a droite
        for i in range(1, 8):
            try:
                if self.coordX-i <=7:
                    if board[self.coordY][self.coordX+i] == " ":
                        coup = (self.coordX+i, self.coordY)
                        coups_possibles.append(coup)
                    else:
                        if board[self.coordY][self.coordX+i] in ["p", "t", "c", "f", "r", "d"]:
                            coup = (self.coordX+i, self.coordY)
                            coups_possibles.append(coup)
                        break
            except:
                pass
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
            try:
                if self.coordY-i >=0:
                    if board[self.coordY-i][self.coordX] == " ":
                        coup = (self.coordX, self.coordY-i)
                        coups_possibles.append(coup)
                    else:
                        if board[self.coordY-i][self.coordX] in ["P", "T", "C", "F", "R", "D"]:
                            coup = (self.coordX, self.coordY-i)
                            coups_possibles.append(coup)
                        break
            except:
                pass

        #coup de la tour derriere elle
        for i in range(1, 8):
            try:
                if board[self.coordY+i][self.coordX] == " ":
                    coup = (self.coordX, self.coordY+i)
                    coups_possibles.append(coup)
                else:
                    if board[self.coordY+i][self.coordX] in ["P", "T", "C", "F", "R", "D"]:
                        coup = (self.coordX, self.coordY+i)
                        coups_possibles.append(coup)
                    break
            except:
                pass

        #coup de la tour a gauche
        for i in range(1, 8):
            try:
                if self.coordX-i >=0:
                    if board[self.coordY][self.coordX-i] == " ":
                        coup = (self.coordX-i, self.coordY)
                        coups_possibles.append(coup)
                    else:
                        if board[self.coordY][self.coordX-i] in ["P", "T", "C", "F", "R", "D"]:
                            coup = (self.coordX-i, self.coordY)
                            coups_possibles.append(coup)
                        break
            except:
                pass

        #coup de la tour a droite
        for i in range(1, 8):
            try:
                if self.coordX-i <=7:
                    if board[self.coordY][self.coordX+i] == " ":
                        coup = (self.coordX+i, self.coordY)
                        coups_possibles.append(coup)
                    else:
                        if board[self.coordY][self.coordX+i] in ["P", "T", "C", "F", "R", "D"]:
                            coup = (self.coordX+i, self.coordY)
                            coups_possibles.append(coup)
                        break
            except:
                pass
        return coups_possibles

class CavalierBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Blanc"
        self.affichage = "C"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-2), (self.coordX+1, self.coordY-2), (self.coordX+2, self.coordY-1), (self.coordX+2, self.coordY+1), (self.coordX+1, self.coordY+2), (self.coordX-1, self.coordY+2), (self.coordX-2, self.coordY+1), (self.coordX-2, self.coordY-1)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class CavalierNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Noir"
        self.affichage = "c"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-2), (self.coordX+1, self.coordY-2), (self.coordX+2, self.coordY-1), (self.coordX+2, self.coordY+1), (self.coordX+1, self.coordY+2), (self.coordX-1, self.coordY+2), (self.coordX-2, self.coordY+1), (self.coordX-2, self.coordY-1)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class FouBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Fou Blanc"
        self.affichage = "F"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
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
        self.nom = "Fou Noir"
        self.affichage = "f"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
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
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-1), (self.coordX, self.coordY-1), (self.coordX+1, self.coordY-1), (self.coordX+1, self.coordY), (self.coordX+1, self.coordY+1), (self.coordX, self.coordY+1), (self.coordX-1, self.coordY+1), (self.coordX-1, self.coordY)]
        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer


class RoiNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Roi Noir"
        self.affichage = "r"
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
        coups_possibles = []
        coups_possibles=[(self.coordX-1, self.coordY-1), (self.coordX, self.coordY-1), (self.coordX+1, self.coordY-1), (self.coordX+1, self.coordY), (self.coordX+1, self.coordY+1), (self.coordX, self.coordY+1), (self.coordX-1, self.coordY+1), (self.coordX-1, self.coordY)]
        
        indice_liste = 0
        for coups in coups_possibles:
            print(coups)
            #on le décompose le tuple pr recup x et y
            x = coups[0]
            y = coups[1]
            if (x < 0) or (x > 7) or (y < 0) or (y > 7):
                coups_possibles.pop(indice_liste)
                indice_liste += 1
        print("debuuuug")
        print(coups_possibles)
                

                    

        return coups_possibles #on return un tableau avec dans chaque case le tuple (x,y) dans lequel il a le droit de se deplacer

    

class DameBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Dame Blanche"
        self.affichage = "D"
        self.couleur = "blanc"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
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
        self.couleur = "noir"

    def get_coups_possibles(self, board):#on veut connaitre vers quelle position peut se déplacer la piece
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




