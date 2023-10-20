class Duck:

    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")


class Chicken:

    def talk(self):
        print("This duck is clucking")

class Person:

    def catch(self, animal):
        animal.walk()
        animal.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)