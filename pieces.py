class Piece :
    def __init__(self):
        self.nom = "piece"

    def get_affichage(self):
        return self.affichage


class PionBlanc(Piece):
    
    def __init__(self):
        self.affichage = "♟"

class PionNoir(Piece):

    def __init__(self):
        self.affichage = "♙"

class TourBlanc(Piece):

    def __init__(self):
        self.affichage = "♜"

class TourNoir(Piece):

    def __init__(self):
        self.affichage = "♖"

class CavalierBlanc(Piece):

    def __init__(self):
        self.affichage = "♞"

class CavalierNoir(Piece):

    def __init__(self):
        self.affichage = "♘"

class FouBlanc(Piece):

    def __init__(self):
        self.affichage = "♝"

class FouNoir(Piece):

    def __init__(self):
        self.affichage = "♗" 

class RoiBlanc(Piece):

    def __init__(self):
        self.affichage = "♚"

class RoiNoir(Piece):

    def __init__(self):
        self.affichage = "♔"

class DameBlanc(Piece):

    def __init__(self):
        self.affichage = "♛"

class DameNoir(Piece):

    def __init__(self):
        self.affichage = "♕" 