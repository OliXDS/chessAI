from pieces.base import Piece
from pieces.rook import Rook
from pieces.bishop import Bishop
from tools import OnBoard, Position
from botSetting import Config
from displayImages import GetSprite

class Queen(Bishop, Rook, Piece): # inheriting from Bishop, Rook, and Piece classes
    def __init__(self, position, colour):
        super().__init__(position, colour) # Call the initialization of inherited classes
        self.code = "q"
        self.value = 90 if colour == 0 else -90 # Value of the piece for evaluation
        self.sprite = GetSprite(self)
        self.previousMove = None
        self.pieceMap = []

    def GetMoves(self, board):
        diagonal_moves, diagonal_captures = self.DiagonalMoves(board)
        # Get diagonal moves and captures for the Queen
        r_moves, r_captures = self.VertHorzMoves(board)
        # Get vertical and horizontal moves and captures for the Queen
        moves = diagonal_moves + r_moves # Combine all moves
        captures = diagonal_captures + r_captures # Combine all captures
        return moves, captures
