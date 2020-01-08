from util.gui_util import *
from util.enum_classes import battle_type

WAIT_TIME_FOR_LOBBY_UI_CLEAR = 12


def __lobby_to_adventure():
    # TODO
    return


def __lobby_to_world_adventure():
    dispatch_missions()
    find_and_click_image(LOBBY_BATTLE_IMG)
    find_and_click_image(SIDE_STORY_IMG)
    find_and_click_image(UNRECORDED_HISTORY_ICON_IMG)
    find_and_click_image(ADVENTURE_IMG)
    find_and_click_image(READY_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    return


def __lobby_to_sidestory():
    dispatch_missions()
    find_and_click_image(LOBBY_BATTLE_IMG)
    find_and_click_image(SIDE_STORY_IMG)
    find_and_click_image(SIDE_STORY_ICON_IMG)
    find_and_click_image(ADVENTURE_IMG)
    find_and_click_image(READY_IMG)
    find_and_click_image(SELECT_SUPPORTER_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    return


def __lobby_to_fodder_farm():
    dispatch_missions()
    find_and_click_image(MAIN_MENU_IMG)
    find_and_click_image(ADVENTURE_FROM_MENU_IMG)
    find_and_click_image(ZOOM_OUT_IMG)
    find_and_click_image(ZOOM_OUT_IMG)
    find_and_click_image(RITANIA_IMG)
    find_and_click_image(TWO_S_IMG)
    find_and_click_image(FODDER_FARM_IMG)
    find_and_click_image(SELECT_TEAM_IMG)


def lobby_to(destination):
    destination_map = {battle_type.adventure: __lobby_to_adventure,
                       battle_type.world_adventure: __lobby_to_world_adventure,
                       battle_type.side_story: __lobby_to_sidestory,
                       battle_type.fodder_farm: __lobby_to_fodder_farm}
    return destination_map[destination]()


def dispatch_missions():
    click_pos([1500, 500])
    time.sleep(DEFAULT_RANDOM_TIME)
    if find_image(DISPATCH_COMPLETE_IMG):
        find_and_click_image(TRY_AGAIN_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    if find_image(DISPATCH_COMPLETE_IMG):
        find_and_click_image(TRY_AGAIN_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    return
