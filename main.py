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
class Book:
    author="Samir Isamir"
    titel="EXOs Exponetioana Organization"
book =Book()
print(f"{book.author},{book.titel}")

class SuperHero:
    def __init__(self, name,movie,id):
        self.name=name
        self.movie=movie
        self.id =id._id
    def moving(self):
        print("Moving")
supperman=SuperHero("SuperMan","Into SpiderVerse",1)
print (supperman.moving())
print(supperman.name)