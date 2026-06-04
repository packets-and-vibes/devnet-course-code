class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def display_person(self):
        return f'Person({self.name}, {self.age})'