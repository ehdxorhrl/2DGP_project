import random

from pico2d import *
import game_framework

import Game_World
from bg import Background
from Athletics import Boy
from hurdle import Hurdle


# boy = None

def handle_events():
    global boy
    global hurdle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            boy.x = 50
            hurdle.state = 'stand'
            pass
        else:
            boy.handle_event(event)
            pass

def init():
    # global grass
    global boy
    global background1
    global hurdle

    running = True

    background1 = Background()
    Game_World.add_object(background1, 0)

    boy = Boy()
    Game_World.add_object(boy, 2)

    hurdle = Hurdle()
    Game_World.add_object(hurdle, 1)

    # fill here
def finish():
    Game_World.clear()
    pass


def update():
    global hurdle
    Game_World.update()
    if hurdle.state == 'stand':
        if Game_World.collide(boy, hurdle):
            hurdle.state = 'lay_down'
            boy.state_machine.handle_event(('lay_down', 0))


    # fill here

def draw():
    clear_canvas()
    Game_World.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

