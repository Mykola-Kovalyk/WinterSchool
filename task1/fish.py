import datetime

class Fish:

    def __init__(self, name: str, price_in_uah_per_kilo: float, catch_date: datetime, origin: str, body_only: bool, weight: float) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin
        self.body_only = body_only
        self.weight = weight

class FishShop:
    def __init__(self) -> None:
        self.all_fish = dict()

    def add_fish(self, fish: Fish) -> None:
        if fish.name in self.all_fish:
            self.all_fish[fish.name].append(fish)
        else:
            self.all_fish[fish.name] = list()   


    def sell_fish(self, fish_name: str, weight: float) -> Fish:
        if fish_name in self.all_fish:
            all_available = self.all_fish[fish_name]
            the_best_fish = None
            for item in all_available:
                if item.weight - 100 < weight < item.weight + 100:
                    the_best_fish = item
                    break
            if the_best_fish != None:
                self.all_fish[fish_name].remove(the_best_fish)
                return the_best_fish

        return None      


    def throw_away_old_fish(self):
        for fish_name, list_of_fish in self.all_fish.items():
            for fish in list_of_fish:
                if fish.catch_date < datetime.now() - datetime.timedelta(days=10):
                    self.all_fish[fish_name].remove[fish]


class Seller:
    def __init__(self):
        self.shop = FishShop()
        self.opened = True

    def is_opened(self):
        return self.opened

    def close_shop(self):
        self.opened = False

    def open_shop(self):
        self.opened = True       

class Buyer:
    def buy_fish(fish: Fish, seller: Seller):
        return seller.shop.sell_fish(fish.name, fish.weight)