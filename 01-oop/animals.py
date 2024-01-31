from abc import ABC, abstractclassmethod

class Animal(ABC): 
    @abstractclassmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Wooof")

class Cat(Animal):
    def sound(self):
        print("Mieow")

class Duck(Animal):
    def sound(self):
        print("Quack")

animals = [Dog(), Duck(), Cat()]

for a in animals:
    a.sound()