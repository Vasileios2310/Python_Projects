class Robot:
    # variable class , counts the number of robots
    poppulation = 0
    
    def __init__(self , name):
        # name is an object variable
        self.name = name
        print('Initializing {0}' .format(self.name))
        
        # when a new is created , it is added in population
        Robot.poppulation += 1
    
    def __del__(self):
        print('{0} is beaing destroyed'.format(self.name))
        
        Robot.poppulation -= 1
        
        if Robot.poppulation == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working' .format(Robot.poppulation))
    
    def sayHi(self):
        print('Greetings , my masters call me {0}'.format(self.name))
    
    #@staticmethod
    def howMany():
        """Prints the current population"""
        print('The current population is {0}'.format(Robot.poppulation))
    
    howMany = staticmethod(howMany)

robot1 = Robot('RBT1')
robot1.sayHi()
Robot.howMany()

robot2 = Robot('RBT2')
robot2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

del robot1
del robot2

Robot.howMany()