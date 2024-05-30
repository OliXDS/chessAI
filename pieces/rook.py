from pieces.base import Piece
from tools import OnBoard, Position
from botSetting import Config
from displayImages import GetSprite

class Rook(Piece):
    def __init__(self, position, colour):
        super().__init__(position, colour) # Calling the constructor of the parent class
        self.code = "r"
        self.value = 50 if colour == 0 else -50 # Assigning value based on colour
        self.sprite = GetSprite(self)
        self.previousMove = None
        self.pieceMap = []

    def GetMoves(self, board):
        moves, captures = self.VertHorzMoves(board) # calls VertHorzMoves()
        return moves, captures

    def VertHorzMoves(self, board):
        patterns = ((-1, 0), (1, 0), (0, 1), (0, -1))
        # Patterns for vertical and horizontal movement
        return self.GetPatternMoves(board, patterns)
