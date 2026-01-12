#! /bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int) -> object:

        self.name = name
        self.age_b = age
        self.height = height


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> object:
        super().__init__(name, height, age)

        self.color = color


if __name__ == "__main__":
