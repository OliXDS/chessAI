from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # found online --> only gets rid of "Hello from pygam etc..."

import pygame
import sys
from botSetting import Config
from screens.uiMenu import Menu
from screens.chessGame import runChess

def main():
    # initialise pygame
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(Config.resolution)

    # load and set icon of the main window
    loaded_icon = pygame.image.load("assets/images/white_knight.png")
    main_icon = pygame.transform.smoothscale(loaded_icon, (Config.windowIconSize, Config.windowIconSize))
    pygame.display.set_icon(main_icon)
    # this is the game loop
    MenuScreen = Menu(screen)
    # here runs the ui loop
    MenuScreen.Run()
    # quit pygame
    chess = runChess(screen)
    chess.vsAI()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



"""
def main():
    # initialise pygame
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(Config.resolution)

    # load and set icon of the main window
    loaded_icon = pygame.image.load("assets/images/white_knight.png")
    main_icon = pygame.transform.smoothscale(loaded_icon, (Config.windowIconSize, Config.windowIconSize))
    pygame.display.set_icon(main_icon)
    # game loop
    # WILL HAVE TO GET RID OF MENU! Below...
    MenuScreen = Menu(screen)
    MenuScreen.Run()
    # quit pygame
    chess = Chess(screen)
    print("vs computer screen")
    chess.vsComputer()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()










"""
