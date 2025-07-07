# src/states/main_menu.py

import pygame as pg
from ..engine_types import CLEAR
from .base_state import BaseState
from ..ui.button import Button
from ..ui.button_group import ButtonGroup

class MainMenu(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pg.font.SysFont("arial", 40)
        
        self.btn_container = ButtonGroup(
            pos=(300, 200),
            button_size=(200, 60),
            spacing=15,
            orientation="vertical",
        )
        self.btn_container.add_button(
            text="Start",
            color_fill=pg.Color(CLEAR),
            text_color=pg.Color("white"),
            font=self.font,
            action=self.start_game,
        )
        self.btn_container.add_button(
            text="Settings",
            color_fill=pg.Color(CLEAR),
            text_color=pg.Color("white"),
            font=self.font,
            action=self.open_settings,
        )
        self.btn_container.add_button(
            text="Exit",
            color_fill=pg.Color(CLEAR),
            text_color=pg.Color("white"),
            font=self.font,
            action=self.exit_game,
        )

    def start_game(self):
        print("Starting game...")

    def open_settings(self):
        print("Opening settings...")

    def exit_game(self):
        self.quit = True

    def handle_event(self, event):
        self.btn_container.handle_event(event)

    def update(self, dt):
        self.btn_container.update(dt)

    def render(self, screen):
        screen.fill("black")
        self.btn_container.render(screen)