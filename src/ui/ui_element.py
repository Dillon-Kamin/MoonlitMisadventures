# src/ui/ui_element.py

from typing import Tuple

class UIElement:
    def __init__(self, pos: Tuple[float, float], visible):
        self.pos = pos
        self.visible = visible

    def render(self, surface):
        raise NotImplementedError

    def handle_event(self, event):
        raise NotImplementedError

    def update(self, dt):
        raise NotImplementedError
