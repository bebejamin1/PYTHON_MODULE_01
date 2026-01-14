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
        self.name = name.capitalize()
        self.__age_b = 0
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
        return self.__age_b

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

    def set_age(self, age_b: int) -> None:
        """
        Summury:
            Check that the flower age is positive,
            otherwise it displays an error message.

        Args:
            height (int): flower age (in days)
        """
        if age_b < 0:
            print(f"Invalid operation attempted: age {age_b}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age_b = age_b
            print(f"Age updated: {self.__age_b} days [OK]")


if __name__ == "__main__":
    print(" Garden Security System ".center(50, "="))
# ============= Garden Security System =============
    flower_1 = SecurePlant("Rose")
    print(f"Plant created: {flower_1.name}")
    flower_1.set_height(12)
    flower_1.set_age(20)
    print("\n" + " Error Test ".center(50, "="))
# ========== direct modif, does not work ===========
    flower_1.__height = 42
    flower_1.__age_b = 42
# =================== Error Test ===================
    flower_1.set_height(-12)
    flower_1.set_age(-90)
# ================= Current Plant ==================
    print("\n" + "".center(50, "="))
    print(f"Current plant: {flower_1.name}", end=" ")
    print(f"({flower_1.get_height()}cm, {flower_1.get_age()} days)")
