import pygame
import components
import util
import resources
import random

class GamePlay:
    surface: pygame.SurfaceType
    play_button: components.SurfaceButton
    ham_button: components.SurfaceButton
    tomato_button: components.SurfaceButton
    lettuce_button: components.SurfaceButton
    top_button: components.SurfaceButton

    def __init__(self, surface):
        self.surface = surface
        self.switch_button = components.text_button("Switch", (250, 50),  font=resources.FONT)
        self.serve_button = components.text_button("Serve", (250, 50),  font=resources.FONT)
        self.ham_button = components.SurfaceButton(resources.SUB_HAM_SPRITE_3X)
        self.tomato_button = components.SurfaceButton(resources.SUB_TOMATO_SPRITE_3X)
        self.lettuce_button = components.SurfaceButton(resources.SUB_LETTUCE_SPRITE_3X)
        self.top_button = components.SurfaceButton(resources.SUB_TOP_SPRITE_3X)
        self.status = "Counter"
        self.newOrder = True
        self.sandwichmade = False
        self.correctsandwich = []
        self.madesandwich = ["bread"]

    def displaysandwich(screen, sandwich):
        position = 200
        for i in sandwich:
            screen.blit(            
                resources.FONT.render(i, True, (0, 0, 0)),
                (1000, position),
            )
            position += 50

    def sandwich(self, screen):
        fillings = ["lettuce", "ham", "tomatoes"]
        amountOfFilling = random.randrange(1,4)
        sandwich = ["bread"]
        for _ in range(amountOfFilling):
            filling = random.randrange(0,3)
            sandwich.append(fillings[filling])
        sandwich.append("bread")
        self.correctsandwich = sandwich
        GamePlay.displaysandwich(screen, sandwich)
        

    def do(self):
        if self.switch_button.blit_onto(self.surface, (1000, 10)):
            if self.status == "Counter" and self.sandwichmade == False:
                self.surface.fill("lightgreen")
                self.status = "Food"
                self.surface.blit(resources.SUB_BOTTOM_SPRITE_10X, (300, 350))
            else:
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                self.status = "Counter"
                self.newOrder = True

        if self.serve_button.blit_onto(self.surface, (10, 600)):
            self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
            #serve
            print("serve")
            print(self.correctsandwich)
            print(self.madesandwich)
            if self.correctsandwich == self.madesandwich:
                self.surface.blit(            
                resources.FONT.render("Correct!!", True, (0, 0, 0)),
                (10, 10),
                )
            else:
                self.surface.blit(            
                resources.FONT.render("Incorrect!!", True, (0, 0, 0)),
                (10, 10),
                )
            self.madesandwich = ["bread"]
            self.correctsandwich = []
            #change to counter button

        if self.status == "Counter" and self.newOrder == True:
            GamePlay.sandwich(self, self.surface)
            self.newOrder = False
        elif self.status == "Food" :
            GamePlay.displaysandwich(self.surface, self.correctsandwich)
            if self.ham_button.blit_onto(self.surface, (100, 250)):
                self.surface.blit(resources.SUB_HAM_SPRITE_10X, (300, 350))
                self.madesandwich.append("ham")
            elif self.tomato_button.blit_onto(self.surface, (250, 250)):
                self.surface.blit(resources.SUB_TOMATO_SPRITE_10X, (300, 350))
                self.madesandwich.append("tomatoes")
            elif self.lettuce_button.blit_onto(self.surface, (400, 250)):
                self.surface.blit(resources.SUB_LETTUCE_SPRITE_10X, (300, 350))
                self.madesandwich.append("lettuce")
            elif self.top_button.blit_onto(self.surface, (550, 250)):
                self.surface.blit(resources.SUB_TOP_SPRITE_10X, (300, 350))
                self.madesandwich.append("bread")
            self.sandwichmade == True


