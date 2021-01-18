class Piece :
    def __init__(self, coordX, coordY):
        self.nom = "pièce"
        self.coordX = coordX
        self.coordY = coordY

    def get_affichage(self):
        return self.affichage


class PionBlanc(Piece):
    
    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Pion Blanc"
        self.affichage = "P"

    

class PionNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Pion Noir"
        self.affichage = "p"

class TourBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Tour Blanche"
        self.affichage = "T"

class TourNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Tour Noire"
        self.affichage = "t"

class CavalierBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Blanc"
        self.affichage = "C"

class CavalierNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Cavalier Noir"
        self.affichage = "c"

class FouBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.nom = "Fou Blanc"
        self.affichage = "F"

class FouNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.affichage = "f" 

class RoiBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.affichage = "R"

class RoiNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.affichage = "r"

class DameBlanc(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.affichage = "D"

class DameNoir(Piece):

    def __init__(self, coordX, coordY):
        super().__init__(coordX, coordY)
        self.affichage = "d" 


testpion = PionBlanc(0, 1)

print(testpion.nom)