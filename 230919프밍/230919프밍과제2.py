class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self, n):
        while n > 0:
            print("bark!")
            n -= 1

    def human_age(self):
        return self.age * 4
    
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self, n):
        while n > 0:
            print("moew~")
            n -= 1

    def human_age(self):
        return self.age * 4

if __name__ == '__main__':
    popo = Dog('popo', 10)
    popo.bark(3)
    print(popo)
    print('사람 나이로 환산 :', popo.human_age())

    pipi = Cat('pipi', 5)
    pipi.meow(4) 
    print(pipi)
    print('사람 나이로 환산 :', pipi.human_age())
