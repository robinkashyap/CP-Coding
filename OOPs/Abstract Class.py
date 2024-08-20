# An abstract class in programming is a class that cannot be instantiated on its own and serves as a blueprint for other classes. 
# It can contain abstract methods, which are methods that are declared but not fully implemented, requiring subclasses to provide 
# their own specific implementations of these methods. 
# Abstract classes are used to define common behavior that multiple subclasses should follow.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Buffalo(Animal):
    def sound():            # if this function is not defined then on line 33 it will give error (Can't instantiate abstract class Buffalo without an implementation for abstract method 'sound')
        pass
    def sound_buff(self):
        return "Error!"
     
dog = Dog()
cat = Cat()
buf = Buffalo()

print(dog.sound())
print(cat.sound())
print(buf.sound_buff())