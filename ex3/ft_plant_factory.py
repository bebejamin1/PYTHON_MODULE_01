#! /bin/python3.10

class Flower:
    plant_count = 0

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
        self.name = name.capitalize()
        self.height = height
        self.age_b = age_b
        Flower.plant_count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age_b} days)")


if __name__ == "__main__":
    print(" Plant Factory Output ".center(50, "="))
    flower_1 = Flower(name="tulip", height=15, age_b=12)
    flower_2 = Flower(name="Rose", height=23, age_b=11)
    flower_3 = Flower(name="Daisy", height=12, age_b=14)
    flower_4 = Flower(name="bollockwort", height=36, age_b=62)
    flower_5 = Flower(name="Daffodil", height=28, age_b=51)
    print("\n" + f"Total plants created: {Flower.plant_count}")
