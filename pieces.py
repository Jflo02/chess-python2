class Piece :
    def __init__(self):
        self.nom = "piece"

    def get_affichage(self):
        return self.affichage


class PionBlanc(Piece):
    
    def __init__(self):
        self.affichage = "P"

    

class PionNoir(Piece):

    def __init__(self):
        self.affichage = "p"

class TourBlanc(Piece):

    def __init__(self):
        self.affichage = "T"

class TourNoir(Piece):

    def __init__(self):
        self.affichage = "t"

class CavalierBlanc(Piece):

    def __init__(self):
        self.affichage = "C"

class CavalierNoir(Piece):

    def __init__(self):
        self.affichage = "c"

class FouBlanc(Piece):

    def __init__(self):
        self.affichage = "F"

class FouNoir(Piece):

    def __init__(self):
        self.affichage = "f" 

class RoiBlanc(Piece):

    def __init__(self):
        self.affichage = "R"

class RoiNoir(Piece):

    def __init__(self):
        self.affichage = "r"

class DameBlanc(Piece):

    def __init__(self):
        self.affichage = "D"

class DameNoir(Piece):

    def __init__(self):
        self.affichage = "d" 