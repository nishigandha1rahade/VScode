class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand  # private attribute
        self.__model = model  # private attribute
        self.__year = year    # private attribute

    # Getter method for brand
    def get_brand(self):
        return self.__brand

    # Setter method for brand
    def set_brand(self, brand):
        self.__brand = brand

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        self.__model = model

    # Getter method for year
    def get_year(self):
        return self.__year

    # Setter method for year
    def set_year(self, year):
        self.__year = year

    # Method to display car details
    def display_info(self):
        print(f"Car Details: {self.__brand} {self.__model} ({self.__year})")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes via getter methods
my_car.display_info()

# Modifying attributes using setter methods
my_car.set_brand("Honda")
my_car.set_model("Civic")
my_car.set_year(2022)

# Accessing updated attributes via getter methods
my_car.display_info()
