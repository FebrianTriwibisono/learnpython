#define class
class Animal:
    #define property of class
    species = 'mammal'

    #define instance, self is the same as 'this' in php
    #self must be declared in instance's parameter
    def __init__ (self, nama, tipe, umur):
        self.nama = nama
        self.tipe = tipe
        self.umur = umur
    
    #To call a method from the class, use @staticmethod
    @staticmethod
    def get_bigest_number(*args):
        return max(args)

    #instance method
    def description(self):
        return "{} is a {} and {} years old".format(self.nama, self.tipe, self.umur)

    #instance method
    def speak(self, sound):
        return "{} speaks {}".format(self.nama, sound)

    #instance method
    def element(self, tipeElement):
        return "{} is a {} type animal".format(self.nama, tipeElement)

#creating objects
animal_1 = Animal("Nora", "cat", 9)
animal_2 = Animal("Shiro", "dog", 7)
animal_3 = Animal("Alice", "Rabbit", 4)

#Showing output, .format is used for capturing obejct's data to be shown in output
print ("{} is a {} and {} is a {}".format(animal_1.nama, animal_1.tipe, animal_2.nama, animal_2.tipe))

#simple conditional in python
if animal_1.species == "mammal":
    print("{0} and {1} is a {2}".format(animal_1.nama, animal_2.nama, animal_2.species))
else:
    print("{0} and {1} is not a mammal".format(animal_1.nama, animal_2.nama))

#call the method through the class Animal
print("The oldest is {} years old".format(Animal.get_bigest_number(animal_1.umur, animal_2.umur, animal_3.umur)))

#call instance of method
print(animal_1.description())
print(animal_1.speak("Nyaaan!"))
print(animal_1.element("lightning"))