class Animal:
    def eat(self):
        print("Animal is Eating")
        
class Dog(Animal):
    def bark(self):
        print("The dog is Barking")
        
d = Dog()

d.bark()
d.eat()