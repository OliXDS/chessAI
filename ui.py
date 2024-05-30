import pygame
from ui import *
from botSetting import sounds

# NOT NEEDED???

class TextUI: # Class for handling text user interface elements
    def __init__(self, screen, text, x, y, fontSize, colour):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.fontSize = fontSize
        self.colour = colour
        self.textColour = colour
        self.font = pygame.font.Font("assets/fonts/Champagne&Limousines.ttf", self.fontSize) # selected font
        self.centered = False # Determine if text should be centered
    
    def Draw(self): # Method to draw the text on the screen
        mytext = self.font.render(self.text, True, self.textColour)

        if self.centered:
            text_rect = mytext.get_rect(center=(self.x , self.y))
            self.screen.blit(mytext, text_rect)
        else:
            self.screen.blit(mytext, (self.x, self.y))

class Button: # Class for creating button UI elements
    def __init__(self, screen, x, y, w, h, text):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.thickness = 4
        self.backgroundColour = (70, 70, 70)
        self.outlineColour = (0, 0, 0)
        self.textColour = (255 ,255, 255)
        self.hoverColour = (50, 50, 50)
        self.fontSize = 24
        self.font = pygame.font.Font("assets/fonts/Champagne&Limousines.ttf", self.fontSize)
        self.tempcolour = self.backgroundColour # Temporary colour for hover effect
        self.counter = 0

    def Hover(self):
    # Method to check if mouse is hovering over the button
        mouse_position = pygame.mouse.get_pos()
        # return 0 or 1
        if self.get_rect().collidepoint(mouse_position):
            self.tempcolour = self.hoverColour
            self.counter += 1
            if self.counter == 2:
                sounds.check_sound.play()
        else:
            self.counter = 0
            self.tempcolour = self.backgroundColour

    def get_rect(self):
        # Method to get the rectangle representing the button
        x = self.x - self.w//2 - self.thickness//2
        y = self.y - self.h //2 - self.thickness//2
        w = self.w + self.thickness
        h = self.h + self.thickness
        return pygame.Rect(x, y, w, h)

    def Draw(self):
        # Method to draw the button on the screen
        out_x = self.x - self.w//2 - self.thickness//2
        out_y = self.y - self.h //2 - self.thickness//2
        out_w = self.w + self.thickness
        out_h = self.h + self.thickness

        in_x = self.x - self.w //2
        in_y = self.y - self.h //2
        in_w = self.w
        in_h = self.h

        # Draw button outline and fill with colour
        pygame.draw.rect(self.screen, self.outlineColour, [out_x, out_y, out_w, out_h])
        pygame.draw.rect(self.screen, self.tempcolour, [in_x, in_y, in_w, in_h])
        buttonText = self.font.render(self.text, True, self.textColour)
        text_rect = buttonText.get_rect(center=(in_x + self.w//2, in_y + self.h//2))
        self.screen.blit(buttonText, text_rect)

        self.Hover()
