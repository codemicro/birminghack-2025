from operator import truediv

import pygame
import resources


class Button:
    surface: pygame.SurfaceType
    text: str
    size: tuple[int, int]
    already_pressed: bool
    already_collided: bool

    def __init__(self, text, size):
        self.surface = pygame.Surface(size)
        self.surface.fill((255, 0, 255))
        self.surface.set_colorkey((255, 0, 255))
        self.already_pressed = False
        self.already_collided = False

        self.text = text
        self.size = size

        (text_width, text_height) = resources.FONT.size(text)
        self.text_pos = (
            (size[0] - text_width) / 2,
            (size[1] - text_height) / 2,
        )

    def do(self):
        pygame.draw.rect(self.surface, 0xdf3062, pygame.Rect((0, 0), self.size), border_radius=5)
        self.surface.blit(
            resources.FONT.render(self.text, True, "black"),
            self.text_pos,
        )

    def blit_onto(self, output_surface: pygame.SurfaceType, pos: tuple[int, int]) -> bool:
        """
        blits the button onto a surface

        :param output_surface: surface to blit on to
        :param pos: position to place the button
        :return: if the button is clicked or not - is debounced
        """
        output_surface.blit(
            self.surface,
            pos
        )

        does_mouse_collide = pygame.Rect(*pos, *self.size).collidepoint(*pygame.mouse.get_pos())

        if does_mouse_collide != self.already_collided:
            self.already_collided = does_mouse_collide
            pygame.mouse.set_cursor(*(pygame.cursors.broken_x if self.already_collided else pygame.cursors.arrow))

        if does_mouse_collide:
            (lmb_pressed, _, _) = pygame.mouse.get_pressed(3)

            if lmb_pressed and (not self.already_pressed):
                self.already_pressed = True
                return True

            if (not lmb_pressed) and self.already_pressed:
                self.already_pressed = False
                return False
        elif self.already_pressed:
            return False

        return False
