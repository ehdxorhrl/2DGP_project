from pico2d import *
import game_framework

class PLAY_TIME:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 70)
        self.start_time = 2.5
        self.play_time = 0
        self.play_font = load_font('DS-DIGIB.TTF', 36)
    def update(self):
        self.start_time -= game_framework.frame_time
        if self.start_time <= -0.5:
            self.play_time += game_framework.frame_time
    def draw(self):
        current_time = self.play_time  # 현재 시간(초 단위)을 가져옵니다.
        seconds = int(current_time)  # 현재 시간의 정수 부분은 초 단위로 표시됩니다.
        milliseconds = int((current_time - seconds) * 1000)
        play_str = "{:02d}:{:02d}".format(seconds, milliseconds // 10, milliseconds % 10)
        self.play_font.draw(700, 400, play_str, (255, 255, 255))
        if self.start_time >= 1:
            time_str = str(round(self.start_time + 1))
            self.font.draw(400, 220, time_str, (255, 255, 255))
        elif self.start_time < 1 and self.start_time > -0.5:
            time_str = str(round(self.start_time + 1))
            self.font.draw(400, 220, time_str, (255, 255, 255))
        elif self.start_time > -1.5 and self.start_time <= -0.5:
            time_str = str("start")
            self.font.draw(300, 220, time_str, (255, 255, 255))
