import pygame as pg

from .base_state import BaseState
from ..ui.button_group import ButtonGroup

class SettingsMenu(BaseState):
    def __init__(self, context): 
        super().__init__(context)
        self.context = context
        self.RESOURCES = context.resources
        self.active_submenu = None
        self.resize()

    def resize(self):
        screen_width, screen_height = self.context.screen.get_size()
        font_size = int(screen_height * 0.05)
        self.menu_font = pg.font.Font(self.RESOURCES["FONTS"]["main_font_path"], font_size)

        button_width = screen_width // 4.5
        button_height = screen_height // 15
        button_size = (button_width, button_height)
        padding = 20
        spacing = int(screen_height * 0.02)
        pos_y = (screen_height - 3 * button_height - 2 * padding - 2 * spacing) / 2
        pos_x = (screen_width - button_width - 2 * padding) / 2

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
        self.btn_container.add_button(
            text="Audio",
            color_fill=pg.Color("grey"),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.audio_submenu,
        )

        if self.active_submenu:
            self.active_submenu.resize()

    def handle_event(self, event):
        if self.active_submenu:
            self.active_submenu.handle_event(event)
        else:
            self.btn_container.handle_event(event)
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.quit = True

    def update(self, dt):
        if self.active_submenu:
            self.active_submenu.update(dt)

            if self.active_submenu.quit == True:
                self.active_submenu = None

        else:
            self.btn_container.update(dt)

    def render(self, screen):
        if self.active_submenu:
            self.active_submenu.render(screen)
        else:
            self.btn_container.render(screen)

    def video_submenu(self): 
        self.active_submenu = VideoSettingsSubmenu(self.context)
    
    def audio_submenu(self): 
        self.active_submenu = AudioSettingsSubmenu(self.context)


class AudioSettingsSubmenu:
    def __init__(self, context):
        self.context = context
        self.RESOURCES = context.resources
        self.quit = False

    def resize(self):
        pass

    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.quit = True

    def update(self, dt):
        pass

    def render(self, screen):
        pass

class VideoSettingsSubmenu:
    def __init__(self, context):
        self.context = context
        self.RESOURCES = context.resources
        self.quit = False
        self.resize()

    def resize(self):
        screen_width, screen_height = self.context.screen.get_size()
        font_size = int(screen_height * 0.04)
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
        self.resolution_button = self.btn_container.add_button(
            text=f"Resolution: {screen_width}x{screen_height}",
            color_fill=pg.Color("grey"),
            text_color=pg.Color("white"),
            font=self.menu_font,
            action=self.change_resolution,
        )

    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.quit = True

        self.btn_container.handle_event(event)

    def update(self, dt):
        self.btn_container.update(dt)

    def render(self, screen):
        self.btn_container.render(screen)

    def change_resolution(self):
        available_resolutions = self.context.resolutions
        idx_current = self.context.current_resolution_index
        resolution_next = available_resolutions[(idx_current + 1) % len(available_resolutions)]
        w, h = resolution_next

        self.context.set_screen(resolution_next)
        self.resolution_button.set_text(f"Resolution: {w}x{h}")
        self.context.resize()
