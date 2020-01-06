import time
from image_strings import *
from helper.helper_functions import (find_and_click_image, imagesearch_region_loop, imagesearch_count,
                                     click_if_is_not_selected, find_image, click_image, stage_start_checks,
                                     click_anywhere_on_screen, two_image_search_loop, stage_end_checks, click_pos)
from lobby_functions import lobby_to_adventure, lobby_to_sidestory, lobby_to_world_adventure

DEFAULT_WAIT_TIME = 2
WAIT_TIME_FOR_TRANSITIONS = 6


def search_for_boss_battle():
    imagesearch_region_loop(BOSS_BATTLE_IMG, 450, 50, 650, 150)


def farm_fodder():
    find_and_click_image(BATTLE_INVENTORY_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    time.sleep(DEFAULT_WAIT_TIME)
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
    find_and_click_image(CLEAR_PORTAL_IMG)
    find_and_click_image(STOP_EXPLORING_IMG)


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
        find_and_click_image(SUBTRACT_HERO)

    type_list = [WARRIOR_ICON_IMG, KNIGHT_ICON_IMG, THIEF_ICON_IMG, RANGER_ICON_IMG, MAGE_ICON_IMG,
                 SOUL_WEAVER_ICON_IMG]
    find_and_click_image(HERO_IN_TEAM_IMG)
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

    fodders_replaced = 0
    for i, hero_type in enumerate(type_list):
        if fodders_replaced == fodder_count_to_level:
            break
        find_and_click_image(HERO_SORT_IMG)
        if i > 0:
            find_and_click_image(type_list[i - 1])
        find_and_click_image(hero_type)
        find_and_click_image(HERO_SORT_IMG)
        if not find_image(LEVEL_ONE):
            continue
        find_and_click_image(ADD_HERO_IMG)

        if fodders_replaced == 0:
            click_pos(area_left)
        if fodders_replaced == 1:
            click_pos(area_bot)
        if fodders_replaced == 2:
            click_pos(area_right)

        fodders_replaced = fodders_replaced + 1


def __run_adventure(need_to_replace_fodder, fodder_count_to_level, replenish_energy, count_dict=None):
    click_if_is_not_selected(REPEAT_CHECKBOX_IMG)
    if need_to_replace_fodder:
        replace_fodder(fodder_count_to_level)
        need_to_replace_fodder = False
    find_and_click_image(START_IMG)
    stage_start_checks(replenish_energy, count_dict)

    search_for_boss_battle()
    find_and_click_image(STOP_REPEAT_BATTLING_IMG)
    find_and_click_image(AUTO_BATTLE_IMG)

    if two_image_search_loop(REPEAT_BATTLE_END_IMG, STAGE_FAILED_IMG) == STAGE_FAILED_IMG:
        find_and_click_image(LOBBY_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
        return
    find_and_click_image(CLOSE_IMG)
    click_anywhere_on_screen()
    stage_end_checks()
    count, pt = imagesearch_count(LEVEL_MAX_IMG)
    print(str(count) + " number of max level units")
    if count > 1 and fodder_count_to_level > 0:
        need_to_replace_fodder = True
    find_and_click_image(CONFIRM_IMG)
    return need_to_replace_fodder


def __run_lab_adventure(lab_instructions, need_to_replace_fodder, fodder_count_to_level, replenish_energy,
                        count_dict=None):
    if need_to_replace_fodder:
        replace_fodder(fodder_count_to_level)
        need_to_replace_fodder = False
    find_and_click_image(START_IMG)
    stage_start_checks(replenish_energy, count_dict)

    lab_instructions()

    find_and_click_image(STAGE_CLEAR_IMG)
    click_anywhere_on_screen()
    stage_end_checks()
    count, pt = imagesearch_count(LEVEL_MAX_IMG)
    print(str(count) + " number of max level units")
    if count > 1 and fodder_count_to_level > 0:
        need_to_replace_fodder = True
    find_and_click_image(CONFIRM_IMG)
    return need_to_replace_fodder


def __clear_urgent_mission(need_to_replace_fodder, fodders_to_level, replenish_energy):
    find_and_click_image(GO_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    need_to_replace_fodder = __run_adventure(need_to_replace_fodder, fodders_to_level, replenish_energy)
    find_and_click_image(LOBBY_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    return need_to_replace_fodder


def adventure_loop(adventure_type, replenish_energy=False, fodders_to_level=0, lab_instructions=None, remaining_runs=-1):
    count_dict = {'total_runs': 0, 'failed_runs': 0, 'refresh_count': 0}

    need_to_replace_fodder = False
    while remaining_runs < 0 or remaining_runs > 0:
        if remaining_runs > 0:
            print("runs remaining: " + str(remaining_runs))
        if lab_instructions:
            need_to_replace_fodder = __run_lab_adventure(lab_instructions, need_to_replace_fodder, fodders_to_level,
                                                         replenish_energy, count_dict)
        else:
            need_to_replace_fodder = __run_adventure(need_to_replace_fodder, fodders_to_level, replenish_energy,
                                                     count_dict)
        time.sleep(DEFAULT_WAIT_TIME)
        if find_image(URGENT_MISSION_IMG):
            need_to_replace_fodder = __clear_urgent_mission(need_to_replace_fodder, fodders_to_level, replenish_energy)
            if adventure_type == "side_story":
                lobby_to_sidestory()
            elif adventure_type == "adventure":
                lobby_to_adventure()
            elif adventure_type == "world_adventure":
                lobby_to_world_adventure()

        if lab_instructions:
            find_and_click_image(READY_IMG)
        else:
            find_and_click_image(TRY_AGAIN_IMG)
        find_and_click_image(SELECT_TEAM_IMG)

        remaining_runs = remaining_runs - 1
        count_dict['total_runs'] = count_dict['total_runs'] + 1
        print("loop stats: " + str(count_dict))


if __name__ == '__main__':
    adventure_loop("world_adventure", False, 3, lab_instructions=farm_fodder)
