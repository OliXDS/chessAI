from botSetting import Config # Importing configuration settings
from displayImages import * # Importing utility functions
from tools import Position, OnBoard

class Piece:
    def __init__(self, position, colour):
        # Initialize Piece object with position, colour, previous move, and code
        # 0 -> White, 1 -> Black
        self.position = position
        self.colour = colour
        self.previousMove = None
        self.code = None

    def updatePosition(self, position):
        # Update the position of the piece
        self.position.x = position.x
        self.position.y = position.y

    def GetPatternMoves(self, board, patterns):
        # Generate all possible moves and captures for the piece based on given patterns
        moves = []
        captures = []
        for pattern in patterns:
            m, c = self.generator(board, pattern[0], pattern[1])
            moves =  moves+ m # Append moves
            captures = captures+ c # Append captures
        return moves, captures

    def generator(self, board, dx, dy):
        # Generate moves and captures in a particular direction
        moves = []
        captures = []
        pos = Position(self.position.x + dx, self.position.y + dy)

        # Keep iterating while the position is on the board and empty
        while OnBoard(pos) and board.grid[pos.x][pos.y] == None:
            moves.append(pos.GetCopy()) # Append the move
            pos.x = pos.x + dx # Move in the x direction
            pos.y = pos.y + dy # Move in the y direction

        # If there's a piece of the opponent's colour, append as a capture
        if OnBoard(pos) and board.grid[pos.x][pos.y] != None and board.grid[pos.x][pos.y].colour != self.colour:
            captures.append(pos.GetCopy())

        #print(moves)   # --> Shows the moves

        return moves, captures
