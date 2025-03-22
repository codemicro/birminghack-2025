import pygame
import components

class Counter:
    surface: pygame.SurfaceType
    def __init__(self, surface):
        self.surface = surface
        self.play_button = components.Button("Food", (250, 50))

    def do(self, status):
        
        #width = self.get_width() 
        #height = self.get_height() 
        self.play_button.do()

        if self.play_button.blit_onto(self.surface, (1000, 10)):
            status = "Food"
            
            print("Clicked!!")
            return status
