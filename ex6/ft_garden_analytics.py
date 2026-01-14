#! /bin/python3.10

class SecurePlant:
    def __init__(self, name: str) -> None:
        """
        Summury:
            Initializes attributes corresponding to flower information in
            a class to bring all the data together.

        Args:
            name (str): flower name
        """
        self.name = name
        self.__age = 0
        self.__height = 0

    def get_height(self) -> int:
        """
        Summury:
            return flower size

        Returns:
            int: flower size (in centimeters)
        """
        return self.__height

    def get_age(self) -> int:
        """
        Summury:
            return flower age

        Returns:
            int: flower age (in days)
        """
        return self.__age

    def set_height(self, height: int) -> None:
        """
        Summury:
            Check that the flower size is positive,
            otherwise it displays an error message.

        Args:
            height (int): flower size (in centimeters)
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Summury:
            Check that the flower age is positive,
            otherwise it displays an error message.

        Args:
            height (int): flower age (in days)
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

        class GardenStats():
            total_garden = 0



class Plant:
    

if __name__ == "__main__":
    print(" Garden Management System Demo ".center("=", 50))
# ============= Garden Plant Types =============
# =================== Flower ===================
    print("ahahaha")
