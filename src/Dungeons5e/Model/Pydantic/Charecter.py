import pydantic
from abc import ABC
from Dungeons5e.Model.interfaces.CharecterStats import BaseDndStat
import dataclasses
import functools
import operator
from typing import *

@dataclasses.dataclass
class BaseDndStatModel(BaseDndStat):
    strength: int=0
    dexterity: int=0
    intelligence: int=0
    wisdom: int=0
    charisma: int=0

class CharecterRace(BaseDndStat):
    race: str

class CharecterChosenBaseStats(BaseDndStat):
    pass

class BaseStatCombiner(BaseDndStat):
    def __init__(self, to_combine: List[BaseDndStat]):
        self._combinables: List[BaseDndStat] = to_combine
        self.strength = 0
        self.dexterity = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0
        self.constitution = 0
    
    def _reset_stat(self):
        self.strength = 0
        self.dexterity = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0
        self.constitution = 0

    
    def _compute_stats(self):
        for base_stat_object in self._combinables
class CharecterBaseStats(object):
    def __init__(self, race: CharecterRace, player: CharecterRace):
        self._race_stats = race
        self._player_stats = player
    
    @property
    def strength(self):
        return self._race_stats.strength + self._player_stats.strength
    
    @property
    def dexterity(self):
        return 



class BaseCharecterStats(pydantic.BaseModel):
    hit_points: int

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @staticmethod
    def get_modifier(stat):
        return (stat - 10) // 2
    
    @property
    def acrobatics(self):
        return (self.dexterity - 10) // 2
    
    @property
    def animal_handling(self):
        return (self.wisdom - 10) // 2
    
    @property
    def arcana(self):
        return (self.intelligence - 10) // 2
    
    @property
    def athletics(self):
        return (self.strength - 10) // 2
    
    @property
    def deception(self):
        return (self.charisma - 10) // 2
    
    @property
    def history(self):
        return (self.intelligence - 10) // 2
    
    @property
    def insight(self):
        return (self.wisdom - 10) // 2
    
    @property
    def intimidation(self):
        return (self.charisma - 10) // 2

    @property
    def investigation(self):
        return self.get_modifier(self.intelligence)

    @property
    def medicine(self):
        return self.get_modifier(self.wisdom)
    
    @property
    def nature(self):
        return self.get_modifier(self.intelligence)

    @property
    def perception(self):
        return self.get_modifier(self.intelligence)
    
    @property
    def performance(self):
        return self.get_modifier(self.charisma)
    
    @property
    def persuasion(self):
        return self.get_modifier(self.charisma)
    
    @property
    def religion(self):
        return self.get_modifier(self.intelligence)
    
    @property
    def slight_of_hand(self):
        return self.get_modifier(self.dexterity)
    
    @property
    def stealth(self):
        return self.get_modifier(self.dexterity)
    
    @property
    def survival(self):
        return self.get_modifier(self.wisdom)
    
    
class Charecter(pydantic.BaseModel):
    hit_points: int