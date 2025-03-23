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
        self.food_button = components.text_button("Prepare/Next", (250, 50),  font=resources.FONT)
        self.getorder_button = components.text_button("Get Order", (250, 50),  font=resources.FONT)
        self.serve_button = components.text_button("Serve", (250, 50),  font=resources.FONT)
        self.drawer_button = components.SurfaceButton(resources.DRAWER_TRANS)
        self.draweropen_button = components.SurfaceButton(resources.DRAWER_OPEN)
        self.ham_button = components.SurfaceButton(resources.TUB_HAM_SPRITE)
        self.tomato_button = components.SurfaceButton(resources.TUB_TOMATO_SPRITE)
        self.lettuce_button = components.SurfaceButton(resources.TUB_LETTUCE_SPRITE)
        self.top_button = components.SurfaceButton(resources.TUB_TOP_SPRITE)
        #self.cheese_button = components.SurfaceButton(resources.TUB_CHEESE_SPRITE)
        self.status = "Get Order"
        self.newOrder = True
        self.sandwichmade = False
        self.correctsandwich = []
        self.madesandwich = ["Bread"]
        self.start = True
        self.suspicion = 0

        self.generate_character()

    def generate_character(self):
        self.character = components.Character(random.choice(resources.SCRIPT_ASK_SANDWICH))
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
            ''' elif i == "Cheese":
                screen.blit(
                    resources.TICKET_CHEESE_SPRITE_3X ,
                    (975, picposition),
                )'''
            picposition +=75
            position += 75

    def sandwich(self, screen):
        fillings = ["Lettuce", "Ham", "Tomatoes"]
        #fillings = ["Lettuce", "Ham", "Tomatoes", "Cheese"]
        amountOfFilling = random.randrange(1,6)
        sandwich = ["Bread"]
        for _ in range(amountOfFilling):
            #filling = random.randrange(0,4)
            filling = random.randrange(0,3)
            sandwich.append(fillings[filling])
        sandwich.append("Bread")
        self.correctsandwich = sandwich
        GamePlay.displaysandwich(screen, sandwich)
        

    def do(self):
        #print(self.status)
        if self.start == True:
            self.surface.blit(resources.BACKGROUND_SCREEN_IMAGE, (0, 0))
            self.character.blit_onto(self.surface, self.character_pos)
            self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
            self.start = False
            self.newOrder = False
        

        if self.menu_button.blit_onto(self.surface, (15, 5)):
            pygame.event.post(util.make_transition_event("menu"))

        if self.status == "Serve":
            if self.food_button.blit_onto(self.surface, (1000, 5)):
                self.surface.fill("lightgreen")
                self.status = "Food"
                self.surface.blit(resources.PREPARE_SCREEN_IMAGE, (0, 0))
                self.surface.blit(resources.SUB_PAPER_SPRITE_3X, (270, 315))
                self.surface.blit(resources.SUB_BOTTOM_SPRITE_10X, (300, 300))
                print("click get food serve")
        elif self.status == "Counter" and self.sandwichmade == False:
            
            if self.drawer_button.blit_onto(self.surface, (755, 465)):
                print("Drawer")
                self.surface.blit(resources.DRAWER_OPEN, (755, 465))
                if self.draweropen_button.blit_onto(self.surface, (755, 465)):
                    print("Drawer")
                    self.drawer_button.blit_onto(self.surface, (755, 465))
            if self.food_button.blit_onto(self.surface, (1000, 5)):
                self.surface.fill("lightgreen")
                self.status = "Food"
                self.surface.blit(resources.PREPARE_SCREEN_IMAGE, (0, 0))
                self.surface.blit(resources.SUB_PAPER_SPRITE_3X, (270, 315))
                self.surface.blit(resources.SUB_BOTTOM_SPRITE_10X, (300, 300))
                print("click prepare counter")
        elif self.status == "Food":
            if self.counter_button.blit_onto(self.surface, (1000, 5)):
                self.surface.blit(resources.BACKGROUND_SCREEN_IMAGE, (0, 0))
                self.generate_character()
                self.character.blit_onto(self.surface, self.character_pos)
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                self.status = "Counter"
                self.newOrder = True
                print ("click counter from food")
        elif self.status == "Get Order":
            if self.getorder_button.blit_onto(self.surface, (1000, 5)):
                self.surface.blit(resources.BACKGROUND_SCREEN_IMAGE, (0, 0))
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                GamePlay.sandwich(self, self.surface)
                self.status = "Counter"
                print ("click get order ")


        if self.status == "Food":
            if self.serve_button.blit_onto(self.surface, (10, 660)):
                self.status = "Serve"
                self.surface.blit(resources.BACKGROUND_SCREEN_IMAGE, (0, 0))
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0))
                self.surface.blit(resources.SUB_WRAPPED_SPRITE_3X, (350, 300))
                GamePlay.displaysandwich(self.surface, self.correctsandwich)
                #serve

                if self.correctsandwich == list(reversed(self.madesandwich)):
                    if self.suspicion > 0:
                        self.suspicion -= 1
                    self.surface.blit(            
                    resources.FONT.render("Correct!!", True, (0, 0, 0)),
                    (10, 60),
                    )
                    self.character.text = random.choice(resources.SCRIPT_TAKE_SANDWICH)
                else:
                    
                    self.suspicion += 1
                    self.surface.blit(            
                    resources.FONT.render("Incorrect!!", True, (0, 0, 0)),
                    (10, 60),
                    )
                    self.character.text = random.choice(resources.SCRIPT_TAKE_SANDWICH_RUDE)

                self.character.blit_onto(
                    self.surface,
                    self.character_pos
                )
                self.surface.blit(resources.COUNTER_SCREEN_IMAGE, (0, 0)) # so the customer is under the counter

                message = "Suspicion Levels: " + str(self.suspicion)
                self.surface.blit(            
                    resources.FONT.render(message, True, (0, 0, 0)),
                    (10, 85),
                    )
                if self.suspicion == 3:
                    pygame.event.post(util.make_transition_event("gameover"))
                self.madesandwich = ["Bread"]
                self.correctsandwich = []
                self.sandwichmade = False
                #self.status = "Get Order"
                #change to counter button
                #if suspician is over 5 then ooooooo game over?

        if self.status == "Counter" and self.newOrder == True:
            GamePlay.sandwich(self, self.surface)
            self.newOrder = False
        elif self.status == "Food" :
            GamePlay.displaysandwich(self.surface, self.correctsandwich)
            variationlr = random.randrange(0,15)
            variationud = random.randrange(0,15)
            if self.ham_button.blit_onto(self.surface, (100, 200)):
                self.surface.blit(resources.SUB_HAM_SPRITE_10X, (300 + variationlr, 300 + variationud))
                self.madesandwich.append("Ham")
            elif self.tomato_button.blit_onto(self.surface, (300, 200)):
                self.surface.blit(resources.SUB_TOMATO_SPRITE_10X, (300 + variationlr, 300 + variationud))
                self.madesandwich.append("Tomatoes")
            elif self.lettuce_button.blit_onto(self.surface, (500, 200)):
                self.surface.blit(resources.SUB_LETTUCE_SPRITE_10X, (300 + variationlr, 300 + variationud))
                self.madesandwich.append("Lettuce")
            elif self.top_button.blit_onto(self.surface, (700, 200)):
                self.surface.blit(resources.SUB_TOP_SPRITE_10X, (300 + variationlr, 300 + variationud))
                self.madesandwich.append("Bread")
            '''elif self.cheese_button.blit_onto(self.surface, (700, 200)):
                self.surface.blit(resources.SUB_CHEESE_SPRITE_10X, (300 + variationlr, 300 + variationud))
                self.madesandwich.append("Cheese")'''
            self.sandwichmade == True




