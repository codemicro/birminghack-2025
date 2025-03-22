import pygame

import components

class Menu:
    surface: pygame.SurfaceType

    def __init__(self, surface):
        self.surface = surface
        self.play_button = components.Button("balls"*5, (250, 50))

    def do(self):
        self.play_button.do()

        if self.play_button.blit_onto(self.surface, (200, 200)):
            print("Clicked!!")
