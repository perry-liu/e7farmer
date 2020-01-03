import pyautogui
import time
from helper import imagesearch as s
from image_strings import *

DEFAULT_RANDOM_TIME = s.r(1, 1)

DEFAULT_WAIT_TIME = 1
WAIT_TIME_FOR_TRANSITIONS = 5


def find_image(img, precision=0.8):
    pos = s.imagesearch(img, precision)
    if pos[0] != -1:
        return True
    else:
        return False


def click_image(image, pos, action="left", offset=8):
    return s.click_image(image, pos, action, offset)


def scroll(pos, direction):
    s.pyautogui.moveTo(pos)
    s.pyautogui.scroll(direction)
    time.sleep(DEFAULT_WAIT_TIME)
    s.pyautogui.scroll(direction)


def scroll_and_find(pos, direction, img):
    scroll(pos, direction)
    time.sleep(DEFAULT_WAIT_TIME)
    return find_image(ARENA_FIGHT_IMG)


def imagesearch_loop(img, precision=0.8):
    return s.imagesearch_loop(img, DEFAULT_RANDOM_TIME, precision)


def imagesearch_region_loop(img, x1, y1, x2, y2, precision=0.8):
    return s.imagesearch_region_loop(img, DEFAULT_RANDOM_TIME, x1, y1, x2, y2, precision)


def imagesearch_count(img, precision=0.6):
    return s.imagesearch_count(img, precision)


# searches for two images at the same time
def two_image_search_loop(image1, image2):
    print("Looking for " + image1 + " and " + image2 + "...")
    pos = s.imagesearch(image1)
    while pos[0] == -1:
        pos = s.imagesearch(image2)
        if pos[0] != -1:
            return image2
        time.sleep(s.r(1, 1))
        pos = s.imagesearch(image1)
    return image1


def r(num, rand):
    return s.r(num, rand)


def width_and_height_of_img(img):
    return s.width_and_height_of_img(img)


def find_and_click_image(img):
    pos = s.imagesearch_numLoop(img, DEFAULT_RANDOM_TIME, 10)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        s.click_image(img, pos, "left", 0)
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_WAIT_TIME)


def find_and_click_image_in_area(img, x, y):
    w, h = width_and_height_of_img(img)
    pos = s.imagesearcharea(img, x, y, x + w + 20, y + h + 20, 0.7)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        s.click_image(img, [x, y], "left", 0)
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_WAIT_TIME)


def click_if_is_not_selected(img):
    pos = s.imagesearch_numLoop(img, DEFAULT_RANDOM_TIME, 10)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        # search directly left of image
        checkbox_pos = s.imagesearcharea(CHECKED_BOX_IMG, pos[0] - 60, pos[1], pos[0], pos[1] + 60)
        if checkbox_pos[0] == -1:
            s.click_image(img, pos, "left", 0)
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_WAIT_TIME)


def click_pos(pos, action="left", offset=8):
    pyautogui.moveTo(r(pos[0], offset), r(pos[1], offset))
    pyautogui.click(button=action)
    return

def click_area(x1, y1, x2, y2, action="left"):
    width = x2 - x1
    height = y2 - y1
    width_margin = width / 4
    height_margin = height / 4

    pyautogui.moveTo(s.r(x1 + width_margin, width - 2 * width_margin),
                     s.r(y1 + height_margin, height - 2 * height_margin))
    im = s.region_grabber(region=(x1 + width_margin, y1 + height_margin, x2 - width_margin, y2 - height_margin))
    im.save('area_click.png')
    time.sleep(DEFAULT_RANDOM_TIME)
    pyautogui.click(button=action)


def click_anywhere_on_screen(action="left"):
    click_area(0, 0, 1920, 1080, action)


# returns true or false depending on stage clear
def stage_clear(count_dict):
    if two_image_search_loop(STAGE_CLEAR_IMG, STAGE_FAILED_IMG) == STAGE_FAILED_IMG:
        if count_dict:
            count_dict['failed_runs'] = count_dict['failed_runs'] + 1
        print("stage actually failed")
    time.sleep(DEFAULT_WAIT_TIME)
    return True
    # pos = s.imagesearch(STAGE_CLEAR_IMG)
    # print("Looking for stage clear.png ...")
    # while pos[0] == -1:
    #     pos = s.imagesearch(STAGE_FAILED_IMG)
    #     if pos[0] != -1:
    #         count_dict['failed_runs'] = count_dict['failed_runs'] + 1
    #         print("stage actually failed")
    #         return False
    #     time.sleep(s.r(1, 1))
    #     pos = s.imagesearch(STAGE_CLEAR_IMG)
    # time.sleep(DEFAULT_WAIT_TIME)


def stage_start_checks(replenish_energy, count_dict={}):
    # energy check
    energy_check(replenish_energy, count_dict)

    # inventory check
    if find_image(INSUFFICIENT_INVENTORY_IMG):
        # if too many heroes
        # if too many equips
        return

    # high combat power check
    if find_image(BATTLE_GUIDE_IMG):
        find_and_click_image(CONFIRM_IMG)
        time.sleep(DEFAULT_WAIT_TIME)


def energy_check(replenish_energy, count_dict):
    if replenish_energy and find_image(INSUFFICIENT_ENERGY_IMG):
        find_and_click_image(LEIF_IMG)
        find_and_click_image(BUY_IMG)
        find_and_click_image(START_IMG)
        if count_dict:
            count_dict['refresh_count'] = count_dict['refresh_count'] + 1
        #     find_and_click_image("skystone.png")
        #     find_and_click_image("buy.png")
        #     find_and_click_image(START_IMG)
        #     refresh_count = refresh_count + 1

        time.sleep(DEFAULT_WAIT_TIME)
    return count_dict


def stage_end_checks(refill_fodder=False):
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)

    while find_image(RANK_UP_IMG) or find_image(FRIEND_IMG) or find_image(FRIENDSHIP_LVL_INCREASE_IMG):
        # check rank up
        if find_image(RANK_UP_IMG):
            click_anywhere_on_screen()
        # check new friend used
        if find_image(FRIEND_IMG):
            find_and_click_image(CANCEL_IMG)
        # check friendship
        if find_image(FRIENDSHIP_LVL_INCREASE_IMG):
            find_and_click_image(TAP_TO_CLOSE_IMG)
        time.sleep(DEFAULT_WAIT_TIME)


def team_select(team_img):
    find_and_click_image(team_img)


def go_to_lobby():
    find_and_click_image(MAIN_MENU_IMG)
    find_and_click_image(LOBBY_IMG)
