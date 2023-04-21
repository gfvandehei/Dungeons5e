import dataclasses
from Dungeons5e.Model.Interfaces.Race import Race, BaseDndStat, RaceModel
from Dungeons5e.Model.Pydantic.CharecterStats import BaseDndStatCombiner, BaseDndStatModel

class BaseCharecter(BaseDndStatCombiner):
    name: str
    hit_point_pool: int = 0
    hit_points: int = 0

    race: Race
    user_base_stats: BaseDndStat

    def __init__(self, name: str, hit_point_pool: int, race: Race, user_defined_stats: BaseDndStat):
        self.race = race
        self.user_base_stats = user_defined_stats
        self.name = name
        self.hit_point_pool = hit_point_pool
        BaseDndStatCombiner.__init__(self, [self.race, self.user_base_stats])

def test_charecter():
    fake_race = Race.from_model(RaceModel(race="fake", strength=2))
    fake_stat = BaseDndStat.from_pyd_object(BaseDndStatModel(strength=1))
    c = BaseCharecter("Gabe", 100, fake_race, fake_stat)
    print(c.strength)

if __name__ == "__main__":
    test_charecter()

