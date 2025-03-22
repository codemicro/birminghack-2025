import pygame
import components
import util
import resources
import random

class GamePlay:
    surface: pygame.SurfaceType
    play_button: components.Button

    def __init__(self, surface):
        self.surface = surface
        self.play_button = components.Button("Switch", (250, 50))
        self.ham_button = components.Button('resources/sprites/sub_ham.png', (100, 100))
        self.tomato_button = components.Button('resources/sprites/sub_tomato.png', (100, 100))
        self.lettuce_button = components.Button('resources/sprites/sub_lettuce.png', (100, 100))
        self.top_button = components.Button('resources/sprites/sub_top.png', (100, 100))
        self.status = "Counter"
        self.newOrder = True
        self.sandwichmade = False

    def sandwich(screen):
        fillings = ["lettuce", "ham", "tomatoes"]
        amountOfFilling = random.randrange(1,4)
        sandwich = ["bread"]
        for _ in range(amountOfFilling):
            filling = random.randrange(0,3)
            sandwich.append(fillings[filling])
        sandwich.append("bread")
        position = 200
        for i in sandwich:
            screen.blit(            
                resources.FONT.render(i, True, (0, 0, 0)),
                (1000, position),
            )
            position += 50

    def do(self):
        #width = self.get_width() 
        #height = self.get_height() 
        #gap = 15
        #central_button_block = util.center_within(self.surface.get_size(), (250, (self.play_button.size[1] * 2) + gap))

        if self.play_button.blit_onto(self.surface, (1000, 10)):
            #status = "Food"
            if self.status == "Counter" and self.sandwichmade == False:
                self.surface.fill("blue")
                self.surface.blit(            
                    resources.FONT.render("Food", True, (0, 0, 0)),
                    (100, 100),
                )
                self.status = "Food"
            else:
                self.surface.fill("lightblue")
                
                self.surface.blit(            
                    resources.FONT.render("Counter", True, (0, 0, 0)),
                    (100, 100),
                )
                self.status = "Counter"
                self.newOrder = True

        if self.status == "Counter" and self.newOrder == True:
            GamePlay.sandwich(self.surface)
            self.newOrder = False
        elif self.status == "Food":
            if self.ham_button.blit_onto(self.surface, (100, 250)):
                print("HAM!")
            elif self.tomato_button.blit_onto(self.surface, (250, 250)):
                print("TOMATO!")
            elif self.lettuce_button.blit_onto(self.surface, (400, 250)):
                print("LETTUCE!")
            elif self.top_button.blit_onto(self.surface, (550, 250)):
                print("TOP!")
            self.sandwichmade == True

