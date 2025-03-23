import pygame
import resources
import components
import util
import random


class Menu:
    surface: pygame.SurfaceType
    play_button: components.SurfaceButton
    quit_button: components.SurfaceButton

    def __init__(self, surface):
        self.surface = surface
        self.play_button = components.text_button("Play", (250, 50), font=resources.FONT)
        self.quit_button = components.text_button("Quit", (250, 50), font=resources.FONT)

    def do(self):
        self.surface.blit(resources.SPLASH_SCREEN_IMAGE, (0, 0))

        title_text = "Secret Sandwich Service"

        self.surface.blit(
            resources.FONT_XL.render(title_text, True, "black"),
            util.add_coord(util.center_within(self.surface.get_size(), resources.FONT_XL.size(title_text)), (0, -200)),
        )

        gap = 15
        central_button_block = util.center_within(self.surface.get_size(), (250, (50 * 2) + gap))

        if self.play_button.blit_onto(self.surface, central_button_block):
            pygame.event.post(util.make_transition_event("gameplay"))

        if self.quit_button.blit_onto(self.surface, util.add_coord(central_button_block, (0, 50 + gap))):
            pygame.event.post(pygame.event.Event(pygame.QUIT))


class GameOver:
    surface: pygame.SurfaceType
    quit_button: components.SurfaceButton
    desc: str

    def __init__(self, surface):
        self.surface = surface
        self.quit_button = components.text_button(":(", (250, 50), font=resources.FONT)
        self.desc = random.choice(resources.SCRIPT_GAME_OVER)

    def do(self):
        # self.surface.blit(resources.SPLASH_SCREEN_IMAGE, (0, 0))
        self.surface.fill(0xff0000)

        title_text = "YOU LOSE"
        self.surface.blit(
            resources.FONT_XL.render(title_text, True, "black"),
            util.add_coord(util.center_within(self.surface.get_size(), resources.FONT_XL.size(title_text)), (0, -200)),
        )

        util.render_text_centred_at(self.desc, resources.FONT, 0x000000, *util.add_coord(util.center_within(self.surface.get_size(), (1, 1)), (0, -100)), self.surface, self.surface.get_size()[0]*0.8)

        gap = 15
        central_button_block = util.center_within(self.surface.get_size(), (250, 50))

        if self.quit_button.blit_onto(self.surface, util.add_coord(central_button_block, (0, 50 + gap))):
            pygame.event.post(pygame.event.Event(pygame.QUIT))
