import server
from pico2d import *
import game_framework
import title
from datetime import datetime

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


def init():
    global image
    global font
    global time_list
    image = load_image('record2.png')
    file_name = 'record.txt'
    i = 0

    try:
        # 파일 열기 시도
        with open(file_name, 'r') as file:
            # 파일에 play_str 추가하기
            contents = file.readlines()
            time_list = [line.strip() for line in contents]
            time_list.sort()
    except FileNotFoundError:
        print(f"파일 '{file_name}'을(를) 찾을 수 없습니다.")
        print(f"파일 '{file_name}'을(를) 생성하고 시간을 기록합니다.")
        # 파일이 없을 경우 파일을 생성하여 현재 시간 기록
        with open(file_name, 'w') as file:
            pass
    font = load_font('ENCR10B.TTF', 30)

def finish():
    global image
    del image
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            game_framework.change_mode(title)

def draw():
    global image
    global fort
    global time_list
    i = 0
    clear_canvas()
    image.draw(400, 266, 800, 532)
    for seconds in time_list[:5]:
        current_time = seconds  # 현재 시간(초 단위)을 가져옵니다.
        seconds = int(current_time)  # 현재 시간의 정수 부분은 초 단위로 표시됩니다.
        milliseconds = int((current_time - seconds) * 1000)
        play_str = "{:02d}:{:02d}".format(seconds, milliseconds // 10, milliseconds % 10)
        font.draw(350, 377 - i * 60, play_str, (0, 0, 0))
        i += 1

    update_canvas()

def update():
    pass