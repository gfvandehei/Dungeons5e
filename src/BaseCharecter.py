import dataclasses

class CharecterRace(object):
    strength: int
    dexterity: int
    wisdom: int
    charisma: int
    constitution: int
    intelligence: int

class CharecterClass(object):
    pass

@dataclasses.dataclass
class BaseCharecterStats(object):
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
    

class BaseCharecter(object):
    name: str
    race: CharecterRace
    base_stats: BaseCharecterStats
    
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


