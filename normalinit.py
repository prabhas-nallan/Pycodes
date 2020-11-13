class Student:
    def __init__(self):
        self.name='Tarun'
    
    def initialize(self,age):
        self.age=10
        print(self.age)
tarun=Student()
tarun.initialize(19)
h=Student()
h.initialize(17)
print(h.name)
print(tarun.name)