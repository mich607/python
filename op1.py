class person:
    def __init__(self, name, age, gender, courses):

        self.name = name
        self.age = age
        self.gender = gender
        self.courses = courses

    def study(self):
            print(self.name, self.age, self.gender, self.courses)
person1 = person("mat",12,"Male","Python")
person1.study()



class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(self.make, self.model, self.year)

car1 = car("BMW","Ford","2021")
car1.drive()
car2 = car("juke","nissan","2021")
car2.drive()
car3 = car("BMW","Ford","2021")
car3.drive()

class device:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def crush(self):
          print(self.model,"has been crushed")

computer = device("hp",2008)
computer.crush()
laptop = device("laptop",2021)
laptop.crush()