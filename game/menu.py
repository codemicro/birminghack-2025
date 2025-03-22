import pygame
import resources
import components
import util

class Menu:
    surface: pygame.SurfaceType
    play_button: components.Button
    quit_button: components.Button

    def __init__(self, surface):
        self.surface = surface
        self.play_button = components.Button("Play", (250, 50))
        self.quit_button = components.Button("Quit", (250, 50))

    def do(self):
        self.surface.blit(resources.SPLASH_SCREEN_IMAGE, (0, 0))

        gap = 15
        central_button_block = util.center_within(self.surface.get_size(), (250, (self.play_button.size[1] * 2) + gap))

        if self.play_button.blit_onto(self.surface, central_button_block):
            pygame.event.post(util.make_transition_event("gameplay"))

        if self.quit_button.blit_onto(self.surface, util.add_coord(central_button_block, (0, self.play_button.size[1] + gap))):
            pygame.event.post(pygame.event.Event(pygame.QUIT))
