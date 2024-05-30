
import pygame
import ui
import time
from screens.chessGame import runChess
from botSetting import Config



################################## STARTS HERE #################################################################
 
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.vsai = ui.Button(screen, Config.width//2, Config.height//2, 200, 80, "Play Computer")
        self.multiplayer = ui.Button(screen, Config.width//2, Config.height//2 + 100, 200, 80, "Pass and Play") 
        self.exit = ui.Button(screen, Config.width//2, Config.height//2 + 200, 200, 80, "Exit")
        self.background = pygame.image.load("./assets/images/background2.jpg")
        self.background = pygame.transform.smoothscale(self.background, Config.resolution)
        self.title = ui.TextUI(self.screen, "CHESS", Config.width//1.2, Config.height//6, 140, (255, 255, 255))
        self.title.centered = True
        self.running = True
        self.clock = pygame.time.Clock()
        self.chess = runChess(screen)
        self.newMenu = False
        #self.online = ui.Button(screen, Config.width//2, Config.height//2 + 200, 200, 80, "Online")
        #self.hard = ui.Button(screen, Config.width//2, Config.height//2 + 300, 200, 80, "Hard") # JUST ADDED
        #self.difficulty_menu_visible = False
        #self.easy_button = None # just added all of these 4 buttons
        #self.medium_button = None
        #self.hard_button = None
        #self.back_button = None
        #self.difficulty_menu = None # JUST ADDED


############################################################## added now
    """
    def DrawDifficultyMenu(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))
        # self.screen.fill((0, 0, 0))
        # Display title
        self.title.Draw()

        # Create buttons for difficulty levels
        self.easy_button = ui.Button(self.screen, Config.width//2, Config.height//2, 200, 80, "Easy")
        self.medium_button = ui.Button(self.screen, Config.width//2, Config.height//2 + 100, 200, 80, "Medium") 
        self.hard_button = ui.Button(self.screen, Config.width//2, Config.height//2 + 200, 200, 80, "Hard")
        self.back_button = ui.Button(self.screen, Config.width//2, Config.height//2 + 300, 200, 80, "Back")

        # Draw buttons
        self.easy_button.Draw()
        self.medium_button.Draw()
        self.hard_button.Draw()
        self.back_button.Draw()

        pygame.display.update()

    def HandleDifficultyClick(self):
        mouse_position = pygame.mouse.get_pos()
        if self.easy_button.get_rect().collidepoint(mouse_position):
            Config.AI_DEPTH = 1
            self.StartGame()
        elif self.medium_button.get_rect().collidepoint(mouse_position):
            #Config.AI_DEPTH = 3
            self.chess.gameOver = False # BEFORE
            self.vscomputer.tempcolour = (255, 255, 180) # BEFORE
            self.chess.vsComputer() # BEFORE
            #self.StartGame()
        elif self.hard_button.get_rect().collidepoint(mouse_position):
            Config.AI_DEPTH = 4
            self.StartGame()
        elif self.back_button.get_rect().collidepoint(mouse_position):
            self.DrawButtons()
        else:
            print("error")
                                """


    def StartGame(self):
        self.running = False
        #self.chess = Chess(self.screen) # added
        #self.chess.vsComputer() # added
#######################################################


#######################################################

    def DrawButtons(self):
        self.vsai.Draw()
        # Commented OUT BELOW
        self.multiplayer.Draw()
        #self.hard.Draw() # JUST ADDED
        self.exit.Draw()
        self.title.Draw()

        
################################################

    def HandleClick(self):
        mouse_position = pygame.mouse.get_pos()
        if self.vsai.get_rect().collidepoint(mouse_position):
            self.chess.gameOver = False # BEFORE
            self.vsai.tempcolour = (255, 255, 180) # BEFORE
            # self.DrawDifficultyMenu()
            # #time.sleep(5)
            # self.HandleDifficultyClick()
    
            
            
            #self.HandleDifficultyClick()
            #pygame.display.update() # <--- CHANGE HERE FOR NEW MENU - DOES WORK FOR A SPLIT SECOND WITH PYGAME.QUIT() #############################################################################################################################
            
            
            # self.chess.gameOver = False # BEFORE
            # self.vscomputer.tempcolor = (255, 255, 180) # BEFORE
            print("vs computer screen") 
            self.chess.vsAI() # BEFORE
            #self.chess.vsComputer(difficulty="easy") # AFTER
            #self.difficulty_menu = DifficultyMenu(self.screen, self) # JUST ADDED
            
            ######################################

            #DO NOT NEED --> START

        elif self.multiplayer.get_rect().collidepoint(mouse_position):
            self.chess.gameOver = False
            self.multiplayer.tempcolour = (255, 255, 180)
            print("multiplayer screen")
            self.chess.multiplayer()

        elif self.exit.get_rect().collidepoint(mouse_position):
            self.exit.tempcolour = (255, 255, 180)
            self.running = False
            pygame.quit() # just added <-- creates error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            

    def GetFrameRate(self):
        return self.clock.get_fps()

    def Run(self):
        while self.running:
            self.clock.tick(Config.fps)
            # update caption and frame rate
            pygame.display.set_caption("Chess " + str(int(self.GetFrameRate())))
            # display background image
            self.screen.blit(self.background, (0, 0))
            # handle Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() # just added <-- creates error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit() # just added <-- creates error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                elif event.type == pygame.MOUSEBUTTONUP:
                     # left mouse click
                    if event.button == 1:
                        print("button clicked")
                        
                        self.HandleClick() # NEED


            
            self.DrawButtons() #NEED
            pygame.display.update() # NEED
            #mouse_position = pygame.mouse.get_pos()
            #self.HandleClick() # MAKES THE COLLISION ACTIVATE
            # if self.vscomputer.get_rect().collidepoint(mouse_position):
                
            #     self.HandleDifficultyClick()
            #     self.DrawDifficultyMenu()
            # else:
            #     self.DrawButtons()
            # update screen
            
         ######################################################################################### ENDS HERE
"""
    def DrawDifficultyMenu(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Display title
        self.title.Draw()

        # Create buttons for difficulty levels
        self.easy_button = ui.Button(self.screen, Config.width//2, Config.height//2, 200, 80, "Easy")
        self.medium_button = ui.Button(self.screen, Config.width//2, Config.height//2 + 100, 200, 80, "Medium") 
        self.hard_button = ui.Button(self.screen, Config.width//2, Config.height//2 + 200, 200, 80, "Hard")
        self.back_button = ui.Button(self.screen, Config.width//2, Config.height//2 + 300, 200, 80, "Back")

        # Draw buttons
        self.easy_button.Draw()
        self.medium_button.Draw()
        self.hard_button.Draw()
        self.back_button.Draw()

        pygame.display.update()

    def HandleDifficultyClick(self):
        mouse_position = pygame.mouse.get_pos()
        if self.easy_button.get_rect().collidepoint(mouse_position):
            Config.AI_DEPTH = 1
            self.StartGame()
        elif self.medium_button.get_rect().collidepoint(mouse_position):
            Config.AI_DEPTH = 3
            self.StartGame()
        elif self.hard_button.get_rect().collidepoint(mouse_position):
            Config.AI_DEPTH = 4
            self.StartGame()
        elif self.back_button.get_rect().collidepoint(mouse_position):
            self.DrawButtons()

    def StartGame(self):
        self.running = False """



        ##################NEW###########################################
"""
class DifficultyMenu:
    def __init__(self, screen, parent_menu):
        self.screen = screen
        self.parent_menu = parent_menu
        self.easy_button = ui.Button(screen, Config.width//2, Config.height//2, 200, 80, "Easy")
        self.medium_button = ui.Button(screen, Config.width//2, Config.height//2 + 100, 200, 80, "Medium") 
        self.hard_button = ui.Button(screen, Config.width//2, Config.height//2 + 200, 200, 80, "Hard")
        # Other necessary initialization here

    def DrawButtons(self):
        self.easy_button.Draw()
        self.medium_button.Draw()
        self.hard_button.Draw()
        # Other buttons if any

    def HandleClick(self):
        mouse_position = pygame.mouse.get_pos()
        if self.easy_button.get_rect().collidepoint(mouse_position):
            self.parent_menu.chess.setAIDepth(1)  # Set AI depth for easy level
            # Proceed to start the game
        elif self.medium_button.get_rect().collidepoint(mouse_position):
            self.parent_menu.chess.setAIDepth(3)  # Set AI depth for medium level
            # Proceed to start the game
        elif self.hard_button.get_rect().collidepoint(mouse_position):
            self.parent_menu.chess.setAIDepth(4)  # Set AI depth for hard level
            # Proceed to start the game
        # Handle other button clicks if any
"""
    ##########################################################################
