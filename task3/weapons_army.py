from bdb import effective
from enum import Enum
from types import NoneType
from urllib.parse import ParseResultBytes
from xmlrpc.client import boolean



# forward declarations

class Division: pass
class Solider: pass

class WeaponryManager: pass
class Weapon: pass

class DivisionType(Enum): pass
class WeaponAssaultType(Enum): pass



# classes 


class Division:

    def __init__(self, type : DivisionType, id_number: int, soliders: list[Solider] = list()) -> None:
        
        self.soliders = soliders
        self.type = type
        self.id_number = id_number


    def add_solider(self, new_solider: Solider) -> None:
        self.soliders.append(new_solider)

    def remove_solider(self, solider_to_remove: Solider) -> None:
        self.soliders.remove(solider_to_remove)

    def reserve_weapons(self, manager: WeaponryManager) -> None:

        if self.type.value == 0:
            weapon_taken = manager.get_defence_weapons(len(self.soliders))
        else:
            weapon_taken = manager.get_offence_weapons(self.type, len(self.soliders))

        index = 0
        for solider in self.soliders:
            solider.take_weapon(self.available_weapons[index])
            index += 1

        

    def return_weapons(self, manager: WeaponryManager) -> None:
        for solider in self.soliders:
            manager.add_weapon(solider.weapon)
        
        self.available_weapons = list()
        
   


class Solider:
    
    def __init__(self, division: Division, effectiveness: float) -> None:
        
        self.division = division
        self.effectiveness_factor =  effectiveness
        self.weapon = None

    def take_weapon(self, weapon : Weapon) -> None:
        self.weapon = weapon

    def return_weapon(self) -> Weapon:
        weapon_returned =  self.weapon
        self.weapon = None
        return weapon_returned 



class DivisionType(Enum):
    DEFENCE_FORCE = 0
    INFANTRY = 1
    ARTILLERY = 2
    SCOUTS = 3



class WeaponryManager:

    def __init__(self) -> None:
        
        self.available_weapons = list()


    def add_weapons(self, *new_weapons: Weapon) -> None:
        self.available_weapons.append(new_weapons)
    
    def get_defence_weapons(self, count: int) -> list[Weapon]:
        return [x for x in self.available_weapons if isinstance(x, DefenceWeapon)]

    def get_offense_weapons(self, assault_type: WeaponAssaultType, count: int) -> list[Weapon]:
        return [x for x in self.available_weapons if isinstance(x, OffenceWeapon) and x.assault_type == assault_type]
        
    def sort_weapons_by_id(self, descending: bool) -> None:  
        self.available_weapons = sorted(self.available_weapons, lambda x : x.id, descending) 

    def sort_weapons_by_quality(self, descending: bool) -> None:
        self.available_weapons = sorted(self.available_weapons, lambda x : x.quality, descending) 


class Weapon:
    
    def __init__(self, id: int, quality: float) -> None:   
        self.id = id
        self.quality = quality

    def use(self) -> None:
        print(f"using weapon {Weapon.__name__}!")


class DefenceWeapon(Weapon):
    
    def __init__(self, id: int, quality: float, shield_health: float, blocked_damage_percent: float, rated_for: str) -> None:
        super().__init__(id, quality)

        self.blocked_damage_percent = blocked_damage_percent
        self.shield_health = shield_health
        self.rated_for = rated_for


class OffenceWeapon(Weapon):
    
    def __init__(self, id: int, quality: float, damage: float, effective_range: float, assault_type: WeaponAssaultType) -> None:
        super().__init__(id, quality)

        self.damage = damage
        self.effective_range = effective_range
        self.assault_type = assault_type


class WeaponAssaultType(Enum):
    COMBAT = 1
    DISTANT_WARFATE = 2
    SCOUT_ORIENTED = 3



if __name__ ==  '__main__':

    new_solider =  Solider(division=None, effectiveness=1)
    print(new_solider)


