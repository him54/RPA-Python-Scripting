#Random - Generate your random function
#random.randint(1, 10) - 1 to 10 include number
#random.randrancy(1,10)  - 1 to 9
#random.randient(3.5, 5) - Showing error becom not used any float value random function

from threading import*
from time import*
class threatre:

    def __init__(self, str):
        self.str = str
    def movieShow(self):

        print(self.str)

obj1 = threatre("CUT THE TICKET") # Deal with ur checking portion
obj2 = threatre("SHOW THE SEAT")

t1 = Thread(target=obj1.movieShow)
t2 = Thread(target=obj2.movieShow)

t1.start()
t2.start()

