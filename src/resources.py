# src/resources.py

import pygame as pg

class Resources:
    def __init__(self):
        self.resources = {}
        self.init_colors()
        self.init_fonts()
        print(self.resources)
    
    def init_colors(self):
        self.resources["COLORS"] = {"clear": pg.Color(0, 0, 0, 0)}

    def init_fonts(self):
        self.resources["FONTS"] = {"main_font": pg.font.Font("assets/fonts/_bitmap_font____romulus_by_pix3m_d6aokem.ttf", 7)}
