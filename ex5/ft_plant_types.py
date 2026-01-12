#! /bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Summury:
            Initializes attributes corresponding to Plant information in
            a class to bring all the data together.

        Args:
            name (str): Plant name.
            height (int): Plant size (in centimeters).
            age (int): Plant age (in days).
        """
        self.name = name
        self.age = age
        self.height = height


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Summury:
            Initializes attributes corresponding to Plant and Flower
            information in a class to bring all the data together.

        Args:
            name (str): Same name as Plant.
            height (int): Same height as Plant.
            age (int): Same age as Plant.
            color (str): flower color.
        """
        super().__init__(name, height, age)

        self.color = color

        print(f"{self.name} (Flower): {self.height}cm, {self.age} days,"
              f" {self.color} color")

    def bloom(self) -> None:
        """
        Summury:
            state of blooming.
        """
        if (self.height <= 20):
            print(f"{self.name} is in the throes of adolescence.")
        elif (self.height > 20 and self.height <= 40):
            print(f"{self.name} has become a young adult.")
        elif (self.height > 40 and self.height <= 70):
            print(f"{self.name} is in the midst of a midlife crisis.")
        elif (self.height > 70):
            print(f"{self.name} is retiring")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Summury:
            Initializes attributes corresponding to Plant and Tree
            information in a class to bring all the data together.

        Args:
            name (str): Same name as Plant
            height (int): Same height as Plant
            age (int): Same age as Plant
            trunk_diameter (int): diameter of the tree trunk
        """
        super().__init__(name, height, age)

        self.trunk_diameter = trunk_diameter

        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,"
              f" {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """
        Summury:
            shadow surface.
        """
        print(f"{self.name} provides"
              f" {round((self.trunk_diameter * self.height) / 42)}"
              " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Summury:
            Initializes attributes corresponding to Plant and Vegetable
            information in a class to bring all the data together.

        Args:
            name (str): Same name as Plant.
            height (int): Same height as Plant.
            age (int): Same age as Plant.
            harvest_season (str): flowering season.
            nutritional_value (str): nutritional value of legumes.
        """
        super().__init__(name, height, age)

        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
              f" {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print(" Garden Plant Types ".center(50, "=") + "\n")
# ============= Garden Plant Types =============
# =================== Flower ===================
    flower = Flower("Rose", 80, 25, "red")
    flower.bloom()
    flower2 = Flower("Tulip", 10, 4, "pink")
    flower2.bloom()
    print("")
# ==================== Tree ====================
    flower = Tree("Oak", 50, 18, 5)
    flower.produce_shade()
    flower2 = Tree("Fir", 200, 320, 24)
    flower2.produce_shade()
    print("")
# ================== Vegetable =================
    flower = Vegetable("Tomato", 8, 3, "summer", "vitamin C")
    flower2 = Vegetable("Carrot", 12, 40, "summer", "vitamin B")
