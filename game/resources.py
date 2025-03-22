import pygame
import os
from pathlib import Path

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

pygame.font.init()

FONT_SM = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=20)
FONT = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=40)
FONT_LG = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=60)
FONT_XL = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=100)

SPLASH_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "splash.png")
COUNTER_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "counter.png")

SUB_TOMATO_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_tomato.png")
SUB_TOMATO_SPRITE_3X = pygame.transform.scale_by(SUB_TOMATO_SPRITE, 3)
SUB_TOMATO_SPRITE_10X = pygame.transform.scale_by(SUB_TOMATO_SPRITE, 10)

SUB_HAM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_ham.png")
SUB_HAM_SPRITE_3X = pygame.transform.scale_by(SUB_HAM_SPRITE, 3)
SUB_HAM_SPRITE_10X = pygame.transform.scale_by(SUB_HAM_SPRITE, 10)


SUB_LETTUCE_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_lettuce.png")
SUB_LETTUCE_SPRITE_3X = pygame.transform.scale_by(SUB_LETTUCE_SPRITE, 3)
SUB_LETTUCE_SPRITE_10X = pygame.transform.scale_by(SUB_LETTUCE_SPRITE, 10)

SUB_TOP_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_top.png")
SUB_TOP_SPRITE_3X = pygame.transform.scale_by(SUB_TOP_SPRITE, 3)
SUB_TOP_SPRITE_10X = pygame.transform.scale_by(SUB_TOP_SPRITE, 10)

SUB_BOTTOM_SPRITE = pygame.image.load(RESOURCES_DIR / "sprites" / "sub_bottom.png")
SUB_BOTTOM_SPRITE_10X = pygame.transform.scale_by(SUB_BOTTOM_SPRITE, 10)

