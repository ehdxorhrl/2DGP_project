from pico2d import *
import random
import Ingame

class Hurdle:
    def __init__(self):
        self.image = load_image('hurdle.png')
        self.x, self.y = random.randint(100, 1500), 266
        self.state = 'stand'
        self.sx = 0

    def set_background(self, bg):
        self.bg = bg

    def update(self):
        self.sx = (self.x - self.bg.window_left) * 2
        pass

    def draw(self):
        if self.state == 'stand':
            self.image.draw(self.sx, 200, 100, 100)
            draw_rectangle(*self.get_bb())
        elif self.state == 'lay_down':
            self.image.rotate_draw(math.radians(270), self.sx + 50, 200, 80, 100)

    def get_bb(self):
        if self.state == 'stand':
            if Ingame.phase == 0:
                return self.sx, self.y - 70, self.sx + 30, self.y - 20
            elif Ingame.phase == 1:
                return self.sx - 100, self.y - 90, self.sx - 20, self.y - 20
        else:
            pass
