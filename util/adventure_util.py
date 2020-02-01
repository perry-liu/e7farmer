from const.enum_classes import battle_type, refresh_energy_method
from util.gui_util import *
from util.lobby_util import lobby_to, came_to_lobby, find_and_click_in_lobby


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
        find_and_click_image(BACK_IMG)
        find_and_click_in_lobby(MAIL_IMG)
        if not find_image(ENERGY_IMG):
            if not scroll_and_find(find_image(TIME_LEFT_IMG), ENERGY_IMG, -1):
                print("could not find energy in mail.")
        find_and_click_next_to_image(ENERGY_IMG, x_offset=150)
        find_and_click_in_lobby(MAIL_IMG)
        time.sleep(DEFAULT_RANDOM_TIME)
        find_and_click_in_lobby(MAIN_MENU_IMG)
        find_and_click_in_lobby(LOBBY_FROM_MENU_IMG)
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
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    # energy check
    __energy_check(replenish_energy, replenish_energy_method, adventure_type, count_dict)

    # inventory check
    if find_image(INSUFFICIENT_INVENTORY_IMG):
        if find_image(FULL_HERO_INVENTORY_IMG):
            # if too many heroes
            find_and_click_image(ARRANGE_IMG)
            promote_fodder(5)
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


def promote_fodder(max_fodder_to_promote=-1):
    # find all max level 2 star heroes
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
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
    while find_image(MAX_FODDER_IMG) and (max_fodder_to_promote < 0 or max_fodder_to_promote > 0):
        find_and_click_image(PROMOTION_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
        find_and_click_image(HERO_SORT_IMG)
        if find_image(SORT_LOWEST_LEVEL_IMG):
            find_and_click_image(HERO_SORT_IMG)
        else:
            find_and_click_image(LEVEL_IMG)
        if not find_and_click_image(LEVEL_ONE_IMG):
            print("no more lvl 1 fodder cards")
            find_and_click_image(BACK_ARROW_IMG)
            break
        if not find_and_click_image(LEVEL_ONE_IMG):
            print("no more lvl 1 fodder cards")
            find_and_click_image(BACK_ARROW_IMG)
            break
        find_and_click_image(PROMOTION_IMG)
        find_and_click_image(CONFIRM_IMG)
        two_image_search_loop(TAP_TO_CLOSE_IMG, PROMOTION_FINISH_INDICATOR_IMG)
        click_anywhere_on_screen()
        time.sleep(DEFAULT_RANDOM_TIME)
        find_and_click_image(HERO_SORT_IMG)
        find_and_click_image(LEVEL_IMG)
        time.sleep(DEFAULT_RANDOM_TIME)
        promote_count = promote_count + 1
        print(str(promote_count) + " promote count")


def replace_fodder(fodder_count_to_level):
    area_left = [494, 633]
    area_bot = [619, 738]
    area_right = [793, 618]

    # get rid of fodders
    for i in range(fodder_count_to_level):
        if i == 0:
            click_pos(area_left)
        if i == 1:
            click_pos(area_bot)
        if i == 2:
            click_pos(area_right)
        time.sleep(DEFAULT_RANDOM_TIME)
        find_and_click_image(SUBTRACT_HERO)

    # sort by lowest lvl 2 star units
    find_and_click_image(HERO_SORT_IMG)
    click_if_is_not_selected(TWO_STARS_IMG)
    if find_image(SORT_LOWEST_LEVEL_IMG):
        find_and_click_image(HERO_SORT_IMG)
    else:
        find_and_click_image(LEVEL_IMG)
        find_and_click_image(HERO_SORT_IMG)
        if find_image(SORT_LOWEST_LEVEL_IMG):
            find_and_click_image(HERO_SORT_IMG)
        else:
            find_and_click_image(LEVEL_IMG)

    # try to find distinct fodder heroes, double for loop through type and element
    type_list = [WARRIOR_ICON_IMG, KNIGHT_ICON_IMG, THIEF_ICON_IMG, RANGER_ICON_IMG, MAGE_ICON_IMG,
                 SOUL_WEAVER_ICON_IMG]
    element_list = [FIRE_ICON_IMG, ICE_ICON_IMG, WOOD_ICON_IMG, LIGHT_ICON_IMG, DARK_ICON_IMG]
    fodders_replaced = 0
    find_and_click_image(HERO_SORT_IMG)
    for i, hero_type in enumerate(type_list):
        if i > 0:
            find_and_click_image(type_list[i - 1])
        click_if_is_not_selected(hero_type)
        for j, hero_element in enumerate(element_list):
            if j > 0:
                find_and_click_image(element_list[j - 1])
            click_if_is_not_selected(hero_element, .9)
            find_and_click_image(HERO_SORT_IMG)
            time.sleep(DEFAULT_RANDOM_TIME)
            if not find_image(LEVEL_ONE_IMG):
                find_and_click_image(HERO_SORT_IMG)
                continue
            find_and_click_image(ADD_HERO_IMG)

            if fodders_replaced == 0:
                click_pos(area_left)
            if fodders_replaced == 1:
                click_pos(area_bot)
            if fodders_replaced == 2:
                click_pos(area_right)

            fodders_replaced = fodders_replaced + 1
            if fodders_replaced == fodder_count_to_level:
                break
            find_and_click_image(HERO_SORT_IMG)
        else:
            find_and_click_image(element_list[-1])
            continue
        break


def search_max_level_units():
    imagesearch_region_loop(LEVEL_MAX_IMG, 1050, 850, 1300, 1000)


def team_select(team_img):
    find_and_click_image(team_img)
