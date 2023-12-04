import random
from pico2d import *
import game_framework

import Game_World
from bg import Background
from Athletics import Boy
from hurdle import Hurdle
import server
import shooting
from record import PLAY_TIME

phase = 0

def handle_events():
    global hurdle
    global phase

    if phase == 0:
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
                server.boy.start_time = 2.5
                server.boy.play_time = 0
                server.boy.x = 10
                hurdle1.state = 'stand'
                hurdle2.state = 'stand'
                hurdle3.state = 'stand'
                pass
            else:
                if server.play_time.start_time <= -0.5:
                    server.boy.handle_event(event)
    elif phase == 1:
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
                server.boy.start_time = 2.5
                server.boy.play_time = 0
                server.boy.x = 10
                phase = 0
                hurdle1.state = 'stand'
                hurdle2.state = 'stand'
                hurdle3.state = 'stand'
                pass
            else:
                if server.play_time.start_time <= -0.5:
                    server.boy.handle_event(event)
def init():
    # global grass
    global hurdle1
    global hurdle2
    global hurdle3
    global start_time
    global phase

    phase = 0
    running = True
    start_time = 3

    server.background = Background()
    Game_World.add_object(server.background, 0)

    server.play_time = PLAY_TIME()
    Game_World.add_object(server.play_time, 2)

    server.boy = Boy()
    Game_World.add_object(server.boy, 2)

    hurdle1 = Hurdle()
    Game_World.add_object(hurdle1, 1)
    hurdle1.x = 200

    hurdle2 = Hurdle()
    Game_World.add_object(hurdle2, 1)
    hurdle2.x = 700

    hurdle3 = Hurdle()
    Game_World.add_object(hurdle3, 1)
    hurdle3.x = 1100

    server.boy.set_background(server.background)
    hurdle1.set_background(server.background)
    hurdle2.set_background(server.background)
    hurdle3.set_background(server.background)

    # fill here
def finish():
    Game_World.clear()
    pass


def update():
    global hurdle1
    global hurdle2
    global hurdle3
    global phase
    Game_World.update()
    if hurdle1.state == 'stand':
        if Game_World.collide(server.boy, hurdle1):
            hurdle1.state = 'lay_down'
            server.boy.state_machine.handle_event(('lay_down', 0))
    if hurdle2.state == 'stand':
        if Game_World.collide(server.boy, hurdle2):
            hurdle2.state = 'lay_down'
            server.boy.state_machine.handle_event(('lay_down', 0))
    if hurdle3.state == 'stand':
        if Game_World.collide(server.boy, hurdle3):
            hurdle3.state = 'lay_down'
            server.boy.state_machine.handle_event(('lay_down', 0))
    if server.boy.x >= 2000 and phase == 0:
        phase = 1
        server.boy.x = 0
        hurdle1.state = 'stand'
        hurdle2.state = 'stand'
        hurdle3.state = 'stand'


def draw():
    clear_canvas()
    Game_World.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

