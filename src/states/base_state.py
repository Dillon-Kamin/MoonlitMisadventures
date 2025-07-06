# src/states/base_state.py

class BaseState:
    def __init__(self):
        self.quit = False
        self.next_state = None

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass
