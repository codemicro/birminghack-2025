import pygame


def add_coord(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (
        a[0] + b[0],
        a[1] + b[1],
    )


def center_within(
    canvas_size: tuple[int, int], thing_size: tuple[int, int]
) -> tuple[int, int]:
    return (
        int((canvas_size[0] - thing_size[0]) / 2),
        int((canvas_size[1] - thing_size[1]) / 2),
    )


TRANSITION_EVENT_TYPE = 50123


def make_transition_event(to: str) -> pygame.event.Event:
    return pygame.event.Event(TRANSITION_EVENT_TYPE, {"to": to})


def render_text_centred_at(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(" ".join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = " ".join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh
