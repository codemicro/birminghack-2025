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