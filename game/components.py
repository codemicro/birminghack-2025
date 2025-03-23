import random
import pygame
import resources
import util


class SurfaceButton:
    surface: pygame.SurfaceType
    already_pressed: bool
    already_collided: bool

    def __init__(self, surface):
        self.surface = surface
        self.already_pressed = False
        self.already_collided = False

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

        does_mouse_collide = pygame.Rect(*pos, *self.surface.get_size()).collidepoint(*pygame.mouse.get_pos())

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


def text_button(text, size, font=resources.FONT_SM) -> SurfaceButton:
    surface = pygame.Surface(size)
    surface.fill((255, 0, 255))
    surface.set_colorkey((255, 0, 255))

    (text_width, text_height) = font.size(text)
    text_pos = (
        (size[0] - text_width) / 2,
        (size[1] - text_height) / 2,
    )

    pygame.draw.rect(surface, 0xdf3062, pygame.Rect((0, 0), size), border_radius=5)
    surface.blit(
        font.render(text, True, "black"),
        text_pos,
    )

    return SurfaceButton(surface)


class Character:
    torso: pygame.Surface
    head: pygame.Surface

    headpos: int

    def __init__(self):
        self.torso = random.choice(resources.CHARACTER_TORSOS)
        self.head = random.choice(resources.CHARACTER_HEADS)
        self.headpos = self.head.get_size()[1] * random.randint(6, 9) / 10

    def blit_onto(self, output_surface: pygame.SurfaceType, pos: tuple[int, int]):
        output_surface.blit(self.torso, util.add_coord(pos, (0, self.headpos)))
        torso_centerpoint = util.center_within(self.torso.get_size(), self.head.get_size())
        output_surface.blit(self.head, util.add_coord(pos, (torso_centerpoint[0], 0)))
