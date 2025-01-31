class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age =  age 
    
    def info(self):
        print(f"I am Cat .My name is {self.name}. I am {self.age} years old" )

    def sound(self):
        print("Meow")



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am Dog .My name is {self.name}. I am {self.age} years old")

    def sound(self):
        print("Bark")


cat1 = Cat("Tyson",2.5)
dog1 = Dog("Tommy",7)


for animal in (cat1,dog1):
    animal.sound()
    animal.info()