from helper.helper_functions import *


def hunt_loop(replenish_energy=False, remaining_runs=-1):
    count_dict = {'total_runs': 0, 'failed_runs': 0, 'refresh_count': 0}

    while remaining_runs < 0 or remaining_runs > 0:
        if remaining_runs > 0:
            print("runs remaining: " + str(remaining_runs))
        find_and_click_image(START_IMG)
        stage_start_checks(replenish_energy, count_dict)
        if not stage_clear(count_dict):
            find_and_click_image(TRY_AGAIN_IMG)
            continue
        time.sleep(DEFAULT_WAIT_TIME)
        click_anywhere_on_screen()
        stage_end_checks()

        find_and_click_image(CONFIRM_IMG)
        find_and_click_image(TRY_AGAIN_IMG)

        remaining_runs = remaining_runs - 1
        count_dict['total_runs'] = count_dict['total_runs'] + 1

        print("loop stats: " + str(count_dict))
    return


if __name__ == '__main__':
    hunt_loop(True)
