from util.gui_util import *
from util.adventure_util import stage_start_checks, stage_end_checks, stage_clear, replace_fodder
from const.enum_classes import battle_type, refresh_energy_method


def hunt_or_altar_loop(hunt_or_altar_type, replenish_energy=False, replenish_energy_method=None, fodders_to_level=0, remaining_runs=-1):
    count_dict = {'total_runs': 0, 'failed_runs': 0, 'refresh_count': 0}

    need_to_replace_fodder = False
    while remaining_runs < 0 or remaining_runs > 0:
        if remaining_runs > 0:
            print("runs remaining: " + str(remaining_runs))
        if need_to_replace_fodder:
            replace_fodder(fodders_to_level)
            need_to_replace_fodder = False
        find_and_click_image(START_IMG)
        stage_start_checks(replenish_energy, replenish_energy_method, hunt_or_altar_type, count_dict)
        if not stage_clear(count_dict):
            find_and_click_image(TRY_AGAIN_IMG)
            continue
        time.sleep(DEFAULT_RANDOM_TIME)
        click_anywhere_on_screen()
        stage_end_checks()

        if find_image_in_area(LEVEL_MAX_IMG, 1050, 850, 1300, 1000) and fodders_to_level > 0:
            print("will replace fodder next round")
            need_to_replace_fodder = True
        find_and_click_image(CONFIRM_IMG)
        find_and_click_image(TRY_AGAIN_IMG)

        remaining_runs = remaining_runs - 1
        count_dict['total_runs'] = count_dict['total_runs'] + 1

        print("loop stats: " + str(count_dict))
    return


if __name__ == '__main__':
    hunt_or_altar_loop(hunt_or_altar_type=battle_type.hunt_wyvern, replenish_energy=False, replenish_energy_method=refresh_energy_method.leif, fodders_to_level=0)
