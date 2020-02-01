import time
from const.image_strings import *
from const.enum_classes import battle_type, refresh_energy_method
from util.gui_util import (s, find_and_click_image, find_image_in_area, imagesearch_region_loop, imagesearch_loop,
                           imagesearch_count,
                           click_if_is_not_selected, find_image,
                           click_anywhere_on_screen, two_image_search_loop, click_pos)
from util.adventure_util import stage_start_checks, stage_end_checks, replace_fodder
from util.lobby_util import lobby_to

DEFAULT_RANDOM_TIME = s.r(2, 1)
WAIT_TIME_FOR_TRANSITIONS = 6


def search_for_boss_battle():
    imagesearch_region_loop(BOSS_BATTLE_IMG, 450, 50, 650, 150)


def farm_fodder():
    find_and_click_image(BATTLE_INVENTORY_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    time.sleep(DEFAULT_RANDOM_TIME)
    find_and_click_image(FARM_FODDER_STAGE1_IMG)
    find_and_click_image(CONFIRM_IMG)
    imagesearch_loop(CLEAR_PORTAL_IMG)
    find_and_click_image(BATTLE_INVENTORY_IMG)
    find_and_click_image(FARM_FODDER_STAGE2_IMG)
    find_and_click_image(CONFIRM_IMG)
    imagesearch_loop(CLEAR_PORTAL_IMG)
    find_and_click_image(BATTLE_INVENTORY_IMG)
    find_and_click_image(FARM_FODDER_STAGE3_IMG)
    find_and_click_image(CONFIRM_IMG)
    imagesearch_loop(CLEAR_PORTAL_IMG)
    find_and_click_image(CLEAR_PORTAL_IMG)
    find_and_click_image(STOP_EXPLORING_IMG)


def __run_lab_adventure(lab_instructions, need_to_replace_fodder, fodder_count_to_level, replenish_energy,
                        replenish_energy_method, adventure_type,
                        count_dict=None):
    if need_to_replace_fodder:
        replace_fodder(fodder_count_to_level)
        need_to_replace_fodder = False
    find_and_click_image(START_IMG)
    stage_start_checks(replenish_energy, replenish_energy_method, adventure_type, count_dict)

    lab_instructions()

    find_and_click_image(STAGE_CLEAR_IMG)
    click_anywhere_on_screen()
    stage_end_checks()
    count, pt = imagesearch_count(LEVEL_MAX_IMG)
    print(str(count) + " number of max level units")
    if count > 2 and fodder_count_to_level > 0:
        print("will replace fodder next round")
        need_to_replace_fodder = True
    find_and_click_image(CONFIRM_IMG)
    return need_to_replace_fodder


def __run_adventure(need_to_replace_fodder, fodder_count_to_level, replenish_energy, replenish_energy_method,
                    adventure_type, count_dict=None):
    if need_to_replace_fodder:
        replace_fodder(fodder_count_to_level)
        need_to_replace_fodder = False
    click_if_is_not_selected(REPEAT_CHECKBOX_IMG)
    find_and_click_image(START_IMG)
    stage_start_checks(replenish_energy, replenish_energy_method, adventure_type, count_dict)

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
    # count, pt = imagesearch_count(LEVEL_MAX_IMG)
    # print(str(count) + " number of max level units")
    # if count > 2 and fodder_count_to_level > 0:
    if find_image_in_area(LEVEL_MAX_IMG, 1050, 850, 1300, 1000) and fodder_count_to_level > 0:
        print("will replace fodder next round")
        need_to_replace_fodder = True
    find_and_click_image(CONFIRM_IMG)
    return need_to_replace_fodder


def __clear_urgent_mission(need_to_replace_fodder, fodders_to_level, replenish_energy, replenish_energy_method,
                           adventure_type):
    find_and_click_image(GO_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    need_to_replace_fodder = __run_adventure(need_to_replace_fodder, fodders_to_level, replenish_energy,
                                             replenish_energy_method, adventure_type)
    find_and_click_image(LOBBY_IMG)
    return need_to_replace_fodder


def adventure_loop(adventure_type, replenish_energy=False, replenish_energy_method="leif", fodders_to_level=0,
                   lab_instructions=None, remaining_runs=-1):
    count_dict = {'total_runs': 0, 'failed_runs': 0, 'refresh_count': 0}

    need_to_replace_fodder = False
    while remaining_runs < 0 or remaining_runs > 0:
        if remaining_runs > 0:
            print("runs remaining: " + str(remaining_runs))
        if lab_instructions:
            need_to_replace_fodder = __run_lab_adventure(lab_instructions, need_to_replace_fodder, fodders_to_level,
                                                         replenish_energy, replenish_energy_method, adventure_type,
                                                         count_dict)
        else:
            need_to_replace_fodder = __run_adventure(need_to_replace_fodder, fodders_to_level, replenish_energy,
                                                     replenish_energy_method, adventure_type,
                                                     count_dict)
        time.sleep(DEFAULT_RANDOM_TIME)
        if find_image(URGENT_MISSION_IMG):
            need_to_replace_fodder = __clear_urgent_mission(need_to_replace_fodder, fodders_to_level, replenish_energy,
                                                            replenish_energy_method, adventure_type)
            lobby_to(adventure_type)

        if lab_instructions:
            find_and_click_image(READY_IMG)
        else:
            find_and_click_image(TRY_AGAIN_IMG)
        find_and_click_image(SELECT_TEAM_IMG)

        remaining_runs = remaining_runs - 1
        count_dict['total_runs'] = count_dict['total_runs'] + 1
        print("loop stats: " + str(count_dict))


if __name__ == '__main__':
    adventure_loop(battle_type.fodder_farm, True, replenish_energy_method=refresh_energy_method.mail, fodders_to_level=3, lab_instructions=farm_fodder)
    # adventure_loop(battle_type.world_adventure, True, refresh_energy_method.skystone, fodders_to_level=2)
