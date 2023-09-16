# inheritance
Example of inheritance

Inheritance is a way of adding to exisiting classes and changing 
variables and methods. An example of this is having a dog class.You can create a variable and name your dog, and these dogs all have names so it is a base variable, and can bark, so it is a base method.

But what if you wanted a german sheperd class, since they can herd sheep, they need more variables and more methods. It is not a new class, since it is still a dog, and has a name and barks. In this case, inheritance comes into play. You can create a subclass, which inherits all the variables and methods of dogs, but you can also add a method for herding sheep, and a variable related such as years herding sheep, in this case.

Running the code below gives you an error, since goofy the dog, cannot use the herdsheep method, since dog is not a subclass, while pluto can still use bark, since the GermanSheperd is a subclass of the Dog class.

Another example of how this might be useful is games. this example has an enemy class, and using inheritance, we can have 2 different types of enemies with default stats, each with their own abilities.

In python, inherited classes can be initialised in both of these ways. Using super(), it automatically inherits the parent class, in the brackets of the Spider class. You can also do it manually.

You can overwrite parent methods using inheritance as well.Take for example this superSpider. It inherits all the variables, and methods then overwrites them, with different values, and the same shootWeb() method, but this time it "slows" the player a lot instead.

The other difference in python inheritance isthe fact you can have multiple parent classes. Other languages usually only can have 1 class. Running the code below shows that jose can have 2 variables, inherited from separate classes, showing pythons multi class inheritance.