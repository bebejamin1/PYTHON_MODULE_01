#! /bin/python3.10

class Flower:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Summury:
            Initializes attributes corresponding to flower information in
            a class to bring all the data together.

        Args:
            name (str): flower name
            height (int): flower size (in centimeters)
            age (int): flower age (in days)
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """
        Summury:
            Identify three flowers, giving them a name, size, and age.
            Using our Flower class.
    """
    flower_1 = Flower(name="Rose", height=25, age=30)
    print(f"{flower_1.name}: {flower_1.height}cm, {flower_1.age} days old")
    flower_2 = Flower(name="Sunflower", height=80, age=45)
    print(f"{flower_2.name}: {flower_2.height}cm, {flower_2.age} days old")
    flower_3 = Flower(name="Cactus", height=15, age=120)
    print(f"{flower_3.name}: {flower_3.height}cm, {flower_3.age} days old")


if __name__ == "__main__":
    print(" Garden Plant Registry ".center(30, "-") + "\n")
    ft_garden_data()
    print("\n" + " End of Program ".center(30, "-"))
