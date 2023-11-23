from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background_athletics.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 400, 266, 400, 266, 800, 532)


