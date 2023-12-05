# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_font, load_image, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_a, SDLK_d, \
    draw_rectangle, clamp
import Game_World
import game_framework
import server
import math

# state event check

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and (e[1].key == SDLK_a or e[1].key == SDLK_d)


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and (e[1].key == SDLK_a or e[1].key == SDLK_d)


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

def lay_down(e):
    return e[0] == 'lay_down'

def one_move(e):
    return e[0] == 'GO_IDLE'

def end_jump(e):
    return e[0] == 'GO_IDLE'
# time_out = lambda e : e[0] == 'TIME_OUT'




# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Idle:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(boy, e):
        boy.key = 0
        pass

    @staticmethod
    def do(boy):
         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
         if boy.dir > 0:
             boy.dir -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
         else:
             boy.dir = 0
         pass
    @staticmethod
    def draw(boy):
        boy.image.clip_draw(130 + int(boy.frame) * 45, 440, 45, 45, boy.sx, boy.y, 50, 70)

class Jump:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.jump_y = 7
        boy.wait_time = get_time()
        pass
    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.x += 1.8 * boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.y += boy.jump_y * RUN_SPEED_PPS * game_framework.frame_time
        boy.jump_y -= 0.1
        if int(boy.frame) < 4:
            boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if boy.y <= 210:
            boy.y = 210
            boy.state_machine.handle_event(('GO_IDLE', 0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(138 + int(boy.frame) * 43, 240, 43, 45, boy.sx, boy.y, 50, 70)
class Stun:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.wait_time = get_time()
        pass
    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if boy.y > 210:
            boy.y += boy.jump_y * RUN_SPEED_PPS * game_framework.frame_time
            boy.jump_y -= 0.1
        else :
            boy.y = 210

        if int(boy.frame) < 3:
            boy.x += 1
            boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if get_time() - boy.wait_time > 2:
            boy.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def draw(boy):
        if int(boy.frame) == 0:
            boy.image.clip_draw(635, 440, 45, 45, boy.sx, boy.y, 50, 70)
            pass
        elif int(boy.frame) == 1:
            boy.image.clip_draw(585, 440, 45, 45, boy.sx, boy.y, 50, 70)
            pass
        elif int(boy.frame) == 2:
            boy.image.clip_draw(510, 240, 35, 45, boy.sx, boy.y, 50, 70)
            pass
        elif int(boy.frame) == 3:
            boy.image.clip_draw(560, 240, 35, 45, boy.sx, boy.y, 50, 70)

class Run:
    @staticmethod
    def enter(boy, e):
        if right_down(e):  # 오른쪽으로 RUN
            if boy.key == 0:
                boy.dir, boy.face_dir, boy.key = 3.5, 1, 1
        elif left_down(e):  # 왼쪽으로 RUN
            if boy.key == 0:
                boy.x, boy.y = 50, 210
        elif left_up(e) or right_up(e):
            if boy.key == 1:
                boy.key = 0
        boy.wait_time = get_time()

    @staticmethod
    def exit(boy, e):
        boy.key = 0
        pass

    @staticmethod
    def do(boy):
        # boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 2000)
        boy.runframe = (boy.runframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # a 또는 d 키를 뗀 경우, 다시 눌렀을 때 움직임을 시작하도록 설정
        boy.dir = boy.dir - FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if boy.dir > 0:
            boy.dir -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        else:
            boy.dir = 0
        if get_time() - boy.wait_time > 0.1:
            boy.state_machine.handle_event(('GO_IDLE', 0))
        else:
            boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(135 + int(boy.runframe) * 46, 310, 46, 45, boy.sx, boy.y, 50, 70)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, space_down: Jump},
            Run: {right_up: Idle, left_up: Idle, space_down: Run, lay_down: Stun, one_move: Idle, space_down: Jump},
            Stun: {time_out: Idle},
            Jump: {end_jump: Idle, lay_down: Stun}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)
        self.boy.x = clamp(50.0, self.boy.x, self.boy.bg.w - 50.0)
        self.boy.y = clamp(50.0, self.boy.y, self.boy.bg.h - 50.0)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)


class Boy:
    def __init__(self):

        self.x, self.y = 50, 210
        self.runframe = 0
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('sonic_sprite.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.ball_count = 10
        self.key = 0
        self.jump_y = 0
        self.sx = self.x

    def set_background(self, bg):
        self.bg = bg

    def update(self):
        # sx = self.x - server.background.window_left
        # sy = self.y - server.background.window_bottom
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.sx = (self.x - self.bg.window_left)
        # self.sx = self.x - self.bg.window_left
        self.state_machine.draw()
        print(self.sx)
        print(self.x)
        print(self.bg.window_left)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.sx - 15, self.y - 25, self.sx + 20, self.y + 25

    # fill here

