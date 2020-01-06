import pyautogui
import time
from helper.helper_functions import *


DEFAULT_RANDOM_TIME = r(1, 1)

DEFAULT_WAIT_TIME = 1
WAIT_TIME_FOR_TRANSITIONS = 5


# lobby_to_sidestory()
# adventure_loop("side story")

# imagesearch_loop("skip.png", s.r(1, 1))
# click_anywhere_on_screen()

# find_and_click_image("auto_battle_transparent.png")

# imagesearch_loop("skip_transparent.png", s.r(1, 1))
# click_anywhere_on_screen()
# find_and_click_image("confirm.png")


#
# find_and_click_image("lobby_transparent.png")
# time.sleep(WAIT_TIME_FOR_TRANSITIONS)
# lobby_to_sidestory()
find_and_click_image(BATTLE_INVENTORY_IMG)
find_and_click_image(FARM_FODDER_STAGE1_IMG)
find_and_click_image(CONFIRM_IMG)
time.sleep(WAIT_TIME_FOR_TRANSITIONS)
find_and_click_image(BATTLE_INVENTORY_IMG)
find_and_click_image(FARM_FODDER_STAGE2_IMG)
find_and_click_image(CONFIRM_IMG)
time.sleep(WAIT_TIME_FOR_TRANSITIONS)
find_and_click_image(BATTLE_INVENTORY_IMG)
find_and_click_image(FARM_FODDER_STAGE3_IMG)
find_and_click_image(CONFIRM_IMG)
time.sleep(WAIT_TIME_FOR_TRANSITIONS)
# find_and_click_image_in_area(REPLACE_HERO_IMG, 790, 480)
