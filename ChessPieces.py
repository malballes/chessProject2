from King import King
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen

class ChessPieces:
    
    def __init__(self, isWhite):
        if isWhite:
            self.pieces = [King(4,7,isWhite)]
            for i in range(8):
                self.pieces.append(Pawn(i,6,isWhite))
            self.pieces.append(Rook(0,7,isWhite))
            self.pieces.append(Rook(7,7,isWhite))
            self.pieces.append(Bishop(5,7,isWhite))
            self.pieces.append(Bishop(2,7,isWhite))
            self.pieces.append(Knight(6,7,isWhite))
            self.pieces.append(Knight(1,7,isWhite))
            self.pieces.append(Queen(3,7,isWhite))
        else:
            self.pieces = [King(4,0,isWhite)]
            for i in range(8):
                self.pieces.append(Pawn(i,1,isWhite))
            self.pieces.append(Rook(0,0,isWhite))
            self.pieces.append(Rook(7,0,isWhite))
            self.pieces.append(Bishop(5,0,isWhite))
            self.pieces.append(Bishop(2,0,isWhite))
            self.pieces.append(Knight(6,0,isWhite))
            self.pieces.append(Knight(1,0,isWhite))
            self.pieces.append(Queen(3,0,isWhite))




