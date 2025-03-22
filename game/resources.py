import pygame
import os
from pathlib import Path

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

pygame.font.init()

FONT = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=40)

SPLASH_SCREEN_IMAGE = pygame.image.load(RESOURCES_DIR / "splash.png")