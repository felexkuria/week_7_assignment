# Assignment 1: Design Your Own Class! 🏗️

# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).

# Add attributes and methods to bring the class to life!

# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals or
#  vehicles with the same action (like move()). However, make each class define move() 
# differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Activity 3: Encapsulation Challenge! 🔒

# Updated Book class with a constructor
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def get_details(self):
        return f"{self.author}, {self.title}"

book = Book("Samir Isamir", "EXOs Exponential Organization")
print(book.get_details())

# Updated SuperHero class with corrected id initialization
class SuperHero:
    def __init__(self, name, movie, hero_id):
        self.name = name
        self.movie = movie
        self._id = hero_id  # Encapsulation: Protected attribute

    def moving(self):
        return f"{self.name} is moving!"

supperman = SuperHero("SuperMan", "Into SpiderVerse", 1)
print(supperman.moving())
print(supperman.name)

# Polymorphism Challenge: Adding two classes with the same method but different implementations
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

# Demonstrating polymorphism
vehicles = [Car(), Plane()]
for vehicle in vehicles:
    print(vehicle.move())

# Encapsulation Challenge: Adding private attributes with getter/setter methods
class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        return "Invalid withdrawal amount."

# Example usage of BankAccount
account = BankAccount("John Doe", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(300))