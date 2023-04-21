from Dungeons5e.Model.Interfaces.CharecterStats import BaseDndStat
from Dungeons5e.Model.Pydantic.CharecterStats import BaseDndStatModel
from Dungeons5e.Model.Pydantic.SQLAlchemyORM import RaceModel

class Race(BaseDndStat):
    race: str

    @staticmethod
    def from_model(pyd_model: RaceModel):
        new_race = Race()
        new_race.race = pyd_model.race
        new_race.clear()
        new_race += pyd_model
        return new_race

def test_race():
    race_model = RaceModel(race="test", strength=1)
    new_race = Race.from_model(race_model)
    print(new_race.__dict__)
    assert(new_race.race == "test")
    assert(new_race.strength == 1)

if __name__ == "__main__":
    test_race()
