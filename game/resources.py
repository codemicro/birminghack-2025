import pygame
import os
from pathlib import Path

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

pygame.font.init()

FONT = pygame.font.Font(RESOURCES_DIR / "Jersey10-Regular.ttf", size=40)
TOMATO = pygame.image.load(RESOURCES_DIR / "sprites/ticket_tomato.png")