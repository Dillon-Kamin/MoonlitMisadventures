# src/main.py

import pygame
import sys

from src.settings import Settings
from src.resources import Resources
from src.game import Game

def main():
    pygame.init()
    pygame.display.set_caption("Moonlit Misadventures")

    # Load config and resources
    SETTINGS = Settings().settings
    RESOURCES = Resources().resources

    game = Game(SETTINGS, RESOURCES)
    game.run()