class animal:

    hasscales = True
    def sound(self):
        print("animal is speaking")


class dog(animal):
    haspaws= True
    def move(self):
           print("Dog is moving")

class cat(animal):
    haspaws = True
    def move(self):
        print("Cat is moving")

a = animal()
b = dog()
c = cat()





