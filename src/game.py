# src/game.py

import pygame as pg

from src.states.main_menu import MainMenu

class Game:
    def __init__(self, SETTINGS, RESOURCES):
        self.screen = pg.display.set_mode(
            (SETTINGS["video"]["resolution"]["width"], SETTINGS["video"]["resolution"]["height"]),
            pg.FULLSCREEN if SETTINGS["video"]["fullscreen"] else 0 
        )
        self.clock = pg.time.Clock()
        self.state_stack = [MainMenu(RESOURCES, screen=self.screen)]
        self.gameRunning = True
    
    def run(self):
        while self.gameRunning:
            dt = self.clock.tick(60) / 1000
            current_state = self.state_stack[-1]

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.gameRunning = False
                current_state.handle_event(event)

            current_state.update(dt)

            # render all states in the state stack (may change later or have some visibility variable in state to determine)
            for state in self.state_stack:
                state.render()
            pg.display.flip()

            if current_state.quit:
                next_state = current_state.next_state

                if current_state.persist_on_quit == False:
                    self.state_stack.pop()

                if next_state:
                    self.state_stack.append(next_state)

                if not self.state_stack:
                    self.gameRunning = False
                