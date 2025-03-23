import pygame
import menu
import util
import gameplay
import resources
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True
    pygame.mouse.set_cursor(*pygame.cursors.arrow)

    screen.fill("lightblue")

    active_scene = menu.Menu(screen)

    while running:
        for _ in pygame.event.get(eventtype=pygame.QUIT):
            running = False

        for event in pygame.event.get(eventtype=util.TRANSITION_EVENT_TYPE):
            next_scene = event.dict["to"]
            match next_scene:
                case "menu":
                    active_scene = menu.Menu(screen)
                case "gameplay":
                    active_scene = gameplay.GamePlay(screen)
                case "gameover":
                    active_scene = menu.GameOver(screen)
                case _:
                    raise NotImplementedError("switch to scene " + event.dict["to"])
            screen.fill(0x000000)

        active_scene.do()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
