import pygame
import os
from pathlib import Path

base_dir = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    # pygame setup
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    main_font = pygame.font.Font(base_dir / "resources" / "Jersey10-Regular.ttf", size=40)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("lightblue")

        surf = main_font.render("can i take your order please", True, (0, 0, 0))
        screen.blit(surf, (50, 50))

        pygame.mouse.set_cursor(*pygame.cursors.arrow)

        button_pressed, _, _ = pygame.mouse.get_pressed()
        if button_pressed:
            player_pos = pygame.mouse.get_pos()

        pygame.draw.circle(screen, "red", player_pos, 40)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
