import enum


class battle_type(enum.Enum):
    adventure = 1
    world_adventure = 2
    side_story = 3
    hunt = 4
    altar = 5
    normal_raid = 6
    fodder_farm = 7


class refresh_energy_method(enum.Enum):
    leif = 1
    skystone = 2
    mail = 3
    all = 4
