from pieces.base import Piece
from tools import OnBoard, Position
from botSetting import Config
from displayImages import GetSprite

class Bishop(Piece):
    def __init__(self, position, colour):
        super().__init__(position, colour)
        self.code = "b" # will be used for sprite method
        self.value = 30 if colour == 0 else -30
        self.sprite = GetSprite(self)
        self.previousMove = None
        self.pieceMap = []

    def GetMoves(self, board):
        moves, captures = self.DiagonalMoves(board)
        # used below to locate moves
        return moves, captures

    def DiagonalMoves(self, board):
        patterns = ((-1, -1), (1, 1), (1, -1), (-1, 1))
        # diagonal pattern above
        moves, captures = self.GetPatternMoves(board, patterns)
        return moves, captures
