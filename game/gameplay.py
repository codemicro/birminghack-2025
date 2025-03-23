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

    character: components.Character
    character_pos: tuple[int, int]

    def __init__(self, surface):
        self.surface = surface
        self.menu_button = components.text_button("Menu", (250, 50),  font=resources.FONT)
        self.counter_button = components.text_button("Counter", (250, 50),  font=resources.FONT)
        self.food_button = components.text_button("Prepare", (250, 50),  font=resources.FONT)
        self.serve_button = components.text_button("Serve", (250, 50),  font=resources.FONT)
        self.ham_button = components.SurfaceButton(resources.SUB_HAM_SPRITE_3X)
        self.tomato_button = components.SurfaceButton(resources.SUB_TOMATO_SPRITE_3X)
        self.lettuce_button = components.SurfaceButton(resources.SUB_LETTUCE_SPRITE_3X)
        self.top_button = components.SurfaceButton(resources.SUB_TOP_SPRITE_3X)
        self.status = "Counter"
        self.newOrder = True
        self.sandwichmade = False
        self.correctsandwich = []
        self.madesandwich = ["Bread"]
        self.start = True
        self.suspicion = 0

        self.character = components.Character()
        self.character_pos = (400 + random.randint(0, 100), 100 + random.randint(25, 100))

    def displaysandwich(screen, sandwich):
        position = 125
        picposition = 100
        start = 0
        for i in sandwich:
            screen.blit(            
                resources.FONT.render(i, True, (0, 0, 0)),
                (1110, position),
            )
            if start == 0:
                screen.blit(
                    resources.TICKET_TOP_SPRITE_3X,
                    (975, picposition),
                )
                start = 1
            elif i == "Lettuce":
                screen.blit(
                    resources.TICKET_LETTUCE_SPRITE_3X,
                    (992, picposition + 15),
                )
            elif i == "Ham":
                screen.blit(
                    resources.TICKET_HAM_SPRITE_3X,
                    (975, picposition - 2),
                )
            elif i == "Tomatoes":
                screen.blit(
                    resources.TICKET_TOMATO_SPRITE_3X,
                    (992, picposition + 15),
                )
            elif i == "Bread":
                screen.blit(
                    resources.TICKET_BOTTOM_SPRITE_3X ,
                    (975, picposition),
                )
            picposition +=75
            position += 75

    def sandwich(self, screen):
        fillings = ["Lettuce", "Ham", "Tomatoes"]
        amountOfFilling = random.randrange(1,4)
        sandwich = ["Bread"]
        for _ in range(amountOfFilling):
            filling = random.randrange(0,3)
            sandwich.append(fillings[filling])
        sandwich.append("Bread")
        self.correctsandwich = sandwich
        GamePlay.displaysandwich(screen, sandwich)
        

    def do(self):
        if self.start == True:
            self.surface.fill("lightgreen")
            self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
            self.start = False

        if self.menu_button.blit_onto(self.surface, (15, 5)):
            pygame.event.post(util.make_transition_event("menu"))

        if self.status == "Counter" and self.sandwichmade == False:
            if self.food_button.blit_onto(self.surface, (1000, 5)):
                self.surface.fill("lightgreen")
                self.status = "Food"
                self.surface.blit(resources.SUB_BOTTOM_SPRITE_10X, (300, 350))
        else:
            if self.counter_button.blit_onto(self.surface, (1000, 5)):
                self.surface.fill("lightgreen")
                self.character.blit_onto(self.surface, self.character_pos)
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                self.status = "Counter"
                self.newOrder = True
        ''' #swap status for different buttons
        if self.switch_button.blit_onto(self.surface, (1000, 5)):
            if self.status == "Counter" and self.sandwichmade == False:
                self.surface.fill("lightgreen")
                self.status = "Food"
                self.surface.blit(resources.SUB_BOTTOM_SPRITE_10X, (300, 350))
            else:
                self.surface.fill("lightgreen")
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                self.status = "Counter"
                self.newOrder = True'''
        if self.status == "Food":
            if self.serve_button.blit_onto(self.surface, (10, 660)):
                self.status = "Serve"
                self.surface.fill("lightgreen")
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                GamePlay.displaysandwich(self.surface, self.correctsandwich)
                #serve

                if self.correctsandwich == list(reversed(self.madesandwich)):
                    self.surface.blit(
                    resources.FONT.render("Correct!!", True, (0, 0, 0)),
                    (10, 10),
                    )
                    self.suspicion -= 1
                else:
                    self.surface.blit(
                    resources.FONT.render("Incorrect!!", True, (0, 0, 0)),
                    (10, 10),
                    )
                    self.suspicion += 1
                self.madesandwich = ["Bread"]
                self.correctsandwich = []
                #change to counter button

        if self.status == "Counter" and self.newOrder == True:
            GamePlay.sandwich(self, self.surface)
            self.newOrder = False
        elif self.status == "Food" :
            GamePlay.displaysandwich(self.surface, self.correctsandwich)
            variationlr = random.randrange(0,15)
            variationud = random.randrange(0,15)
            if self.ham_button.blit_onto(self.surface, (100, 250)):
                self.surface.blit(resources.SUB_HAM_SPRITE_10X, (300 + variationlr, 350 + variationud))
                self.madesandwich.append("Ham")
            elif self.tomato_button.blit_onto(self.surface, (250, 250)):
                self.surface.blit(resources.SUB_TOMATO_SPRITE_10X, (300 + variationlr, 350 + variationud))
                self.madesandwich.append("Tomatoes")
            elif self.lettuce_button.blit_onto(self.surface, (400, 250)):
                self.surface.blit(resources.SUB_LETTUCE_SPRITE_10X, (300 + variationlr, 350 + variationud))
                self.madesandwich.append("Lettuce")
            elif self.top_button.blit_onto(self.surface, (550, 250)):
                self.surface.blit(resources.SUB_TOP_SPRITE_10X, (300 + variationlr, 350 + variationud))
                self.madesandwich.append("Bread")
            self.sandwichmade == True


