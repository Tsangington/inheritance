class Enemy():
    def __init__(self, damage, hitpoints, speed):
        self.damage = damage
    
    def hit(self, playerHP):
        return(playerHP- self.damage)

    def getHit(self, playerDMG):
        return(self.hitpoints - playerDMG)
"""
Another example of how this might be useful is games. this
example has an enemy class, and using inheritance, we can 
have 2 different types of enemies with default stats, each with
their own abilities.
"""
#2 different ways to inherit
#Using super(), automatically inherits from parent class
class Spider(Enemy):
    def __init__(self, damage=2, hitpoints=10, speed=30):
        super().__init__(damage, hitpoints, speed)
    
    def shootWeb(self):
        print("Player slowed")
"""
In python, inherited classes can be initialised in both of these ways.
using super(), it automatically inherits the parent class, in the brackets
of the Spider class.
You can also do it manually, shown below.
"""
#manual inheritance
class Zombie(Enemy):
    def __init__(self, damage=10 , hitpoints=30, speed=10):
        Enemy.__init__(damage, hitpoints, speed)
    
    def bite(self):
        print("Player weakened")
"""
You can overwrite parent methods using inheritance as well.
Take for example this superSpider. It inherits all the variables,
and methods then overwrites them, with different values, and 
the same shootWeb() method, but this time it "slows" the player
a lot instead.
"""
# Overwriting parent methods
class SuperSpider(Spider):
    def __init__(self, damage=5, hitpoints=20, speed=50):
        super().__init__(damage, hitpoints, speed)
    
    def shootWeb(self):
        print("Player very slowed")

superSpider = SuperSpider()
superSpider.shootWeb()

normalSpider = Spider()
normalSpider.shootWeb()