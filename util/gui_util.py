import pyautogui
import time
from util import imagesearch as s
from image_strings import *

DEFAULT_RANDOM_TIME = s.r(2, 1)

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
    im.save('.\\Pictures\\test\\area_click.png')
    time.sleep(DEFAULT_RANDOM_TIME)
    pyautogui.click(button=action)


def click_anywhere_on_screen(action="left"):
    click_area(0, 0, 1920, 1080, action)


