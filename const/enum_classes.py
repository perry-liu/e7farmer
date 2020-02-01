import enum


class battle_type(enum.Enum):
    adventure = 1
    world_adventure = 2
    side_story = 3
    hunt_wyvern = 4.1
    hunt_banshee = 4.2
    hunt_golem = 4.3
    hunt_azimanak = 4.4
    altar = 5
    normal_raid = 6
    fodder_farm = 7
    arena = 8


class refresh_energy_method(enum.Enum):
    leif = 1
    skystone = 2
    mail = 3
    all = 4
