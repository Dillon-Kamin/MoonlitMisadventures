# main.py

import pygame
import sys
from src.settings import Settings

# Load video config
SETTINGS_VIDEO = Settings().video
res = SETTINGS_VIDEO["resolution"]
fullscreen = SETTINGS_VIDEO["fullscreen"]

pygame.init()

fullscreen_flag = pygame.FULLSCREEN if fullscreen else False
screen = pygame.display.set_mode((res["width"], res["height"]), fullscreen_flag)
pygame.display.set_caption("Moonlit Misadventures")

clock = pygame.time.Clock()
gameRunning = True

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    screen.fill("white")
    pygame.display.flip()
    clock.tick(30)
