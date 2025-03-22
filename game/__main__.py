import pygame
import os
from pathlib import Path
import resources
import random

def sandwich(screen):
    fillings = ["lettuce", "ham", "tomatoes"]
    amountOfFilling = random.randrange(0,4)
    sandwich = "bread "
    for _ in range(amountOfFilling):
        filling = random.randrange(0,3)
        sandwich += fillings[filling] + " "

    sandwich += "bread"
    screen.blit(            
        resources.FONT.render(sandwich, True, (0, 0, 0)),
        (100, 100),
    )
    
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    width = screen.get_width() 
    height = screen.get_height() 
    #surface1 = pygame.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    colour = "lightblue"
    screen.fill("lightblue")
    
    while running:
        #Image = Buttonify('resources\sprites\start.png',(100,100),screen)
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            # button the game is terminated 
            if 10 <= mouse[0] <= 40 and 10 <= mouse[1] <= 40: 
                if colour == "lightblue":
                    screen.fill("blue") 
                    colour = "blue"
                else:
                    screen.fill("lightblue") 
                    colour = "lightblue"
                    sandwich(screen)
                    #code if button is pressed goes here

        # fill the screen with a color to wipe away anything from last frame
        '''if colour == "lightblue":
            #counter
        else:
            #food'''
        
        

        mouse = pygame.mouse.get_pos() 
        screen.blit(
            resources.FONT.render("can i take your order please", True, (0, 0, 0)),
            (50, 50),
        )
        pygame.draw.rect(screen,"green",[10,10,40,40])
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

        button_pressed, _, _ = pygame.mouse.get_pressed()
        if button_pressed:
            player_pos = pygame.mouse.get_pos()

        screen.blit(
            resources.TOMATO,
            player_pos,
        )
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
