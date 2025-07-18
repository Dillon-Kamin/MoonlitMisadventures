# src/game.py

import pygame as pg
import os, sys

from src.game_context import GameContext
from src.states.main_menu import MainMenu

class Game:
    def __init__(self, SETTINGS, RESOURCES):
        self.screen = pg.display.set_mode(
            (SETTINGS["video"]["resolution"]["width"], SETTINGS["video"]["resolution"]["height"]),
            pg.FULLSCREEN if SETTINGS["video"]["fullscreen"] else 0 
        )
        self.context = GameContext(screen=self.screen, resources=RESOURCES, set_screen=self.set_screen, resize=self.resize)

        self.clock = pg.time.Clock()
        self.state_stack = [MainMenu(self.context)]
        self.gameRunning = True

    def set_screen(self, new_size):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
        self.screen = pg.display.set_mode(new_size, pg.RESIZABLE)
        self.context.screen = self.screen
        if new_size in self.context.resolutions:
            self.context.current_resolution_index = self.context.resolutions.index(new_size)

    def resize(self):
        for state in self.state_stack:
            state.resize()
    
    def run(self):
        while self.gameRunning:
            dt = self.clock.tick(60) / 1000
            current_state = self.state_stack[-1]

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.gameRunning = False
                    sys.exit()
                current_state.handle_event(event)

            current_state.update(dt)

            # render all states in the state stack (may change later or have some visibility variable in state to determine)
            for state in self.state_stack:
                state.render(self.screen)
            pg.display.flip()

            if current_state.quit:
                next_state = current_state.next_state

                if current_state.persist_on_quit == False:
                    self.state_stack.pop()
                else:
                    current_state.next_state = None

                if next_state:
                    self.state_stack.append(next_state)

                if not self.state_stack:
                    self.gameRunning = False
                