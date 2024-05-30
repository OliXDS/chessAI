import pygame

pygame.init()
pygame.font.init()

class Setting:
    def __init__(self):
        # Board settings
        self.boardSize = 8
        self.windowIconSize = 30
        self.width = 1600
        self.height = 900
        self.resolution = (self.width, self.height)
        self.top_offset = 20
        self.spotSize = (self.height - self.top_offset) // self.boardSize
        self.horizontal_offset = self.width // 2 - (self.spotSize * (self.boardSize // 2)) # sets the board in the middle of the screen
        self.fps = 60 # FPS setting
        self.CoordFont = pygame.font.SysFont("jaapokki", 18, bold=True) # Font setting for coordinates display
        self.highlightOutline = 5 # Thickness of highlight outlines
        self.themeIndex = -1
        # self.horizontal_offset = self.width // 2 - (self.spotSize * (self.boardSize // 2))
        # CHANGE THE AI DIFFICULTY
        self.AI_DEPTH = 3 # Default AI difficulty level
        
        self.themes = [
            # CHESS.com THEME
            {"dark": (148, 111, 81), "light": (240, 217, 181), "outline": (0, 0, 0)},
            # GREEN THEME
            {"dark": (118, 148, 85), "light": (234, 238, 210), "outline": (0, 0, 0)},
        ]


class Sound:
    def __init__(self):
        self.capture_sound = pygame.mixer.Sound("assets/sounds/capture_sound.mp3")
        self.castle_sound = pygame.mixer.Sound("assets/sounds/castle_sound.mp3")
        self.check_sound = pygame.mixer.Sound("assets/sounds/check_sound.mp3")
        self.checkmate_sound = pygame.mixer.Sound("assets/sounds/checkmate_sound.mp3")
        self.game_over_sound = pygame.mixer.Sound("assets/sounds/gameover_sound.mp3")
        self.game_start_sound = pygame.mixer.Sound("assets/sounds/start_sound.mp3")
        self.move_sound = pygame.mixer.Sound("assets/sounds/move_sound.mp3")
        self.stalemate_sound = pygame.mixer.Sound("assets/sounds/stalemate_sound.mp3")
        self.pop = pygame.mixer.Sound("assets/sounds/pop.mp3")

# Instantiate game settings and sound effects
Config = Setting()
sounds = Sound()

