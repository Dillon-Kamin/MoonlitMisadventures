# src/entities/player.py
import pygame as pg

class Player:
    def __init__(self, x, y, speed=200):
        self.rect = pg.Rect(x, y, 32, 32)
        self.color = pg.Color("dodgerblue")
        self.speed = speed

    def handle_event(self, event):
        pass

    def update(self, dt, keys):
        dx = dy = 0
        if keys[pg.K_w]: dy -= self.speed * dt
        if keys[pg.K_s]: dy += self.speed * dt
        if keys[pg.K_a]: dx -= self.speed * dt
        if keys[pg.K_d]: dx += self.speed * dt
        self.rect.x += dx
        self.rect.y += dy

    def render(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
