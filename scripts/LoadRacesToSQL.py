from Dungeons5e.Controller.DatabaseController import DungeonsDBBaseHandler
from Dungeons5e.Controller.Environment import Dungeons5eEnvironmentHandler
import Dungeons5e.Model.SQLAlchemyModels as SQLModels
import json

env = Dungeons5eEnvironmentHandler(["./pg-variables.env"])
db_uri = f"postgresql://{env.get_env('POSTGRES_USER')}:{env.get_env('POSTGRES_PASSWORD')}\
@{env.get_env('POSTGRES_HOST', 'localhost')}:{env.get_env('POSTGRES_PORT', 5432)}\
/{env.get_env('POSTGRES_DB', 'dungeon5e')}"

print(db_uri)

db_hander = DungeonsDBBaseHandler(db_uri)

with open("./data/races.json", "r") as fp:
    races_json: dict = json.load(fp)

with db_hander.get_session() as session:
    races_in_db = set(session.query(SQLModels.CharecterRace.race).all())
    
    races_not_in_db = set(races_json.keys()).difference(races_in_db)
    
    for race_name in races_not_in_db:
        new_race = SQLModels.CharecterRace()
        new_race.race = race_name
        new_race.charisma = races_json[race_name].get("charisma")
        new_race.dexterity = races_json[race_name].get("dexterity")
        new_race.intelligence = races_json[race_name].get("intelligence")
        new_race.strength = races_json[race_name].get("strength")
        new_race.wisdom = races_json[race_name].get("wisdom")
        session.add(new_race)
    session.commit()
