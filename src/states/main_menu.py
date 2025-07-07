# src/states/main_menu.py

import pygame as pg
from .base_state import BaseState
from ..ui.button import Button
from ..ui.button_group import ButtonGroup

class MainMenu(BaseState):
    def __init__(self, resources):
        super().__init__()
        self.RESOURCES = resources
        self.menu_font = self.RESOURCES["FONTS"]["main_font"]
        self.bg_image = pg.image.load("assets/images/backgrounds/mainmenu_background.png").convert()
        
        self.btn_container = ButtonGroup(
            pos=(300, 200),
            button_size=(200, 60),
            spacing=15,
            orientation="vertical",
        )
        self.btn_container.add_button(
            text="Start",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.start_game,
        )
        self.btn_container.add_button(
            text="Settings",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.open_settings,
        )
        self.btn_container.add_button(
            text="Exit",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
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
        screen.blit(self.bg_image, (0, 0))
        self.btn_container.render(screen)