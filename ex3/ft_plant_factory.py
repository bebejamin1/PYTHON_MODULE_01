#! /bin/python3.10

class Flower:
    def __init__(self, name: str, height: int, age_b: int) -> None:
        """
        Summury:
            Initializes attributes corresponding to flower information in
            a class to bring all the data together.

        Args:
            name (str): flower name
            height (int): flower size (in centimeters)
            age (int): flower age (in days)
        """
        self.name = name
        self.height = height
        self.age_b = age_b

    def creat_flower(self, name_f: str, height_f: int, age_b_f: int) -> None:
        self.name = name_f
        self.height = height_f
        self.age_b = age_b_f

    def age(self) -> None:
        """
        Summury:
            Increases age
        """
        self.age_b += 1

    def grow(self) -> None:
        """
        Summury:
            Increases height
        """
        self.height += 1

    def get_info(self) -> None:
        """
        Summury:
            Displays plant information
        """
        print(f"{self.name}: {self.height}cm, {self.age_b} days old")


def ft_plant_factory():
    """
    Summury:
        Create a flower using the Flower class.
        Use age() and grow() to modify the plant's information.
        Display its information before and after growth.
        Distinguish between before and after.
    """
    days = 1
    print(f"Day {days}".center(20, "-"))
    flower = Flower.creat_flower("Tulipe", 12, 20)
    Flower.get_info(flower)
    for days in range(2, 8):
        Flower.age(flower)
        Flower.grow(flower)
    print("\n" + f"Day {days}".center(20, "-"))
    Flower.get_info(flower)


ft_plant_factory()
