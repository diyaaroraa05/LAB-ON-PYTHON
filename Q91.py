#polymorphism

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
def make_animal_speak(animal):
    print(animal.speak())
dog = Dog()
cat = Cat()
make_animal_speak(dog) # Output: Woof!
make_animal_speak(cat) # Output: Meow!

print("Program by jashn sharma - 0221BCA048")