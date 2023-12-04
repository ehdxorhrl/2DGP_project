from pico2d import *
import server
import Ingame


class Background:
    def __init__(self):
        self.image1 = load_image('배경2.png')
        self.image2 = load_image('background_athletics.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image1.w * 2  # 1600
        self.h = self.image1.h * 2  # 266
        self.window_left = 0
    def update(self):
        self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, 1200)

    def draw(self):
        if Ingame.phase == 0:
            self.image1.clip_draw_to_origin(self.window_left, 0, self.cw//2, self.ch//2, 0, 0, self.cw, self.ch)
        elif Ingame.phase == 1:
            self.image2.clip_draw_to_origin(self.window_left, 0, self.cw // 2, self.ch // 2, 0, 0, self.cw, self.ch)
        # self.image.clip_draw(0, 0, 400, 266, 400, 266, 800, 532)


