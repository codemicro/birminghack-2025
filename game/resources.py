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
SUB_PAPER_SPRITE =  pygame.image.load(RESOURCES_DIR / "sprites" / "sub_wrap.png")
SUB_PAPER_SPRITE_3X = pygame.transform.scale_by(SUB_PAPER_SPRITE, 6)

SUB_TOMATO_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_tomato.png")
SUB_TOMATO_SPRITE_3X = pygame.transform.scale_by(SUB_TOMATO_SPRITE, 3)
SUB_TOMATO_SPRITE_10X = pygame.transform.scale_by(SUB_TOMATO_SPRITE, 10)
TICKET_TOMATO_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_tomato.png")
TICKET_TOMATO_SPRITE_3X = pygame.transform.scale_by(TICKET_TOMATO_SPRITE, 2)

SUB_HAM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_ham.png")
SUB_HAM_SPRITE_3X = pygame.transform.scale_by(SUB_HAM_SPRITE, 3)
SUB_HAM_SPRITE_10X = pygame.transform.scale_by(SUB_HAM_SPRITE, 10)
TICKET_HAM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_ham.png")
TICKET_HAM_SPRITE_3X = pygame.transform.scale_by(TICKET_HAM_SPRITE, 3)


SUB_LETTUCE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_lettuce.png")
SUB_LETTUCE_SPRITE_3X = pygame.transform.scale_by(SUB_LETTUCE_SPRITE, 3)
SUB_LETTUCE_SPRITE_10X = pygame.transform.scale_by(SUB_LETTUCE_SPRITE, 10)
TICKET_LETTUCE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_lettuce.png")
TICKET_LETTUCE_SPRITE_3X = pygame.transform.scale_by(TICKET_LETTUCE_SPRITE, 2)

SUB_TOP_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_top.png")
SUB_TOP_SPRITE_3X = pygame.transform.scale_by(SUB_TOP_SPRITE, 3)
SUB_TOP_SPRITE_10X = pygame.transform.scale_by(SUB_TOP_SPRITE, 10)
TICKET_TOP_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_top.png")
TICKET_TOP_SPRITE_3X = pygame.transform.scale_by(TICKET_TOP_SPRITE, 3)

SUB_BOTTOM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_bottom.png")
SUB_BOTTOM_SPRITE_10X = pygame.transform.scale_by(SUB_BOTTOM_SPRITE, 10)

TICKET_BOTTOM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "ticket_bottom.png")
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
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_glasses_4.png"), # the blank one
]

CHARACTER_HAIR = [
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_1.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_2.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_3.png"),
    pygame.image.load(RESOURCES_DIR / "sprites" / "character_hair_4.png"), # the bald one
]