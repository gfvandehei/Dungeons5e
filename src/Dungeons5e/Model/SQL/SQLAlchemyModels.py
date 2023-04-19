from sqlalchemy.orm import declarative_base
from sqlalchemy import *

Base = declarative_base()

class CharecterRace(Base):
    __tablename__="races"

    race=Column(String, primary_key=True)
    strength=Column(Integer)
    dexterity=Column(Integer)
    intelligence=Column(Integer)
    wisdom=Column(Integer)
    charisma=Column(Integer)