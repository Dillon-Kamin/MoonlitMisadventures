# src/ui/button_group.py

from .ui_element import UIElement
import pygame as pg
from src.ui.button import Button
from typing import List, Tuple

class ButtonGroup(UIElement):
    def __init__(self, pos: Tuple[int, int], button_size: Tuple[int, int], spacing: int = 10, 
                 orientation: str = "vertical", padding: int = 10, visible: bool = True):
        super().__init__(pos, visible)
        self.pos = pos
        self._cursor = list(self.pos)
        self.button_size = button_size
        self.spacing = spacing
        self.padding = padding
        self.orientation = orientation
        self.buttons: List[Button] = []
        self.width = 0
        self.height = 0
    
    def add_button(self, color_fill: pg.typing.ColorLike, font: pg.font.Font, text: str = "", 
                   text_color: pg.typing.ColorLike = "white", action = None):
        num_buttons = len(self.buttons)

        # USE CURSOR INSTEAD
        if self.orientation == "vertical":
            self.height += self.button_size[1]
            if num_buttons == 0:
                self._cursor[0] += self.padding
                self._cursor[1] += self.padding
                self.height += self.padding * 2 
                self.width += self.padding * 2 + self.button_size[0]
            else:
                self._cursor[1] += self.spacing + self.button_size[1]
                self.height += self.spacing
        else:
            assert(self.orientation == "horizontal", "ERROR::button_group.py::add_button:Unhandled button orientation.")
            self.width += self.button_size[0]
            if num_buttons == 0:
                self._cursor[0] += self.padding
                self._cursor[1] += self.padding
                self.width += self.padding * 2 
                self.height += self.padding * 2 + self.button_size[1]
            else:
                self._cursor[0] += self.spacing + self.button_size[0]
                self.width += self.spacing
        
        new_btn = Button(self._cursor, color_fill=color_fill, box=self.button_size, visible=self.visible, 
                            text=text, text_color=text_color, font=font, action=action)
        self.buttons.append(new_btn)

    def handle_event(self, event):
        for btn in self.buttons:
            btn.handle_event(event)
    
    def update(self, dt):
        for btn in self.buttons:
            if btn.poll_clicked():
                if btn.action:
                    btn.action()
                    
    def render(self, surface):
        if not self.visible:
            return
        else:
            # draw own border box (no fill/translucent)
            for btn in self.buttons:
                btn.render(surface)
