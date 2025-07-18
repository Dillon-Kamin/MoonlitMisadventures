# src/entities/player.py
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # visual
        self.image = pg.Surface((32, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)

        # movement
        

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            pass
        elif keys[pg.K_DOWN]:
            pass
        if keys[pg.K_RIGHT]:
            pass
        elif keys[pg.K_LEFT]:
            pass

    def update(self, dt):
        self.input()
