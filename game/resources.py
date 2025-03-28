import pygame
import os
from pathlib import Path

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

pygame.font.init()

FONT_SM = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=20)
FONT = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=40)
FONT_LG = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=60)
FONT_XL = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=100)

DRAWER_TRANS = pygame.image.load(RESOURCES_DIR / "drawer_button.png")
DRAWER_OPEN = pygame.image.load(RESOURCES_DIR / "drawer.png")

SPLASH_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "splash.png")
COUNTER_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "counter.png")
PREPARE_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "prepare.png")
BACKGROUND_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "background.png")
SUB_WRAPPED_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_wrapped.png")
SUB_WRAPPED_SPRITE_3X = pygame.transform.scale_by(SUB_WRAPPED_SPRITE, 5)
SUB_PAPER_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_wrap.png")
SUB_PAPER_SPRITE_3X = pygame.transform.scale_by(SUB_PAPER_SPRITE, 6)

SUB_TOMATO_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_tomato.png")
SUB_TOMATO_SPRITE_3X = pygame.transform.scale_by(SUB_TOMATO_SPRITE, 3)
SUB_TOMATO_SPRITE_10X = pygame.transform.scale_by(SUB_TOMATO_SPRITE, 10)
TUB_TOMATO_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "tub_tomato.png")
TUB_TOMATO_SPRITE_3X = pygame.transform.scale_by(TUB_TOMATO_SPRITE, 3)
TICKET_TOMATO_SPRITE = pygame.image.load(
    RESOURCES_DIR / "sprites" / "ticket_tomato.png"
)
TICKET_TOMATO_SPRITE_3X = pygame.transform.scale_by(TICKET_TOMATO_SPRITE, 2)

SUB_HAM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_ham.png")
SUB_HAM_SPRITE_3X = pygame.transform.scale_by(SUB_HAM_SPRITE, 3)
SUB_HAM_SPRITE_10X = pygame.transform.scale_by(SUB_HAM_SPRITE, 10)
TUB_HAM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "tub_ham.png")
TUB_HAM_SPRITE_3X = pygame.transform.scale_by(TUB_HAM_SPRITE, 3)
TICKET_HAM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_ham.png")
TICKET_HAM_SPRITE_3X = pygame.transform.scale_by(TICKET_HAM_SPRITE, 3)


SUB_LETTUCE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_lettuce.png")
SUB_LETTUCE_SPRITE_3X = pygame.transform.scale_by(SUB_LETTUCE_SPRITE, 3)
SUB_LETTUCE_SPRITE_10X = pygame.transform.scale_by(SUB_LETTUCE_SPRITE, 10)
TUB_LETTUCE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "tub_lettuce.png")
TUB_LETTUCE_SPRITE_3X = pygame.transform.scale_by(TUB_LETTUCE_SPRITE, 3)
TICKET_LETTUCE_SPRITE = pygame.image.load(
    RESOURCES_DIR / "sprites" / "ticket_lettuce.png"
)
TICKET_LETTUCE_SPRITE_3X = pygame.transform.scale_by(TICKET_LETTUCE_SPRITE, 2)

SUB_CHEESE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_cheese.png")
SUB_CHEESE_SPRITE_3X = pygame.transform.scale_by(SUB_CHEESE_SPRITE, 3)
SUB_CHEESE_SPRITE_10X = pygame.transform.scale_by(SUB_CHEESE_SPRITE, 6)
TUB_CHEESE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "tub_cheese.png")
TUB_CHEESE_SPRITE_3X = pygame.transform.scale_by(TUB_CHEESE_SPRITE, 3)
TICKET_CHEESE_SPRITE = pygame.image.load(
    RESOURCES_DIR / "sprites" / "ticket_cheese.png"
)
TICKET_CHEESE_SPRITE_3X = pygame.transform.scale_by(TICKET_CHEESE_SPRITE, 2)


SUB_TOP_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_top.png")
SUB_TOP_SPRITE_3X = pygame.transform.scale_by(SUB_TOP_SPRITE, 3)
SUB_TOP_SPRITE_10X = pygame.transform.scale_by(SUB_TOP_SPRITE, 10)
TUB_TOP_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "tub_top.png")
TUB_TOP_SPRITE_3X = pygame.transform.scale_by(TUB_TOP_SPRITE, 3)
TICKET_TOP_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_top.png")
TICKET_TOP_SPRITE_3X = pygame.transform.scale_by(TICKET_TOP_SPRITE, 3)

SUB_BOTTOM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_bottom.png")
SUB_BOTTOM_SPRITE_10X = pygame.transform.scale_by(SUB_BOTTOM_SPRITE, 10)

TICKET_BOTTOM_SPRITE = pygame.image.load(
    RESOURCES_DIR / "sprites" / "ticket_bottom.png"
)
TICKET_BOTTOM_SPRITE_3X = pygame.transform.scale_by(TICKET_BOTTOM_SPRITE, 3)

CHARACTER_TORSOS = [
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_torso_1.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_torso_2.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_torso_3.png"),
]

CHARACTER_HEADS = [
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_head_1.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_head_2.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_head_3.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_head_4.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_head_5.png"),
]

CHARACTER_GLASSES = [
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_glasses_1.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_glasses_2.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_glasses_3.png"),
    pygame.image.load(
        RESOURCES_DIR / "sprites" / "character_glasses_4.png"
    ),  # the blank one
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_glasses_5.png"),
]

CHARACTER_HAIR = [
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_1.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_2.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_3.png"),
    pygame.image.load(
        RESOURCES_DIR / "sprites" / "character_hair_4.png"
    ),  # the bald one
]

EMPTY_NOTE = pygame.image.load(RESOURCES_DIR / "empty_note.png") 

SCRIPT_ASK_SANDWICH = (
    open(RESOURCES_DIR / "scripts" / "ask-sandwich.txt").read().strip().splitlines()
)
SCRIPT_TAKE_SANDWICH = (
    open(RESOURCES_DIR / "scripts" / "take-sandwich.txt").read().strip().splitlines()
)
SCRIPT_TAKE_SANDWICH_RUDE = (
    open(RESOURCES_DIR / "scripts" / "take-sandwich-rude.txt").read().strip().splitlines()
)
SCRIPT_GAME_OVER = (
    open(RESOURCES_DIR / "scripts" / "game-over.txt").read().strip().splitlines()
)
