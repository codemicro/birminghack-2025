import pygame
import components
import util

class Counter:
    surface: pygame.SurfaceType
    play_button: components.Button

    def __init__(self, surface):
        self.surface = surface
        self.play_button = components.Button("Food", (250, 50))

    def do(self):
        
        #width = self.get_width() 
        #height = self.get_height() 
        #gap = 15
        #central_button_block = util.center_within(self.surface.get_size(), (250, (self.play_button.size[1] * 2) + gap))

        if self.play_button.blit_onto(self.surface, (1000, 10)):
            #status = "Food"
            
            print("Clicked!!")
            return "Food"
        #self.switch.do()
        #if self.switch.blit_onto(self.surface, central_button_block):
         #   pygame.event.post(pygame.event.Event(pygame.SWITCH))
