import pygame as pg
from .base_state import BaseState
from ..ui.button_group import ButtonGroup

class SettingsMenu(BaseState):
    def __init__(self, context): 
        super().__init__(context)
        self.RESOURCES = context.resources

        screen_width, screen_height = context.screen.get_size()
        font_size = int(screen_height * 0.05)
        self.menu_font = pg.font.Font(self.RESOURCES["FONTS"]["main_font_path"], font_size)

        button_width = screen_width // 4.5
        button_height = screen_height // 15
        button_size = (button_width, button_height)
        padding = 20
        spacing = int(screen_height * 0.02)
        pos_y = (screen_height - 3*button_height - 2*padding - 2*spacing) / 2
        pos_x = (screen_width - button_width - 2*padding) / 2

        self.btn_container = ButtonGroup(
            pos=(pos_x, pos_y),
            button_size=button_size,
            spacing=spacing,
            orientation="vertical",
            padding=padding,
            bg_color=pg.Color("black")
        )
        self.btn_container.add_button(
            text="Video",
            color_fill=pg.Color("grey"),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.video_submenu,
        )

    def handle_event(self, event):
        self.btn_container.handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.quit = True

    def update(self, dt):
        self.btn_container.update(dt)

    def render(self, screen):
        self.btn_container.render(screen)

    def video_submenu(self): pass