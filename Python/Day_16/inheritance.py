# Parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# Child class
class Penguin(Bird):

    def __init__(self):
        # call super() function to pull the content of parent class method
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

import pdb; pdb.set_trace()
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
