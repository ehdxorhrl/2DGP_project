from pico2d import *
import game_framework
import Ingame
import math

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


def init():
    global scene
    global image1
    global image2
    global image3
    global image4
    image1 = load_image('title1.png')
    image2 = load_image('title2.png')
    image3 = load_image('title3.png')
    image4 = load_image('title4.png')
    scene = 0
def finish():
    global image1
    global image2
    global image3
    global image4
    del image1
    del image2
    del image3
    del image4
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(Ingame)

def draw():
    global scene1
    clear_canvas()
    if scene1 == 0:
        image1.draw(400, 266)
    elif scene1 == 1 or scene1 == 5:
        image2.draw(400, 266)
    elif scene1 == 2 or scene1 == 4:
        image3.draw(400, 266)
    elif scene1 == 3:
        image4.draw(400, 266)
    else:
        pass
    update_canvas()

def update():
    global scene
    global scene1
    scene = (scene + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
    scene1 = int(scene) % 6