# src/states/main_menu.py

import pygame as pg

from .base_state import BaseState
from .settings_menu import SettingsMenu
from ..ui.button_group import ButtonGroup

class MainMenu(BaseState):
    def __init__(self, context):
        super().__init__(context)
        self.RESOURCES = context.resources
        self.resize()

    def resize(self):
        screen_width, screen_height = self.context.screen.get_size()
        font_size = int(screen_height * 0.05)
        self.menu_font = pg.font.Font(self.RESOURCES["FONTS"]["main_font_path"], font_size)
        
        self.bg_image = pg.transform.scale(pg.image.load("assets/images/backgrounds/mainmenu_background.png"), self.context.screen.get_size()).convert()
        
        button_width = screen_width // 4.5
        button_height = screen_height // 15
        button_size = (button_width, button_height)
        padding = 20
        pos_y = 0
        pos_x = screen_width - button_width - 2*padding
        spacing = int(screen_height * 0.02)

        self.btn_container = ButtonGroup(
            pos=(pos_x, pos_y),
            button_size=button_size,
            spacing=spacing,
            orientation="vertical",
            padding=padding,
            bg_color=pg.Color(self.RESOURCES["COLORS"]["clear"])
        )
        self.btn_container.add_button(
            text="New Game",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["somewhat_clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.new_game,
        )
        self.btn_container.add_button(
            text="Load Game",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["somewhat_clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.load_game,
        )
        self.btn_container.add_button(
            text="Settings",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["somewhat_clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.open_settings,
        )
        self.btn_container.add_button(
            text="Exit",
            color_fill=pg.Color(self.RESOURCES["COLORS"]["somewhat_clear"]),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.exit_game,
        )

    def handle_event(self, event):
        self.btn_container.handle_event(event)

    def update(self, dt):
        self.btn_container.update(dt)

    def render(self, screen):
        screen.blit(self.bg_image, (0, 0))
        self.btn_container.render(screen)

    def exit_game(self):
        self.persist_on_quit = False
        self.quit = True
        print("Exiting...")
            
    def new_game(self):
        self.persist_on_quit = False
        self.quit = True
        print("Starting New Game...")

    def load_game(self):
        self.persist_on_quit = True
        self.quit = True
        print("Loading Game...")

    def open_settings(self):
        self.persist_on_quit = True
        self.quit = True
        self.next_state = SettingsMenu(self.context)

    
