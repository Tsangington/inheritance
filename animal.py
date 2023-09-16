"""
Inheritance is a way of adding to exisiting classes and changing 
variables and methods. An example of this is having a dog class. 
You can create a variable and name your dog, and these dogs all 
have names so it is a base variable, and can bark, so it is a base method,
shown below:
"""
class Dog:
    def __init__(self, name, injured=False) -> None:
        self.name = name

    def bark(self):
        print(f"{self.name} barked.")
"""
But what if you wanted a german sheperd class, since they can herd sheep,
they need more variables and more methods. It is not a new class, since it is
still a dog, and has a name and barks. In this case, inheritance comes into
play. You can create a subclass, which inherits all the variables and methods
of dogs, but you can also add a method for herding sheep, and a variable related
such as years herding sheep, in this case.
"""
class GermanSheperd(Dog):
    def __init__(self, name, yearsHerdingSheep=0):
        Dog.__init__(self, name)
        self.yearsHerdingSheep = yearsHerdingSheep

    def herdSheep(self):
        print(f"{self.name} herded sheep.")
"""
Running the code below gives you an error, since goofy the dog, cannot use the
herdsheep method, since dog is not a subclass, while pluto can still use bark,
since the GermanSheperd is a subclass of the Dog class.
"""
goofy = Dog("goofy")
goofy.bark()
goofy.herdSheep()

pluto = GermanSheperd("pluto")
pluto.bark()
pluto.herdSheep()
