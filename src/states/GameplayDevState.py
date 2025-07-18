########### For testing gameplay 
from .base_state import BaseState

class GamePlayState(BaseState):
    def __init__(self, context):
        self.context = context
        self.quit = False
        self.player = Player(...)
        self.level = Level(...)
    
    def handle_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.quit = True
        self.player.handle_event(event)

    def update(self, dt):
        self.player.update(dt)

    def render(self, screen):
        self.level.render(screen)
        self.player.render(screen)