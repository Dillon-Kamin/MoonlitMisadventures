########### For testing gameplay 

import pygame as pg

from .base_state import BaseState
from .settings_menu import SettingsMenu
from src.entities.player import Player

class GamePlayState(BaseState):
    def __init__(self, context):
        self.context = context
        self.quit = False
        self.player = Player(100, 100)
    
    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.quit = True
            self.persist_on_quit = True
            self.next_state = SettingsMenu(self.context)

    def update(self, dt):
        keys = pg.key.get_pressed()
        self.player.update(dt, keys)

    def render(self, screen):
        screen.fill(pg.Color("darkgreen"))
        self.player.render(screen)