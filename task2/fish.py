


from datetime import datetime
from gettext import find
from typing import Tuple

class FishShop: pass
class FishInfo: pass
class Fish(FishInfo): pass
class FishBox: pass

class FishInfo:
    def __init__(self, name: str, origin: str, weight: float, catch_date: datetime, due_date: datetime) -> None:
        self.name =  name
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date
        self.weight =  weight
    
class Fish(FishInfo):

    def __init__(self, name: str, origin: str, weight: float, catch_date: datetime, due_date: datetime, age_in_months : datetime, ) -> None:
        super().__init__(name, origin, weight, catch_date, due_date)

        self.age_in_months =  age_in_months


    def work_with_dict():
        my_dict = {"shark": Fish(name = "shark"), "salmon": Fish()}

class FishBox:
    
    def __init__(self, fish_info: FishInfo, package_date: datetime, width : float, height: float) -> None:
        
        self.fish_info = fish_info

        self.package_date = package_date
        self.height = width
        self.width = height

class FishShop:
    
    def __init__(self) -> None:
        self.frozen_fish_boxes =  dict()
        self.fresh_fish = dict()

    def add_fish(self, fish_box: FishBox) -> None:
        if fish_box.fish_info.name in self.fresh_fish:
            self.frozen_fish_boxes[fish_box.fish_info.name].append(fish_box)
        else:
            self.frozen_fish_boxes[fish_box.fish_info.name] = [fish_box,]

    def add_fish(self, fish: Fish) -> None:
        if fish.name in self.fresh_fish:
            self.fresh_fish[fish.name].append(fish)
        else:
            self.fresh_fish[fish.name] = [fish,]

    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> Tuple[str, float, bool]:
        print(f"Sold {weight} kilos of {'not' if not is_fresh else ''} {name}")
        return name, weight, is_fresh

    def get_fish_names_sorted_by_price(self) -> list[Tuple[str, bool, float]]:
        
        fish_names_list =  self.frozen_fish_boxes.keys()
        return_list =  list()

        for name in fish_names_list:
            for fish in self.frozen_fish_boxes[name]:
                return_list.append(tuple(name, (datetime.now() - fish.catch_date).days < 7), fish.price)

        return sorted(return_list, lambda x : x[2])



    def get_fresh_fish_names_sorted_by_price(self) -> list[Tuple[str, float]]:
        fish_names_list =  self.fresh_fish.keys()
        return_list =  list()

        for name in fish_names_list:
            for fish in self.fresh_fish[name]:
                return_list.append(tuple(name, fish.price))

        return sorted(return_list, lambda x : x[1])



    def get_frozen_fish_names_sorted_by_price(self) -> list[Tuple[str, float]]:
        fish_names_list =  self.frozen_fish_boxes.keys()
        return_list =  list()

        for name in fish_names_list:
            for fish in self.frozen_fish_boxes[name]:
                return_list.append(tuple(name, fish.price))

        return sorted(return_list, lambda x : x[1])