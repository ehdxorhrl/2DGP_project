from pico2d import *

class Hurdle:
    def __init__(self):
        self.image = load_image('hurdle.png')
        self.x, self.y = 400, 266
        self.state = 'stand'

    def update(self):
        pass

    def draw(self):
        if self.state == 'stand':
            self.image.draw(400, 200, 100, 100)
            draw_rectangle(*self.get_bb())
        elif self.state == 'lay_down':
            self.image.rotate_draw(math.radians(270), 450, 200, 80, 100)

    def get_bb(self):
        if self.state == 'stand':
            return self.x, self.y - 70, self.x + 30, self.y - 20
        else:
            pass
