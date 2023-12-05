import random
import Ingame
import pico2d

import server


class PATTERN:
    def __init__(self):
        self.element_counts = [4, 4, 7, 7, 10, 10]
        self.result_list = []
        self.bg1 = pico2d.load_image('frame1.png')
        self.bg2 = pico2d.load_image('frame2.png')
        self.bg3 = pico2d.load_image('frame3.png')
        self.up = pico2d.load_image('up.png')
        self.down = pico2d.load_image('down.png')
        self.left = pico2d.load_image('left.png')
        self.right = pico2d.load_image('right.png')
        for count in self.element_counts:
            temp_list = [random.randint(1073741903, 1073741906) for _ in range(count)]
            self.result_list.append(temp_list)
        self.pattern_index = 0
        self.pattern_num = 0
        self.w = 50
        self.h = 50
        self.x = 400
        self.y = 450
        self.good = False
    def update(self):
        if self.pattern_num < 8:
            if self.test_patter():
                self.pattern_num += 1
                self.pattern_index = 0
                Ingame.pattern = False
                server.boy.state_machine.handle_event(('GOOD', 0))
                self.good = True

    def draw(self):
        if Ingame.pattern == True and self.good == False:
            if self.pattern_num == 0 or self.pattern_num == 1:
                self.bg1.draw(self.x, self.y)
                for i in range(0, 4):
                    if self.result_list[self.pattern_num][i] == 1073741903:
                        self.right.draw(self.x - 75 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741904:
                        self.left.draw(self.x - 75 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741905:
                        self.down.draw(self.x - 75 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741906:
                        self.up.draw(self.x - 75 + i * self.w, self.y, self.w, self.h)
            if self.pattern_num == 2 or self.pattern_num == 3:
                self.bg2.draw(self.x, self.y)
                for i in range(0, 7):
                    if self.result_list[self.pattern_num][i] == 1073741903:
                        self.right.draw(self.x - 150 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741904:
                        self.left.draw(self.x - 150 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741905:
                        self.down.draw(self.x - 150 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741906:
                        self.up.draw(self.x - 150 + i * self.w, self.y, self.w, self.h)
            if self.pattern_num == 4 or self.pattern_num == 5:
                self.bg3.draw(self.x, self.y)
                for i in range(0, 10):
                    if self.result_list[self.pattern_num][i] == 1073741903:
                        self.right.draw(self.x - 225 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741904:
                        self.left.draw(self.x - 225 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741905:
                        self.down.draw(self.x - 225 + i * self.w, self.y, self.w, self.h)
                    elif self.result_list[self.pattern_num][i] == 1073741906:
                        self.up.draw(self.x - 225 + i * self.w, self.y, self.w, self.h)
    def set_patter(self):
        max_index = 0
        if self.pattern_num == 0 or self.pattern_num == 1:
            max_index = 4
        if self.pattern_num == 2 or self.pattern_num == 3:
            max_index = 7
        if self.pattern_num == 4 or self.pattern_num == 5:
            max_index = 10
        for i in range(0, max_index):
            self.result_list[self.pattern_num][i] = random.randint(1073741903, 1073741906)

    def test_patter(self):
        max_index = 0
        if self.pattern_num == 0 or self.pattern_num == 1:
            max_index = 4
        if self.pattern_num == 2 or self.pattern_num == 3:
            max_index = 7
        if self.pattern_num == 4 or self.pattern_num == 5:
            max_index = 10
        for i in range(0, max_index):
            if self.result_list[self.pattern_num][i] != 0:
                return False
        return True

# import pico2d
#
# pico2d.open_canvas()
#
# running = True
#
# while running:
#     events = pico2d.get_events()
#     for event in events:
#         if event.type == pico2d.SDL_KEYDOWN:  # 키가 눌렸는지 확인
#             if event.key == pico2d.SDLK_ESCAPE:  # ESCAPE 키인지 확인
#                 print(event.key)
#             elif event.key == pico2d.SDLK_LEFT:  # 왼쪽 화살표 키인지 확인
#                 print(event.key)
#             elif event.key == pico2d.SDLK_RIGHT:  # 오른쪽 화살표 키인지 확인
#                 print(event.key)
#             elif event.key == pico2d.SDLK_UP:  # 오른쪽 화살표 키인지 확인
#                 print(event.key)
#             elif event.key == pico2d.SDLK_DOWN:  # 오른쪽 화살표 키인지 확인
#                 print(event.key)
#
#     pico2d.update_canvas()
#
# pico2d.close_canvas()



