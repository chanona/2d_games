import random

from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('Resource/unnamed_97(2).png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        self.center_object = boy
        pass


    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)


    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.h - self.canvas_height)

    def handle_event(self, event):
        pass


class BlackRoom:
    def __init__(self):
        self.image = load_image('Resource/BlackRoom.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 800
        self.h = 600

    def set_center_object(self, boy):
        self.center_object = boy
        pass


    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)


    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.h - self.canvas_height)

    def handle_event(self, event):
        pass

class BattleRoom:
    def __init__(self):
        self.image = load_image('Resource/battleroom_monattack.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 800
        self.h = 600
        self.x = 400
        self.y = 300

    def set_center_object(self, boy):
        self.center_object = boy
        pass


    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)


    def update(self, frame_time):
        pass

    def handle_event(self, event):
        pass