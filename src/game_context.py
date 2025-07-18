# src/game_context.py

class GameContext:
    def __init__(self, screen, resources, set_screen, resize):
        self.screen = screen
        self.resources = resources
        self.set_screen = set_screen
        self.resize = resize

        self.resolutions = [(1280, 720), (1920, 1080)]
        self.current_resolution_index = 0
        
    def get_current_resolution(self):
        return self.resolutions[self.current_resolution_index]