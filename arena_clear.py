import pyautogui
import time
from helper.helper_functions import *

DEFAULT_RANDOM_TIME = r(1, 1)

DEFAULT_WAIT_TIME = 1
WAIT_TIME_FOR_TRANSITIONS = 5


def arena_clear():
    find_and_click_image(ARENA_FIGHT_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    find_and_click_image(START_IMG)

    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    imagesearch_loop(SKIP_IMG)
    click_anywhere_on_screen()

    find_and_click_image(AUTO_BATTLE_IMG)

    imagesearch_loop(SKIP_IMG)
    click_anywhere_on_screen()
    find_and_click_image(CONFIRM_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    return True


def clear_all():
    while find_image(ARENA_FIGHT_IMG) or scroll_and_find(find_and_click_image(SKYSTONE_IMG), -1, ARENA_FIGHT_IMG):
        arena_clear()
    return

if __name__ == '__main__':
    clear_all()
