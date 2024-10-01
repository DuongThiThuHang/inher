class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def __repr__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
from person import Person

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return f"Child(Name: {self.name}, Age: {self.age})"
from child import Child
person = Person("Alice", 30)
print(person) 
child = Child("Bob", 10)
print(child)       