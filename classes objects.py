# class is a blue print of an object
# object is an instance of a class
class Person:
    name = "james"
    age = 23
    gender = "male"

    #method/function/behaviors
    def move(self):
        print(self.name, "is moving")
farmer = Person()
farmer.move()
print(farmer.name)

thief = Person()
thief.move()
print(thief.age)