import random
from pico2d import *
import game_framework

from Scene import PATTERN
import Game_World
from bg import Background
from Athletics import Boy
from hurdle import Hurdle
import server
import shooting
from record import PLAY_TIME

def handle_events():
    global hurdles
    global phase
    global pattern
    global pt

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
                for hurdle in hurdles:
                    hurdle.state = 'stand'
                pass
            else:
                if server.play_time.start_time <= -0.5:
                    server.boy.handle_event(event)
    elif phase == 1:
        events = get_events()
        for event in events:
            if pattern == False:
                if event.type == SDL_QUIT:
                    game_framework.quit()
                elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    game_framework.quit()
                elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
                    server.boy.start_time = 2.5
                    server.boy.play_time = 0
                    server.boy.x = 10
                    phase = 0
                    for hurdle in hurdles:
                        hurdle.state = 'stand'
                    pass
                else:
                    server.boy.handle_event(event)
            elif pattern == True:
                if event.type == SDL_KEYDOWN:
                    if event.key == SDLK_LEFT or event.key == SDLK_RIGHT or event.key == SDLK_UP or event.key == SDLK_DOWN:  # 왼쪽 화살표 키인지 확인
                        if pt.result_list[pt.pattern_num][pt.pattern_index] == event.key:
                            pt.result_list[pt.pattern_num][pt.pattern_index] = 0
                            pt.pattern_index += 1
                        else:
                            pt.pattern_index = 0
                            pt.set_patter()
def init():
    # global grass
    global hurdles
    global start_time
    global phase
    global pattern
    global pt

    pattern = False
    phase = 1
    running = True
    start_time = 3

    pt = PATTERN()
    Game_World.add_object(pt, 1)

    server.background = Background()
    Game_World.add_object(server.background, 0)

    server.play_time = PLAY_TIME()
    Game_World.add_object(server.play_time, 2)

    server.boy = Boy()
    Game_World.add_object(server.boy, 2)

    positions = [300, 700, 1100]
    hurdles = []

    for pos in positions:
        hurdle = Hurdle()
        Game_World.add_object(hurdle, 1)
        hurdle.x = pos
        hurdles.append(hurdle)

    server.boy.set_background(server.background)
    for hurdle in hurdles:
        hurdle.set_background(server.background)

    # fill here
def finish():
    Game_World.clear()
    pass


def update():
    global hurdles
    global phase
    global pattern
    Game_World.update()
    if phase == 0:
        for hurdle in hurdles:
            if hurdle.state == 'stand' and Game_World.collide(server.boy, hurdle):
                hurdle.state = 'lay_down'
                server.boy.state_machine.handle_event(('lay_down', 0))
        if server.boy.x >= 2000:
            positions = [150, 500, 700, 1400]
            phase = 1
            server.boy.x = 0
            for hurdle in hurdles:
                hurdle.state = 'stand'

            for pos in positions:
                hurdle = Hurdle()
                Game_World.add_object(hurdle, 1)
                hurdle.x = pos
                hurdles.append(hurdle)

    elif phase == 1:
        if pattern == False:
            for hurdle in hurdles:
                if hurdle.state == 'stand' and Game_World.collide(server.boy, hurdle):
                    pattern = True


def draw():
    clear_canvas()
    Game_World.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

