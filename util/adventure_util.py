from const.enum_classes import battle_type, refresh_energy_method
from util.gui_util import *
from util.lobby_util import *


def __energy_check(replenish_energy, replenish_energy_method, adventure_type, count_dict):
    if replenish_energy and find_image(INSUFFICIENT_ENERGY_IMG):
        __replenish_energy(replenish_energy_method, adventure_type)
        if count_dict:
            count_dict['refresh_count'] = count_dict['refresh_count'] + 1

        time.sleep(DEFAULT_RANDOM_TIME)
    return count_dict


def __replenish_energy(method, adventure_type):
    if method == refresh_energy_method.mail:
        find_and_click_image(CANCEL_IMG)
        find_and_click_image(BACK_ARROW_IMG)
        find_and_click_image(LOBBY_IMG)
        find_and_click_image(MAIL_IMG)
        if not scroll_and_find(find_image(TIME_LEFT_IMG), ENERGY_IMG, -1):
            scroll_and_find(find_image(TIME_LEFT_IMG), ENERGY_IMG, 1)
        find_and_click_next_to_image(ENERGY_IMG, x_offset=150)
        find_and_click_image(MAIL_IMG)
        find_and_click_image(MAIN_MENU_IMG)
        find_and_click_image(LOBBY_FROM_MENU_IMG)
        lobby_to(adventure_type)
        find_and_click_image(START_IMG)
    if method == refresh_energy_method.leif:
        find_and_click_image(LEIF_IMG)
        find_and_click_image(BUY_IMG)
        find_and_click_image(START_IMG)
    if method == refresh_energy_method.skystone:
        find_and_click_image(SKYSTONE_IMG)
        find_and_click_image(BUY_IMG)
        find_and_click_image(START_IMG)


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


def stage_start_checks(replenish_energy, replenish_energy_method, adventure_type, count_dict={}):
    time.sleep(DEFAULT_RANDOM_TIME)
    # energy check
    __energy_check(replenish_energy, replenish_energy_method, adventure_type, count_dict)

    # inventory check
    if find_image(INSUFFICIENT_INVENTORY_IMG):
        if find_image(FULL_HERO_INVENTORY_IMG):
            # if too many heroes
            find_and_click_image(ARRANGE_IMG)
            promote_fodder()
            find_and_click_image(MAIN_MENU_IMG)
            find_and_click_image(LOBBY_FROM_MENU_IMG)
            lobby_to(adventure_type)
            find_and_click_image(START_IMG)
        # if too many equips

    # high combat power check
    if find_image(BATTLE_GUIDE_IMG):
        find_and_click_image(CONFIRM_IMG)
        time.sleep(DEFAULT_RANDOM_TIME)


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


def promote_fodder():
    # find all max level 2 star heroes
    find_and_click_image(HERO_SORT_IMG)
    click_if_is_not_selected(TWO_STARS_IMG)
    find_and_click_image(LEVEL_IMG)
    find_and_click_image(HERO_SORT_IMG)
    if find_image(SORT_LOWEST_LEVEL_IMG):
        find_and_click_image(LEVEL_IMG)
    else:
        find_and_click_image(HERO_SORT_IMG)

    time.sleep(DEFAULT_RANDOM_TIME)
    promote_count = 0
    while find_image(MAX_FODDER_IMG) and promote_count < 15:
        find_and_click_image(PROMOTION_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
        find_and_click_image(HERO_SORT_IMG)
        if find_image(SORT_LOWEST_LEVEL_IMG):
            find_and_click_image(HERO_SORT_IMG)
        else:
            find_and_click_image(LEVEL_IMG)
        if not find_and_click_image(LEVEL_ONE_IMG) or not find_and_click_image(LEVEL_ONE_IMG):
            break
        find_and_click_image(PROMOTION_IMG)
        find_and_click_image(CONFIRM_IMG)
        imagesearch_loop(TAP_TO_CLOSE_IMG)
        if find_image(TAP_TO_CLOSE_IMG):
            click_anywhere_on_screen()
        time.sleep(DEFAULT_RANDOM_TIME)
        find_and_click_image(HERO_SORT_IMG)
        find_and_click_image(LEVEL_IMG)
        time.sleep(DEFAULT_RANDOM_TIME)
        promote_count = promote_count + 1
        print(str(promote_count) + " promote count")


def search_max_level_units():
    imagesearch_region_loop(LEVEL_MAX_IMG, 1050, 850, 1300, 1000)


def team_select(team_img):
    find_and_click_image(team_img)


def go_to_lobby():
    find_and_click_image(MAIN_MENU_IMG)
    find_and_click_image(LOBBY_IMG)
