# src/ui/button.py

from .ui_element import UIElement
from typing import Tuple
import pygame as pg

class Button(UIElement):
    def __init__(self, pos: Tuple[float, float], color_fill: pg.typing.ColorLike, box: Tuple[float, float], 
                 visible: bool = True, text: str = "", text_color: pg.typing.ColorLike = pg.Color("white"), 
                 font: pg.font.Font = None, action = None):
        super().__init__(pos, visible)
        self.text = text
        self.text_color = text_color
        self.font = font
        self.color_fill = color_fill
        self.rect = pg.Rect(pos, box)
        self.hovered = False
        self.pressed = False
        self.clicked = False
        self.action = action

    def render(self, surface):
        if self.visible:
            button_surf = pg.Surface(self.rect.size, pg.SRCALPHA)
            button_surf.fill(self.color_fill)

            #pg.draw.rect(surface, self.color_fill, self.rect)
            if self.text and self.font:
                text_surf = self.font.render(self.text, True, self.text_color)
                text_rect = text_surf.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
                button_surf.blit(text_surf, text_rect)
            
            surface.blit(button_surf, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.pressed:
                self.clicked = True
            self.pressed = False

    def poll_clicked(self) -> bool:
        if self.clicked:
            self.clicked = False
            return True
        return False

    def is_hovered(self) -> bool:
        return self.hovered
    
    def set_text(self, new_text: str):
        self.text = new_text
    