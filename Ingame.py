import random
from pico2d import *
import game_framework

import Game_World
from bg import Background
from Athletics import Boy
from hurdle import Hurdle
import server

def handle_events():
    global hurdle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            server.boy.x = 50
            hurdle.state = 'stand'
            pass
        else:
            server.boy.handle_event(event)
            pass

def init():
    # global grass
    global hurdle

    running = True

    server.background = Background()
    Game_World.add_object(server.background, 0)

    server.boy = Boy()
    Game_World.add_object(server.boy, 2)

    hurdle = Hurdle()
    Game_World.add_object(hurdle, 1)

    server.boy.set_background(server.background)
    hurdle.set_background(server.background)

    # fill here
def finish():
    Game_World.clear()
    pass


def update():
    global hurdle
    Game_World.update()
    if hurdle.state == 'stand':
        if Game_World.collide(server.boy, hurdle):
            hurdle.state = 'lay_down'
            server.boy.state_machine.handle_event(('lay_down', 0))

def draw():
    clear_canvas()
    Game_World.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

