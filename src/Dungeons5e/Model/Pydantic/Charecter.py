import pydantic
from Dungeons5e.Model.Pydantic.CharecterStats import BaseDndStat, BaseDndStatCombiner
from Dungeons5e.Model.Pydantic.SQLAlchemyORM import Race

class BaseCharecter(pydantic.BaseModel):
    name: str
    hit_point_pool: int
    hit_points: int
    
    race: Race
    base_stats: BaseDndStat
    
    @property
    def strength(self):
        return self.base_stats.strength + self.race.strength

    @property
    def dexterity(self):
        return self.base_stats.dexterity + self.race.dexterity
    
    @property
    def constitution(self):
        return self.base_stats.constitution + self.race.constitution
    
    @property
    def intelligence(self):
        return self.base_stats.intelligence + self.race.intelligence
    
    @property
    def wisdom(self):
        return self.base_stats.wisdom + self.race.wisdom
    
    @property
    def charisma(self):
        return self.base_stats.charisma + self.race.charisma


# ================== testing ===========================
def testBaseCharecter():
    fake_race = Race(race="fakerace")
    fake_stats = BaseDndStat()
    new_base_charecter = BaseCharecter(name="bob", hit_point_pool=100, hit_points=100, race=fake_race, base_stats=fake_stats)
    print(new_base_charecter)

if __name__ == "__main__":
    testBaseCharecter()