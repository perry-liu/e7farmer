import pyautogui
import time
from helper import imagesearch as s
from image_strings import *

DEFAULT_RANDOM_TIME = s.r(1, 1)

WAIT_TIME_FOR_TRANSITIONS = 5


def find_image(img, precision=0.8):
    pos = s.imagesearch(img, precision)
    if pos[0] != -1:
        return pos
    else:
        return False


def scroll(pos, direction):
    s.pyautogui.moveTo(pos)
    s.pyautogui.scroll(direction)
    time.sleep(DEFAULT_RANDOM_TIME)
    s.pyautogui.scroll(direction)


def scroll_and_find(pos, img, direction):
    scroll(pos, direction)
    time.sleep(DEFAULT_RANDOM_TIME)
    return find_image(img)


def imagesearch_loop(img, precision=0.8):
    return s.imagesearch_loop(img, DEFAULT_RANDOM_TIME, precision)


def imagesearch_region_loop(img, x1, y1, x2, y2, precision=0.8):
    return s.imagesearch_region_loop(img, DEFAULT_RANDOM_TIME, x1, y1, x2, y2, precision)


def imagesearch_count(img, precision=0.6):
    return s.imagesearch_count(img, precision)


# searches for two images at the same time
def two_image_search_loop(image1, image2):
    print("Looking for " + image1 + " or " + image2 + "...")
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


def find_and_click_image(img, precision=0.8):
    pos = s.imagesearch_numLoop(img, DEFAULT_RANDOM_TIME, 10, precision)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        s.click_image(img, pos, "left")
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_RANDOM_TIME)


def find_and_click_next_to_image(img, x_offset=0, y_offset=0, precision=0.8):
    pos = s.imagesearch_numLoop(img, DEFAULT_RANDOM_TIME, 10, precision)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pos = (pos[0] + x_offset, pos[1] + y_offset)
        s.click_image(img, pos, "left")
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_RANDOM_TIME)


def find_and_click_image_in_area(img, x, y):
    w, h = width_and_height_of_img(img)
    pos = s.imagesearcharea(img, x, y, x + w + 20, y + h + 20, 0.7)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        s.click_image(img, [x, y], "left")
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_RANDOM_TIME)


def click_if_is_not_selected(img, precision=0.8):
    pos = s.imagesearch_numLoop(img, DEFAULT_RANDOM_TIME, 10, precision)
    time.sleep(DEFAULT_RANDOM_TIME)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        # search directly left of image
        checkbox_pos = s.imagesearcharea(CHECKED_BOX_IMG, pos[0] - 60, pos[1], pos[0], pos[1] + 60)
        if checkbox_pos[0] == -1:
            s.click_image(img, pos, "left")
    else:
        print("image not found: " + img)
        pyautogui.hotkey('alt', 'f10')
    time.sleep(DEFAULT_RANDOM_TIME)


# click position with random offset
def click_pos(pos, action="left", offset=8):
    pyautogui.moveTo(r(pos[0], offset), r(pos[1], offset))
    pyautogui.click(button=action)
    return


# click area randomly within area specified with margin buffers
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


# game specific


# returns true or false depending on stage clear
def stage_clear(count_dict):
    if two_image_search_loop(STAGE_CLEAR_IMG, STAGE_FAILED_IMG) == STAGE_FAILED_IMG:
        if count_dict:
            count_dict['failed_runs'] = count_dict['failed_runs'] + 1
        print("stage actually failed")
    time.sleep(DEFAULT_RANDOM_TIME)
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


def stage_start_checks(replenish_energy, replenish_energy_method, count_dict={}):
    # energy check
    __energy_check(replenish_energy, replenish_energy_method, count_dict)

    # inventory check
    if find_image(INSUFFICIENT_INVENTORY_IMG):
        # if too many heroes
        # if too many equips
        return

    # high combat power check
    if find_image(BATTLE_GUIDE_IMG):
        find_and_click_image(CONFIRM_IMG)
        time.sleep(DEFAULT_RANDOM_TIME)


def __energy_check(replenish_energy, replenish_energy_method, count_dict):
    if replenish_energy and find_image(INSUFFICIENT_ENERGY_IMG):
        __replenish_energy(replenish_energy_method)
        if count_dict:
            count_dict['refresh_count'] = count_dict['refresh_count'] + 1

        time.sleep(DEFAULT_RANDOM_TIME)
    return count_dict


def __replenish_energy(replenish_energy_method):
    if replenish_energy_method == "mail":
        find_and_click_image(CANCEL_IMG)
        find_and_click_image(READY_IMG)
        find_and_click_image(LOBBY_IMG)
        find_and_click_image(MAIL_IMG)
        if not scroll_and_find(find_image(TIME_LEFT_IMG), ENERGY_IMG, -1):
            scroll_and_find(find_image(TIME_LEFT_IMG), ENERGY_IMG, 1)
        find_and_click_next_to_image(ENERGY_IMG, x_offset=150)
        find_and_click_image(MAIL_IMG)
        #TODO: lobby to where at previously
    if replenish_energy_method == "leif":
        find_and_click_image(LEIF_IMG)
        find_and_click_image(BUY_IMG)
        find_and_click_image(START_IMG)
    if replenish_energy_method == "skystone":
        find_and_click_image("skystone.png")
        find_and_click_image("buy.png")
        find_and_click_image(START_IMG)


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
        time.sleep(DEFAULT_RANDOM_TIME)


def team_select(team_img):
    find_and_click_image(team_img)


def go_to_lobby():
    find_and_click_image(MAIN_MENU_IMG)
    find_and_click_image(LOBBY_IMG)
