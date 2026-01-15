#! /bin/python3.10

class SecurePlant:
    __total_plant = 0

    def get_total() -> int:
        return (SecurePlant.__total_plant)

    def set_total(plant: int) -> None:
        SecurePlant.__total_plant = plant + SecurePlant.get_total()

    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name.capitalize()
        self.__age = age
        self.__height = height
        SecurePlant.set_total(SecurePlant.get_total() + 1)

    def get_height(self) -> int:
        return self.__height

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def grow(self) -> None:
        self.__height += 1

    def get_info(self) -> None:
        if (isinstance(self, PrizeFlower)):
            print(f"- {self.name}: {self.get_height()}cm, "
                  f"{self.get_color()} flowers ({self.get_state()}), "
                  f"Prize points: {self.get_prize()}")
        elif (isinstance(self, FloweringPlant)):
            print(f"- {self.name}: {self.get_height()}cm, "
                  f"{self.get_color()} flowers ({self.get_state()})")
        elif (isinstance(self, SecurePlant)):
            print(f"- {self.name}: {self.get_height()}cm")


class FloweringPlant(SecurePlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, plant_state: str) -> None:
        super().__init__(name, height, age)
        self.__color = color
        self.__plant_state = plant_state

    def get_color(self) -> str:
        return (self.__color)

    def set_color(self, color: str) -> None:
        self.__color = color

    def get_state(self) -> str:
        return (self.__plant_state)

    def set_state(self, plant_state: str) -> None:
        self.__plant_state = plant_state


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, plant_state: str, prize: int) -> None:
        super().__init__(name, height, age, color, plant_state)
        self.__prize = prize

    def get_prize(self) -> int:
        return self.__prize

    def set_prize(self, prize: int) -> None:
        if prize < 0:
            print(f"Invalid operation attempted: height {prize} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__prize = prize


class GardenManager():
    class GardenStats():
        total_garden = 0

        def __init__(self, garden: object) -> None:
            self.__garden = garden
            self.__cm_tracker = 0
            self.__regular_count = 0
            self.__flowering_count = 0
            self.__prize_flowers = 0
            GardenManager.GardenStats.total_garden += 1

        def get_garden(self) -> object:
            return (self.__garden)

        def set_garden(self, new_garden: object) -> None:
            self.__garden = new_garden

        def get_cm_tracker(self) -> int:
            return (self.__cm_tracker)

        def set_cm_tracker(self, cm: int) -> None:
            self.__cm_tracker = cm

        def add_cm(self, cm_add) -> None:
            self.__cm_tracker += cm_add

        def garden_evolution(self):
            print(f"Plants added: {len(self.__garden.get_garden_content())},",
                  f"Total growth: {self.__cm_tracker}cm")
            print(f"Pant types: {self.__regular_count} regular, "
                  f"{self.__flowering_count} flowering, "
                  f"{self.__prize_flowers} prize flowers")

        def plant_type_count(self, plant: SecurePlant) -> None:
            if (isinstance(plant, PrizeFlower)):
                self.__prize_flowers += 1
            elif (isinstance(plant, FloweringPlant)):
                self.__flowering_count += 1
            elif (isinstance(plant, SecurePlant)):
                self.__regular_count += 1

        @staticmethod
        def plant_score(plant: SecurePlant) -> int:
            if (isinstance(plant, PrizeFlower)):
                return (20 * plant.get_prize())
            if (isinstance(plant, FloweringPlant)):
                return (10)
            if (isinstance(plant, SecurePlant)):
                return (8)

        def garden_score(self) -> int:
            result = 0
            for plant in self.__garden.get_garden_content().values():
                result += GardenManager.GardenStats.plant_score(plant)
            return (result)

        def height_validation(self) -> bool:
            for plant in self.__garden.get_garden_content().values():
                if (plant.get_height() < 20):
                    return (False)
            return (True)

    def __init__(self, owner: str) -> None:
        self.__owner = owner
        self.__garden_content = {}
        self.stats = GardenManager.GardenStats(self)

    def get_owner(self) -> str:
        return (self.__owner)

    def set_owner(self, owner: str) -> None:
        self.__owner = owner.capitalize()

    def get_garden_content(self) -> dict:
        return (self.__garden_content)

    def set_garden_content(self, garden_content: dict) -> None:
        self.__garden_content = garden_content

    @classmethod
    def create_garden_network(cls, owner_list: list) -> list:
        lst = []
        for owner in owner_list:
            lst += [cls(owner)]
        return (lst)

    def add_to_garden(self, plant: SecurePlant) -> None:
        print(f"Added {plant.name} to {self.get_owner()}'s garden")
        self.get_garden_content()[plant.name] = plant
        self.stats.plant_type_count(plant)

    def grow_plant(self, plant_name: str) -> None:
        plant: SecurePlant
        plant = (self.get_garden_content())[plant_name]
        plant.grow()
        self.stats.add_cm(1)
        print(f"{plant.name} grew 1 cm")

    def grow_all(self):
        print(f"{self.get_owner()} is helping all plants grow...")
        plant: SecurePlant
        for plant in self.get_garden_content().values():
            self.grow_plant(plant.name)

    def garden_info(self) -> None:
        print("Plants in garden:")
        for plant in self.get_garden_content().values():
            plant.get_info()


def fc_grow_all(garden: GardenManager) -> None:
    garden.grow_all()


if (__name__ == "__main__"):
    Bob: GardenManager
    Alice: GardenManager
    Bob, Alice = GardenManager.create_garden_network(["Bob", "Alice"])
# ============= Garden Plant Types =============
    print(" Garden Management System Demo ".center(50, "=") + "\n")
# ============= Create Alice Garden =============
    Alice.add_to_garden(SecurePlant("Oak Tree", 380, 100))
    Alice.add_to_garden(FloweringPlant("Rose", 25, 25, "red", "blooming"))
    Alice.add_to_garden(PrizeFlower("Sunflower", 50, 50, "yellow",
                                    "blooming", 10))
# ============= Create Bob Garden =============
    Bob.add_to_garden(FloweringPlant("Pine", 500, 50, "green", "blooming"))
    Bob.add_to_garden(SecurePlant("spruce", 500, 50))
    Bob.add_to_garden(SecurePlant("sprud", 500, 50))
    Bob.add_to_garden(SecurePlant("spru", 500, 50))
    Bob.add_to_garden(PrizeFlower("Daisy", 30, 30, "white", "blooming", 3))
# ================ Grow plant ================
    print("")
    Alice.grow_all()
    print("")
# ========== Alice's Garden Report ==========
    print(" Alice's Garden Report ".center(50, "=") + "\n")
    Alice.garden_info()
    print("")
    Alice.stats.garden_evolution()
    print("")
    print(f"Height validation test: {Alice.stats.height_validation()}")
    print(f"Garden scores - {Alice.get_owner()}: {Alice.stats.garden_score()},"
          f" {Bob.get_owner()}: {Bob.stats.garden_score()}")
    print(f"Total gardens managed: {GardenManager.GardenStats.total_garden}")
