import game_framework
from pico2d import *


import main_state


name = "gameover_state"
image = None
bgm = None

def enter():
    global image, bgm
    image = load_image('Resource//game_over.png')
    bgm = load_music('Resource//mus_gameover.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image, bgm
    del(image)
    del(bgm)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)



def update(frame_time):
    pass


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()



