import abc
from typing import List

class BaseDndStat(object):
    strength: int = 0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    constitution: int = 0
    charisma: int = 0

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

    def __add__(self, other):
        new_stat_object = BaseDndStat()
        new_stat_object.strength = self.strength + other.strength
        new_stat_object.dexterity = self.dexterity + other.dexterity
        new_stat_object.intelligence = self.intelligence + other.intelligence
        new_stat_object.wisdom = self.wisdom + other.wisdom
        new_stat_object.constitution = self.constitution + other.constitution
        new_stat_object.charisma = self.charisma + other.charisma
        return new_stat_object
    
class BaseDndStatCombiner(object):
    def __init__(self, combinables: List[BaseDndStat]) -> None:
        self._combinables = combinables
        self._current_result = BaseDndStat()
        self._current_result.strength = 0
        self._current_result.dexterity = 0
        self._current_result.intelligence = 0
        self._current_result.wisdom = 0
        self._current_result.constitution = 0
        self._current_result.charisma = 0
        
        for i in self._combinables:
            self._current_result += i

    def add_new_combinable(self, new_stat: BaseDndStat):
        self._current_result += new_stat

    def remove_combinable(self, index: int):
        obj = self._combinables[index]
        self._combinables.pop(index)
        self._current_result -= obj
