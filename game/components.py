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


class Note:
    surface: pygame.Surface
    text: str

    def __init__(self, base: pygame.Surface, text: str):
        self.surface = pygame.Surface(base.get_size())
        self.text = text
        self.surface.blit(base, (0, 0))
        util.render_text_centred_at(text, resources.FONT_SM, 0x000000, base.get_size()[0] / 2, 5, self.surface, base.get_size()[0] - 20)

    def blit_onto(self, output_surface: pygame.Surface, pos: tuple[int, int]):
        output_surface.blit(
            self.surface,
            pos
        )


class Character:
    torso: pygame.Surface
    head: pygame.Surface
    glasses: pygame.Surface
    hair: pygame.Surface

    headpos: int
    text: str | None
    text_hash: int | None
    note: Note | None

    def __init__(self, text: str | None = None):
        self.torso = random.choice(resources.CHARACTER_TORSOS)
        self.head = random.choice(resources.CHARACTER_HEADS)
        self.glasses = random.choice(resources.CHARACTER_GLASSES)
        self.hair = random.choice(resources.CHARACTER_HAIR)
        self.headpos = self.head.get_size()[1] * random.randint(6, 9) / 10

        self.text = text
        self.note = None

    def blit_onto(self, output_surface: pygame.SurfaceType, pos: tuple[int, int]):
        output_surface.blit(self.torso, util.add_coord(pos, (0, self.headpos)))
        torso_centerpoint = util.center_within(self.torso.get_size(), self.head.get_size())
        output_surface.blit(self.head, util.add_coord(pos, (torso_centerpoint[0], 0)))
        if self.head not in resources.CHARACTER_HEADS[-2:]:
            output_surface.blit(self.glasses, util.add_coord(pos, (torso_centerpoint[0], 50)))
            output_surface.blit(self.hair, util.add_coord(pos, (torso_centerpoint[0], 0)))

        if self.text is not None:
            if self.note is None or hash(self.text) != self.text_hash:
                self.text_hash = hash(self.text)
                self.note = Note(resources.EMPTY_NOTE, self.text)

            self.note.blit_onto(output_surface, util.add_coord(pos, (-200, 0)))
