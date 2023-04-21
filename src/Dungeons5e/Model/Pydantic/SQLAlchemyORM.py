import Dungeons5e.Model.SQL.SQLAlchemyModels as Models
from Dungeons5e.Model.Pydantic.CharecterStats import BaseDndStatModel
import pydantic

class RaceModel(BaseDndStatModel):
    race: str

    class Config:
        from_orm=True

def test_race():
    new_race = RaceModel(race="fakerace")
    print(new_race) 

if __name__ == "__main__":
    test_race()