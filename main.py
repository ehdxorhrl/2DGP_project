from pico2d import open_canvas, delay, close_canvas
import game_framework

# import Ingame as start_mode
import title as start_mode
# import shooting as start_modea
# import record_sort as start_mode

open_canvas(800, 532)
game_framework.run(start_mode)
close_canvas()
