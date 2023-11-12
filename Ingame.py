import random

from pico2d import *
import game_framework

import Game_World
# from boy import Boy
from bg import Background
from Athletics import Boy


# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            # boy.handle_event(event)
            pass

def init():
    # global grass
    global boy
    global background1

    running = True

    background1 = Background()
    Game_World.add_object(background1, 0)

    boy = Boy()
    Game_World.add_object(boy, 1)

    # fill here



def finish():
    Game_World.clear()
    pass


def update():
    Game_World.update()
    # fill here

def draw():
    clear_canvas()
    Game_World.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

