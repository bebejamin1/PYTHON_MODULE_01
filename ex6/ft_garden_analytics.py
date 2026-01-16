#! /bin/python3.10

class SecurePlant:
    __total_plant = 0

    def get_total() -> int:
        """
        Summary:
            Get the total number of plants created.

        Returns:
            int: Total number of plants.
        """
        return (SecurePlant.__total_plant)

    def set_total(plant: int) -> None:
        """
        Summary:
            Set the total number of plants.

        Args:
            plant (int): Number of plants to add.
        """
        SecurePlant.__total_plant = plant + SecurePlant.get_total()

    def __init__(self, name: str, age: int, height: int) -> None:
        """
        Summary:
            Initializes attributes corresponding to SecurePlant
            information in a class to bring all the data together.

        Args:
            name (str): Plant name.
            age (int): Plant age (in days).
            height (int): Plant size (in centimeters).
        """
        self.name = name.capitalize()
        self.__age = age
        self.__height = height
        SecurePlant.set_total(SecurePlant.get_total() + 1)

    def get_height(self) -> int:
        """
        Summary:
            Get the current height of the plant.

        Returns:
            int: Plant height in centimeters.
        """
        return self.__height

    def set_height(self, height: int) -> None:
        """
        Summary:
            Set the height of the plant with validation.

        Args:
            height (int): New height in centimeters.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def get_age(self) -> int:
        """
        Summary:
            Get the current age of the plant.

        Returns:
            int: Plant age in days.
        """
        return self.__age

    def set_age(self, age: int) -> None:
        """
        Summary:
            Set the age of the plant with validation.

        Args:
            age (int): New age in days.
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def grow(self) -> None:
        """
        Summary:
            Increase plant height by 1 centimeter.
        """
        self.__height += 1

    def get_info(self) -> None:
        """
        Summary:
            Print plant information based on its type.
        """
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
        """
        Summary:
            Initializes attributes corresponding to SecurePlant and
            FloweringPlant information in a class to bring all the
            data together.

        Args:
            name (str): Same name as SecurePlant.
            height (int): Same height as SecurePlant.
            age (int): Same age as SecurePlant.
            color (str): Flower color.
            plant_state (str): Current state of the plant.
        """
        super().__init__(name, height, age)
        self.__color = color
        self.__plant_state = plant_state

    def get_color(self) -> str:
        """
        Summary:
            Get the color of the flowers.

        Returns:
            str: Flower color.
        """
        return (self.__color)

    def set_color(self, color: str) -> None:
        """
        Summary:
            Set the color of the flowers.

        Args:
            color (str): New flower color.
        """
        self.__color = color

    def get_state(self) -> str:
        """
        Summary:
            Get the current state of the plant.

        Returns:
            str: Plant state.
        """
        return (self.__plant_state)

    def set_state(self, plant_state: str) -> None:
        """
        Summary:
            Set the state of the plant.

        Args:
            plant_state (str): New plant state.
        """
        self.__plant_state = plant_state


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, plant_state: str, prize: int) -> None:
        """
        Summary:
            Initializes attributes corresponding to FloweringPlant and
            PrizeFlower information in a class to bring all the data
            together.

        Args:
            name (str): Same name as FloweringPlant.
            height (int): Same height as FloweringPlant.
            age (int): Same age as FloweringPlant.
            color (str): Same color as FloweringPlant.
            plant_state (str): Same plant state as FloweringPlant.
            prize (int): Prize points for this flower.
        """
        super().__init__(name, height, age, color, plant_state)
        self.__prize = prize

    def get_prize(self) -> int:
        """
        Summary:
            Get the prize points of the flower.

        Returns:
            int: Prize points.
        """
        return self.__prize

    def set_prize(self, prize: int) -> None:
        """
        Summary:
            Set the prize points with validation.

        Args:
            prize (int): New prize points value.
        """
        if prize < 0:
            print(f"Invalid operation attempted: height {prize} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__prize = prize


class GardenManager():
    """
    Summary:
        Manages a garden with multiple plants and provides statistics.
    """

    class GardenStats():
        """
        Summary:
            Inner class for tracking garden statistics and evolution.
        """

        total_garden = 0

        def __init__(self, garden: object) -> None:
            """
            Summary:
                Initializes garden statistics tracking.

            Args:
                garden (object): Reference to the parent GardenManager.
            """
            self.__garden = garden
            self.__cm_tracker = 0
            self.__regular_count = 0
            self.__flowering_count = 0
            self.__prize_flowers = 0
            GardenManager.GardenStats.total_garden += 1

        def get_garden(self) -> object:
            """
            Summary:
                Get the associated garden manager.

            Returns:
                object: The garden manager object.
            """
            return (self.__garden)

        def set_garden(self, new_garden: object) -> None:
            """
            Summary:
                Set a new garden manager.

            Args:
                new_garden (object): New garden manager to associate.
            """
            self.__garden = new_garden

        def get_cm_tracker(self) -> int:
            """
            Summary:
                Get the total centimeters of growth tracked.

            Returns:
                int: Total growth in centimeters.
            """
            return (self.__cm_tracker)

        def set_cm_tracker(self, cm: int) -> None:
            """
            Summary:
                Set the centimeter tracker value.

            Args:
                cm (int): New centimeter value.
            """
            self.__cm_tracker = cm

        def add_cm(self, cm_add) -> None:
            """
            Summary:
                Add centimeters to the growth tracker.

            Args:
                cm_add (int): Centimeters to add.
            """
            self.__cm_tracker += cm_add

        def garden_evolution(self):
            """
            Summary:
                Print the evolution statistics of the garden.
            """
            print(f"Plants added: {len(self.__garden.get_garden_content())},",
                  f"Total growth: {self.__cm_tracker}cm")
            print(f"Pant types: {self.__regular_count} regular, "
                  f"{self.__flowering_count} flowering, "
                  f"{self.__prize_flowers} prize flowers")

        def plant_type_count(self, plant: SecurePlant) -> None:
            """
            Summary:
                Count plant type and update statistics.

            Args:
                plant (SecurePlant): Plant to categorize and count.
            """
            if (isinstance(plant, PrizeFlower)):
                self.__prize_flowers += 1
            elif (isinstance(plant, FloweringPlant)):
                self.__flowering_count += 1
            elif (isinstance(plant, SecurePlant)):
                self.__regular_count += 1

        @staticmethod
        def plant_score(plant: SecurePlant) -> int:
            """
            Summary:
                Calculate score for a plant based on its type.

            Args:
                plant (SecurePlant): Plant to score.

            Returns:
                int: Score points for the plant.
            """
            if (isinstance(plant, PrizeFlower)):
                return (20 * plant.get_prize())
            if (isinstance(plant, FloweringPlant)):
                return (10)
            if (isinstance(plant, SecurePlant)):
                return (8)

        def garden_score(self) -> int:
            """
            Summary:
                Calculate the total score of the garden.

            Returns:
                int: Total garden score.
            """
            result = 0
            for plant in self.__garden.get_garden_content().values():
                result += GardenManager.GardenStats.plant_score(plant)
            return (result)

        def height_validation(self) -> bool:
            """
            Summary:
                Validate that all plants meet minimum height requirement.

            Returns:
                bool: True if all plants are 20cm or higher, False otherwise.
            """
            for plant in self.__garden.get_garden_content().values():
                if (plant.get_height() < 20):
                    return (False)
            return (True)

    def __init__(self, owner: str) -> None:
        """
        Summary:
            Initializes a garden manager for a specific owner.

        Args:
            owner (str): Name of the garden owner.
        """
        self.__owner = owner
        self.__garden_content = {}
        self.stats = GardenManager.GardenStats(self)

    def get_owner(self) -> str:
        """
        Summary:
            Get the name of the garden owner.

        Returns:
            str: Owner name.
        """
        return (self.__owner)

    def set_owner(self, owner: str) -> None:
        """
        Summary:
            Set the name of the garden owner.

        Args:
            owner (str): New owner name.
        """
        self.__owner = owner.capitalize()

    def get_garden_content(self) -> dict:
        """
        Summary:
            Get all plants in the garden.

        Returns:
            dict: Dictionary of plants in the garden.
        """
        return (self.__garden_content)

    def set_garden_content(self, garden_content: dict) -> None:
        """
        Summary:
            Set the garden content.

        Args:
            garden_content (dict): New dictionary of plants.
        """
        self.__garden_content = garden_content

    @classmethod
    def create_garden_network(cls, owner_list: list) -> list:
        """
        Summary:
            Create multiple garden managers for a list of owners.

        Args:
            owner_list (list): List of owner names.

        Returns:
            list: List of GardenManager instances.
        """
        lst = []
        for owner in owner_list:
            lst += [cls(owner)]
        return (lst)

    def add_to_garden(self, plant: SecurePlant) -> None:
        """
        Summary:
            Add a plant to the garden.

        Args:
            plant (SecurePlant): Plant to add to the garden.
        """
        print(f"Added {plant.name} to {self.get_owner()}'s garden")
        self.get_garden_content()[plant.name] = plant
        self.stats.plant_type_count(plant)

    def grow_plant(self, plant_name: str) -> None:
        """
        Summary:
            Make a specific plant grow by 1 centimeter.

        Args:
            plant_name (str): Name of the plant to grow.
        """
        plant: SecurePlant
        plant = (self.get_garden_content())[plant_name]
        plant.grow()
        self.stats.add_cm(1)
        print(f"{plant.name} grew 1 cm")

    def grow_all(self):
        """
        Summary:
            Make all plants in the garden grow by 1 centimeter each.
        """
        print(f"{self.get_owner()} is helping all plants grow...")
        plant: SecurePlant
        for plant in self.get_garden_content().values():
            self.grow_plant(plant.name)

    def garden_info(self) -> None:
        """
        Summary:
            Print information about all plants in the garden.
        """
        print("Plants in garden:")
        for plant in self.get_garden_content().values():
            plant.get_info()


def fc_grow_all(garden: GardenManager) -> None:
    """
    Summary:
        Helper function to make all plants in a garden grow.

    Args:
        garden (GardenManager): Garden manager instance.
    """
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
    # Bob.add_to_garden(FloweringPlant("Pine", 500, 50, "green", "blooming"))
    # Bob.add_to_garden(SecurePlant("spruce", 500, 50))
    # Bob.add_to_garden(SecurePlant("sprud", 500, 50))
    # Bob.add_to_garden(SecurePlant("spru", 500, 50))
    # Bob.add_to_garden(PrizeFlower("Daisy", 30, 30, "white", "blooming", 3))
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
