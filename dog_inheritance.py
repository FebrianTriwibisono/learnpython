#parent class
class Dog:
    #class attribute
    species = 'mammal'

    #instantiation
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    #instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)
    def speak(self, sound):
        return "{} speaks {}!".format(self.name, sound)

#Child class (inherits from Dog Class)
class RusselTerrier(Dog):
    def run(self, speed):
        return "{} runs {} km/h.".format(self.name, speed)

class Dalmatians(Dog):
    def run(self, speed):
        return "{} runs {} km/h.".format(self.name, speed)

#child classes inherit attributes and behavior form parent class
dog_1 = RusselTerrier("Saber", 10)
dog_2 = Dalmatians("Rider", 5)

print(dog_1.description())
print(dog_2.description())
print(dog_1.run(50))
print(dog_2.run(20))