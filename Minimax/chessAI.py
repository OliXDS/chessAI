from Minimax.Values import map_points, PieceMap
from pieces import Pawn # Import the Pawn class
import math # dont think I need this anymore

class Minimax(object):
    def __init__(self, depth, board, AlphBetaPruning=True, UsePointMaps=True):
        # Initialiee Minimax object with depth, board, and optional parameters for alpha-beta pruning and point maps usage
        self.depth = depth
        self.board = board
        self.AlphaBetaPruning = AlphBetaPruning
        self.UsePointMaps = UsePointMaps

    def Start(self, depth):
        bestMove = None
        # bestScore = -math.inf
        bestScore = -9999
        currentPiece = None
        isMaximizer = False
        # check if the player is maximizer
        if self.board.player == 1:
            isMaximizer = True
        else:
            isMaximizer = False

        if isMaximizer == False:
            bestScore *= (-1) # If not maximizer, adjust bestScore to be negative
        # get All the possible move in the current Position
        for pieces in self.board.grid:
            for piece in pieces:
                if piece != None and piece.colour == self.board.player: #Checking if the piece exists and belongs to the current player
                    moves, captures = self.board.GetAllowedMoves(piece, True)
                    possibleMoves = captures + moves
                    # Combining captures and regular moves
                    for position in possibleMoves:
                        prev_pos = piece.position # Saving the previous position of the piece
                        pion = self.board.MoveSimulation(piece, position)

                        # score = self.minimax(depth + 1, not isMaximizer, -math.inf, math.inf)
                        score = self.minimax(depth + 1, not isMaximizer, -10000, 10000)
                        if type(piece) == Pawn and (position.y == 7 or position.y == 0):
                            score += 80 # Adjust score for pawn reaching the last row
                        elif self.board.isEnPassant(piece, position):
                            score += 10 # Adjust score for en passant
                        if not isMaximizer:
                            score *= (-1)
                        if score >= bestScore and isMaximizer:
                            bestScore = score
                            bestMove = position
                            currentPiece = piece

                        # UNDO MOVE if no cpatured
                        if pion == None:
                            self.board.MoveSimulation(piece, prev_pos)
                        else:
                            self.board.MoveSimulation(piece, prev_pos)
                            self.board.MoveSimulation(pion, position)

        return currentPiece, bestMove # undoing move if a piece is caputred


    def minimax(self, depth, isMaximizer, alpha, beta):
        # Minimax algorithm with alpha-beta pruning
        if self.depth == depth:
            return self.Evaluate() * (-1)
        # Return the evaluated score at max depth

        if isMaximizer:
            bestScore = -9999
            possibleMoves = self.LegalMoves(1, 7) # Getting legal moves for the maximiser
            for _index in range(len(possibleMoves) -1, -1, -1):
                # Looping through possible moves
                piece = possibleMoves[_index][1]
                i = possibleMoves[_index][2]
                prev_pos = piece.position
                pion = self.board.MoveSimulation(piece, i)
                score = self.minimax(depth + 1, False, alpha, beta)
                bestScore = max(bestScore, score)
                if self.AlphaBetaPruning:
                    alpha = max(alpha, bestScore)
                self.UndoMove(pion, piece, prev_pos, i)

                if beta <= alpha and self.AlphaBetaPruning:
                    return bestScore
            return bestScore
        else: # Minimising opponent's score
            bestScore = 9999
            possibleMoves = self.LegalMoves(0, 0) # Getting legal moves
            for _index in range(len(possibleMoves) -1, -1, -1):
                piece = possibleMoves[_index][1]
                i = possibleMoves[_index][2]
                prev_pos = piece.position
                currentPiece = self.board.MoveSimulation(piece, i)
                score = self.minimax(depth + 1, True, alpha, beta)
                bestScore = min(bestScore, score)
                if self.AlphaBetaPruning:
                    beta = min(beta, bestScore)
                self.UndoMove(currentPiece, piece, prev_pos, i)
                if beta <= alpha and self.AlphaBetaPruning:
                    return bestScore
            return bestScore

    def Evaluate(self):
        # Evaluate the board position
        totalScore = 0
        for pieces in self.board.grid:
            for piece in pieces:
                if piece != None:# Checking if the piece exists
                    p_map = PieceMap(piece)
                    score = piece.value
                    if self.UsePointMaps:
                        score += p_map[piece.position.y][piece.position.x]
                    totalScore += score

        return totalScore
    
    def UndoMove(self, currentPiece, piece, prev_pos, p):
        if currentPiece == None:# Undoing move if no captured piece
            self.board.MoveSimulation(piece, prev_pos)
        elif currentPiece != None:
            self.board.MoveSimulation(piece, prev_pos)
            self.board.MoveSimulation(currentPiece, p)

    def GetMoves(self, piece, position):
        # Get all possible moves for a piece
        bestMoves = []
        possibleMoves = []
        moves, captures = self.board.GetAllowedMoves(piece, True)
        for pos in captures:
            if self.board.grid[pos.x][pos.y] != None: # Checking if a piece is captured
                bestMoves.append([10 * self.board.grid[pos.x][pos.y].value - piece.value, piece, pos]) # Adding capture move with adjusted score
                if type(piece) == Pawn and (pos.y == position): # checking in pawn reaches the last row
                    bestMoves[-1][0] == bestMoves[-1][0] + 90
            else:
                bestMoves.append([piece.value, piece, pos])
        for pos in moves:
            if type(piece) == Pawn and (pos.y == position):
                bestMoves.append([90, piece, pos])
            else:
                bestMoves.append([0, piece, pos])

        return possibleMoves, bestMoves

    def LegalMoves(self, colour, pos):
        # Get legal moves for a given colour and position
        possibleMoves = []
        bestMoves = []
        for pieces in self.board.grid:
            for piece in pieces:
                if piece != None and piece.colour == colour: # cheking if the piece exists and belongs to the given colour
                    temp_moves, better_temp_moves = self.GetMoves(piece, pos)
                    possibleMoves += temp_moves
                    bestMoves += better_temp_moves

        bestMoves.sort(key=lambda key: key[0]) # sorting best moves based on scores
        possibleMoves = possibleMoves + bestMoves
        return possibleMoves
