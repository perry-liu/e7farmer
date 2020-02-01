from util.gui_util import *
from const.enum_classes import battle_type


def click_nothing_in_lobby():
    click_pos([1700, 700])
    time.sleep(DEFAULT_RANDOM_TIME)



def find_and_click_in_lobby(image):
    find_and_click_image(image)
    if dispatch_missions():
        find_and_click_image(image)


def dispatch_missions():
    found = False
    if find_image(DISPATCH_COMPLETE_IMG):
        found = True
        find_and_click_image(TRY_AGAIN_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
        click_nothing_in_lobby()
        time.sleep(DEFAULT_RANDOM_TIME)
    if find_image(DISPATCH_COMPLETE_IMG):
        found = True
        find_and_click_image(TRY_AGAIN_IMG)
        time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    return found


def __lobby_to_adventure():
    find_and_click_in_lobby(MAIN_MENU_IMG)
    find_and_click_in_lobby(ADVENTURE_FROM_MENU_IMG)
    find_and_click_image(READY_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    return


def __lobby_to_world_adventure():
    find_and_click_in_lobby(LOBBY_BATTLE_IMG)
    find_and_click_image(SIDE_STORY_IMG)
    find_and_click_image(UNRECORDED_HISTORY_ICON_IMG)
    find_and_click_image(ADVENTURE_IMG)
    find_and_click_image(READY_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    return


def __lobby_to_sidestory():
    find_and_click_in_lobby(LOBBY_BATTLE_IMG)
    find_and_click_image(SIDE_STORY_IMG)
    find_and_click_image(SIDE_STORY_ICON_IMG)
    find_and_click_image(ADVENTURE_IMG)
    find_and_click_image(READY_IMG)
    find_and_click_image(SELECT_SUPPORTER_IMG)
    find_and_click_image(SELECT_TEAM_IMG)
    return


def __lobby_to_fodder_farm():
    find_and_click_in_lobby(MAIN_MENU_IMG)
    find_and_click_in_lobby(ADVENTURE_FROM_MENU_IMG)
    find_and_click_image(ZOOM_OUT_IMG)
    find_and_click_image(ZOOM_OUT_IMG)
    find_and_click_image(RITANIA_IMG)
    find_and_click_image(TWO_S_IMG)
    find_and_click_image(FARM_FODDER_IMG)
    find_and_click_image(READY_IMG)
    find_and_click_image(SELECT_TEAM_IMG)


def __lobby_to_hunt(hunt_image):
    find_and_click_in_lobby(LOBBY_BATTLE_IMG)
    find_and_click_image(HUNT_IMG)
    find_and_click_image(hunt_image)
    find_and_click_image(HUNT_STAGE_11)
    find_and_click_image(SELECT_TEAM_IMG)


def __lobby_to_wyvern_hunt():
    __lobby_to_hunt(WYVERN_HUNT_IMG)


def __lobby_to_golem_hunt():
    __lobby_to_hunt(GOLEM_HUNT_IMG)


def __lobby_to_banshee_hunt():
    __lobby_to_hunt(BANSHEE_HUNT_IMG)


def __lobby_to_azimanak_hunt():
    print("looking for azimanak hunt")
    find_and_click_in_lobby(LOBBY_BATTLE_IMG)
    find_and_click_image(HUNT_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    scroll_and_find(find_image(WYVERN_HUNT_IMG), AZIMANAK_HUNT_IMG, -1)
    find_and_click_image(AZIMANAK_HUNT_IMG)
    find_and_click_image(HUNT_STAGE_11)
    find_and_click_image(SELECT_TEAM_IMG)


def __lobby_to_altar():
    find_and_click_in_lobby(LOBBY_BATTLE_IMG)
    find_and_click_image(SPIRIT_ALTAR_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    click_pos([1200, 400])
    find_and_click_image(SPIRIT_ALTAR_STAGE_10)
    find_and_click_image(SELECT_TEAM_IMG)
    return


def __lobby_to_arena():
    find_and_click_in_lobby(MAIN_MENU_IMG)
    find_and_click_in_lobby(ARENA_FROM_MENU_IMG)
    find_and_click_image(NPC_CHALLENGE_IMG)
    return


def to_lobby():
    if find_and_click_image(BACK_ARROW_IMG):
        if find_and_click_image(LOBBY_IMG):
            return True
    find_and_click_in_lobby(MAIN_MENU_IMG)
    find_and_click_in_lobby(LOBBY_FROM_MENU_IMG)
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)


def came_to_lobby():
    time.sleep(WAIT_TIME_FOR_TRANSITIONS)
    click_nothing_in_lobby()
    click_nothing_in_lobby()
    dispatch_missions()


def lobby_to(destination):
    came_to_lobby()
    destination_map = {battle_type.arena: __lobby_to_arena,
                       battle_type.altar: __lobby_to_altar,
                       battle_type.adventure: __lobby_to_adventure,
                       battle_type.world_adventure: __lobby_to_world_adventure,
                       battle_type.side_story: __lobby_to_sidestory,
                       battle_type.fodder_farm: __lobby_to_fodder_farm,
                       battle_type.hunt_wyvern: __lobby_to_wyvern_hunt,
                       battle_type.hunt_golem: __lobby_to_golem_hunt,
                       battle_type.hunt_banshee: __lobby_to_banshee_hunt,
                       battle_type.hunt_azimanak: __lobby_to_azimanak_hunt
                       }
    return destination_map[destination]()
