from const.enum_classes import battle_type, refresh_energy_method
from util.gui_util import *
from util.lobby_util import to_lobby, lobby_to, click_nothing_in_lobby
from adventure_farm import adventure_loop, farm_fodder
from hunt_or_altar_farm import hunt_or_altar_loop
from arena_clear import clear_all



def do_daily(arena_clear=True,hunt_count=1, altar_count=1, adventure_count=5):
    #start from lobby
    click_nothing_in_lobby()
    if arena_clear:
        lobby_to(battle_type.arena)
        clear_all()
        to_lobby()
    if hunt_count > 0:
        lobby_to(battle_type.hunt_wyvern)
        hunt_or_altar_loop(battle_type.hunt_wyvern, replenish_energy=True, replenish_energy_method=refresh_energy_method.mail, remaining_runs=hunt_count)
        to_lobby()
    if altar_count > 0:
        lobby_to(battle_type.altar)
        hunt_or_altar_loop(battle_type.altar, replenish_energy=True, replenish_energy_method=refresh_energy_method.mail, remaining_runs=altar_count)
        to_lobby()
    if adventure_count > 0:
        lobby_to(battle_type.fodder_farm)
        adventure_loop(battle_type.fodder_farm, replenish_energy=True, replenish_energy_method=refresh_energy_method.mail, fodders_to_level=0,
                   lab_instructions=farm_fodder, remaining_runs=adventure_count)
        to_lobby()



if __name__ == '__main__':
    do_daily()
    # lobby_to(battle_type.world_adventure)
    # adventure_loop(battle_type.world_adventure, True, refresh_energy_method.mail, fodders_to_level=2)