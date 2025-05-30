class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")  # Public method

# Creating an object of Car
car = Car("Toyota", "Camry")

# Accessing public attributes and methods
print(car.brand)  # Output: Toyota
car.display_info()  # Output: Brand: Toyota, Model: Camry

#Encapsulation when attributes are accessed through public method

class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute

    def __display_info(self):  # Private method
        print(f"Brand: {self.__brand}, Model: {self.__model}")

    def get_info(self):  # Public method to access private attribute
        return f"Brand: {self.__brand}, Model: {self.__model}"

# Creating an object of Car
car = Car("Toyota", "Camry")

# Trying to access private attributes and methods directly (will raise an error)
# print(car.__brand)  # AttributeError: 'Car' object has no attribute '__brand'

# Accessing private attribute via a public method
print(car.get_info())  # Output: Brand: Toyota, Model: Camry
