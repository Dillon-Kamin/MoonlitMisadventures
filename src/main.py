# src/main.py

import pygame
import sys

from src.settings import Settings
from src.game import Game

def main():
    # Load config
    SETTINGS = Settings().settings

    pygame.init()
    pygame.display.set_caption("Moonlit Misadventures")

    game = Game(SETTINGS)
    game.run()