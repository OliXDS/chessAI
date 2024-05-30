from pieces.base import Piece
from tools import OnBoard, Position
from botSetting import Config
from displayImages import GetSprite

class Pawn(Piece): # inheriting from the Piece class
    def __init__(self, position, colour):
        super().__init__(position, colour) # Call the constructor of the superclass (Piece)
        self.code = "p"
        self.value = 10 if colour == 0 else -10
        self.sprite = GetSprite(self)
        self.previousMove = None
        self.pieceMap = []

    # Method to handle En Passant moves for the Pawn
    def EnPassant(self, board, change):
        moves = []
        for i in (-1, 1): # Iterate over possible directions for En Passant moves
            temp_pos = Position(self.position.x + i, self.position.y)
            if OnBoard(temp_pos): # Check if the position is on the board
                pieceToCapture = board.grid[temp_pos.x][temp_pos.y]
                if type(pieceToCapture) == Pawn and self.colour != pieceToCapture.colour:
                    previousmove = board.RecentMove()
                    if previousmove != None and previousmove[2] == self.code and previousmove[4].x == self.position.x + i\
                        and abs(previousmove[4].y - previousmove[3].y) == 2: # Check if the previous move was a double-step by an enemy Pawn next to this Pawn
                        moves.append(Position(self.position.x + i, self.position.y + change))# Add En Passant move

        return moves # Return possible En Passant moves

    def GetMoves(self, board):
        moves = []
        captures = []
        if self.colour == 0:
            offset = -1 # If white, move upwards
        else:
            offset = 1 # If black, move downwards
        dy = self.position.y + offset # Calculate the y-coordinate for the next row
        # all the possible moves of a pawn
        if OnBoard(Position(self.position.x, dy)) and board.grid[self.position.x][dy] == None :
            moves.append(Position(self.position.x, dy))
            if self.previousMove == None: # Check if it's the Pawn's first move
                dy += offset
                if board.grid[self.position.x][dy] == None: # Check if the double-step square is empty
                    moves.append(Position(self.position.x, dy))

        dy = self.position.y + offset # Reset y-coordinate for captures
        # diagonal captures
        for i in (-1, 1):
            dx = self.position.x + i
            if OnBoard(Position(dx, dy)) and board.grid[dx][dy] != None: # Check if the square contains a piece
                if board.grid[dx][dy].colour != self.colour: # Check if it's an enemy piece
                    captures.append(Position(dx, dy))
        # EN PASSANT CAPTURES
        special_moves = self.EnPassant(board, offset)
        captures += special_moves
        return moves, captures
