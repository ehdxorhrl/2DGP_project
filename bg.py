from pico2d import *
import Ingame
import server

class Background:
    def __init__(self):
        self.image = load_image('background_athletics.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w * 2  # 1600
        self.h = self.image.h * 2  # 266
    def update(self):
        self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, 1200)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, 0, self.cw//2, self.ch//2, 0, 0, self.cw, self.ch)
        # self.image.clip_draw(0, 0, 400, 266, 400, 266, 800, 532)


