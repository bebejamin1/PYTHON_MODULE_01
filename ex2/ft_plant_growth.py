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


if __name__ == "__main__":
    print("Day 1".center(20, "-"))
    flower = Flower(name="Rose", height=25, age_b=30)
    original = flower.height
    Flower.get_info(flower)
    days = 1
    for days in range(2, 8):
        Flower.age(flower)
        Flower.grow(flower)
    print("\n" + f"Day {days}".center(20, "-"))
    Flower.get_info(flower)
    stat = flower.height - original
    print(f"Growth this week: +{stat}cm")
