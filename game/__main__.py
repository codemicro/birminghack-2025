import pygame
import resources
import menu
import util


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    pygame.mouse.set_cursor(*pygame.cursors.arrow)

    m = menu.Menu(screen)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for _ in pygame.event.get(eventtype=pygame.QUIT):
            running = False

        # fill the screen with a color to wipe away anything from last frame

        for event in pygame.event.get(eventtype=util.TRANSITION_EVENT_TYPE):
            raise NotImplementedError("switch to scene " + event.dict["to"])

        m.do()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
