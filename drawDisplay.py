import pygame
from Minimax.Values import *
import numpy as np
from botSetting import Config
from ui import *
from displayImages import translate

# Initialize pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(Config.resolution)
animateSpot = 0
showValues = False

myFont = pygame.font.SysFont("consolas", 20, bold=True)

def DrawChessBoard(mapValues):
    # Function to draw the chessboard grid and pieces
    global animateSpot
    _min = np.min(mapValues)
    _max = np.max(mapValues)
    # drawing the empty chess board grid
    if animateSpot < Config.spotSize: # Incrementing the animation spot for smoother animation
        animateSpot += 2
    for i in range(Config.boardSize):
        # Loop through each square in the chessboard
        for j in range(Config.boardSize):
            x = i * Config.spotSize + Config.horizontal_offset
            y = j * Config.spotSize + Config.top_offset // 2
            # Calculate the coordinates of the square


            # Determine the colours of the sqaure based on its value
            l_colour = Config.themes[Config.themeIndex]["light"]
            l_colour = DimColour(l_colour, mapValues[j][i], _min, _max)
            d_colour = Config.themes[Config.themeIndex]["dark"]
            d_colour = DimColour(d_colour, mapValues[j][i], _min, _max)

            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, l_colour, [x, y, animateSpot, animateSpot])
            else:
                pygame.draw.rect(screen, d_colour, [x, y, animateSpot, animateSpot])

            if showValues:
                _x = i * Config.spotSize + Config.horizontal_offset
                _y = j * Config.spotSize + Config.top_offset // 2
                
                fontRenderer = myFont.render(str(mapValues[j][i]), True, (0, 0, 0))
                screen.blit(fontRenderer, (_x, _y))


def DimColour(colour, dim, _min, _max):
    # Function to adjust colour brightness based on the square value
    translatedValue = translate(dim, _min, _max, 8, 1)
    r, g, b = colour
    if r / translatedValue <= 0:
        r = 0
    elif r / translatedValue > 255:
        r = 255
    else:
        r = r / translatedValue

    if g / translatedValue <= 0:
        g = 0
    elif g / translatedValue > 255:
        g = 255
    else:
        g = g / translatedValue

    if b / translatedValue <= 0:
        b = 0
    elif b / translatedValue > 255:
        b = 255
    else:
        b = b / translatedValue

    return (r, g, b)

# states 0->pawn, 1->bishop, 2->knight, 3->rook, 4->queen, 5->king
states = ["pawn", "bishop", "knight", "rook", "queen", "king"]
mapState = 0

# Initialize the current piece to be displayed
currentPiece = TextUI(screen, states[mapState], 70, 70, 30, (255, 255, 255))

run = True
while run: # Main loop for the game
    screen.fill((10, 10, 10))
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit the game if the close button is clicked
            run = False
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT:
                mapState = (mapState + 1) % 6
                currentPiece.text = states[mapState]
            elif event.key == pygame.K_LEFT:
                mapState = (mapState-1) if mapState != 0 else 5
                currentPiece.text = states[mapState]
            elif event.key == pygame.K_ESCAPE: # Quit the game if ESC is pressed
                run = False
            elif event.key == pygame.K_UP:
                Config.themeIndex = (Config.themeIndex + 1) % len(Config.themes)
                print(Config.themeIndex)
            elif event.key == pygame.K_DOWN:
                Config.themeIndex = (Config.themeIndex - 1) if Config.themeIndex > 0 else len(Config.themes)-1
            elif event.key == pygame.K_SPACE:
                showValues = not showValues

    currentPiece.Draw()
    DrawChessBoard(map_points[mapState])
    pygame.display.update() # Update the display
pygame.quit()
