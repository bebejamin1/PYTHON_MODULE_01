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

    def get_info(self) -> None:
        if (isinstance(self, SecurePlant)):
            print(f"- {self.name}: {self.get_height()}cm")
        if (isinstance(self, FloweringPlant)):
            print(f"- {self.name}: {self.get_height()}cm, "
                  f"{self.color} flowers ({self.get_state()})")
        if (isinstance(self, PrizeFlower)):
            print(f"- {self.name}: {self.get_height()}cm, "
                  f"{self.get_color()} flowers ({self.get_state()}), "
                  f"Prize points: {self.get_prize()}")


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

        def plant_type_count(self, plant: SecurePlant) -> None:
            if (isinstance(plant, PrizeFlower)):
                self.__prize_flowers += 1
            elif (isinstance(plant, FloweringPlant)):
                self.__flowering_count += 1
            elif (isinstance(plant, SecurePlant)):
                self.__regular_count += 1


if __name__ == "__main__":
    print(" Garden Management System Demo ".center("=", 50))
# ============= Garden Plant Types =============
    print(" Alice's Garden Report ".center("=", 50))
# ========== Alice's Garden Report =============
    print("ahahaha")
