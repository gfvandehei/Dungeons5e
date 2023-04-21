import abc
from typing import Set, List
import pydantic
from Dungeons5e.Model.Interfaces.CharecterStats import BaseDndStat, BaseDndStatObserver

class BaseDndStatModel(pydantic.BaseModel):
    strength: int = 0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    constitution: int = 0
    charisma: int = 0

    
class BaseDndStatCombiner(BaseDndStat, BaseDndStatObserver):
    def __init__(self, combinables: List[BaseDndStat]) -> None:
        BaseDndStat.__init__(self)
        self._combinables = combinables
        self._current_result = BaseDndStat()
        self.update(None, [])

    @property
    def strength(self):
        return self._current_result.strength
    
    @property
    def wisdom(self):
        return self._current_result.wisdom
    
    @property
    def constitution(self):
        return self._current_result.constitution
    
    @property
    def intelligence(self):
        return self._current_result.intelligence
    
    @property
    def charisma(self):
        return self._current_result.charisma
    
    @property
    def dexterity(self):
        return self._current_result.dexterity

    def add_new_combinable(self, new_stat: BaseDndStat):
        self._current_result += new_stat
        new_stat.attach(self)

    def remove_combinable(self, index: int):
        obj = self._combinables[index]
        self._combinables.pop(index)
        self._current_result -= obj

    def update(self, updated: BaseDndStat, fields: List[str]=[]):
        self._current_result.clear()
        for i in self._combinables:
            self._current_result += i

def test():
    new_stat = BaseDndStatModel()
    new_stat_2 = BaseDndStatModel(strength=10)
    assert(new_stat.strength == 0)
    assert(new_stat_2.strength == 10)
    istat = BaseDndStat.from_pyd_object(new_stat)
    istat2 = BaseDndStat.from_pyd_object(new_stat_2)
    assert(istat.strength == 0)
    assert(istat2.strength == 10)

    c = BaseDndStatCombiner([new_stat, new_stat_2])
    assert(c.strength == 10)

if __name__ == "__main__":
    test()