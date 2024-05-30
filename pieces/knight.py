from pieces.base import Piece
from tools import OnBoard, Position
from botSetting import Config
from displayImages import GetSprite

class Knight(Piece): # inheriting from Piece class
    def __init__(self, position, colour):
        super().__init__(position, colour) # Calling constructor of the superclass Piece
        self.code = "n"
        self.value = 30 if colour == 0 else -30
        self.sprite = GetSprite(self)
        self.previousMove = None
        self.pieceMap = []

    # Method to calculate available moves for the Knight
    def GetMoves(self, board):
        moves = []
        captures = []

        for i in range(-2, 3): # Looping through possible offsets for Knight's moves
            if i != 0: # Ensuring that i is not 0
                for j in range(-2, 3):
                    if j != 0: # Ensuring that j is not 0
                        dx = self.position.x + i
                        dy = self.position.y + j
                        temp = Position(dx, dy)
                        if abs(i) != abs(j) and OnBoard(temp): # Checking if the move is valid for a Knight
                            if board.grid[dx][dy] == None: # Checking if the destination is empty
                                moves.append(temp.GetCopy())
                            else:
                                if board.grid[dx][dy].colour != self.colour: # Checking if the piece at the destination is of opposite colour
                                    captures.append(temp.GetCopy())
        return moves, captures
