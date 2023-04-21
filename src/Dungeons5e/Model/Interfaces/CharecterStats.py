import abc
from typing import List, Set

class BaseDndStatObserver(abc.ABC):
    @abc.abstractmethod
    def update(self, updated, fields: List[str]=[]):
        pass

class BaseDndStat(object):
    strength: int
    dexterity: int
    charisma: int
    intelligence: int
    wisdom: int
    constitution: int

    def __init__(self):
        self._observers: Set[BaseDndStatObserver] = set()

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
    
    def __iadd__(self, other):
        #new_stat_object = BaseDndStat()
        self.strength = self.strength + other.strength
        self.dexterity = self.dexterity + other.dexterity
        self.intelligence = self.intelligence + other.intelligence
        self.wisdom = self.wisdom + other.wisdom
        self.constitution = self.constitution + other.constitution
        self.charisma = self.charisma + other.charisma
        return self
    
    def signal_update(self, fields: List[str] = []):
        for observer in self._observers:
            observer.update(self, fields)
    
    def attach(self, observer: BaseDndStatObserver):
        self._observers.add(observer)

    def clear(self):
        self.strength = 0
        self.charisma = 0
        self.intelligence = 0
        self.dexterity = 0
        self.constitution = 0
        self.wisdom = 0

    @staticmethod
    def from_pyd_object(pyd_object):
        new_stat = BaseDndStat()
        new_stat.strength: int = pyd_object.strength
        new_stat.dexterity: int = pyd_object.dexterity
        new_stat.charisma: int = pyd_object.charisma
        new_stat.intelligence: int = pyd_object.intelligence
        new_stat.wisdom: int = pyd_object.wisdom
        new_stat.constitution: int = pyd_object.constitution
        return new_stat