from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background_athletics.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 266, 800, 532)


