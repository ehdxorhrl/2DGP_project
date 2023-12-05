from pico2d import open_canvas, delay, close_canvas
import game_framework

import title as start_mode

open_canvas(800, 532)
game_framework.run(start_mode)
close_canvas()
