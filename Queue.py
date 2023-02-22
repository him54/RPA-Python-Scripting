from threading import *
from time import *
from queue import*


class producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1,11):
            print("Producing Item:", i)
            self.q.put(i)
            sleep(1)

class consumer:
        def __init__(self,prod):
            self.prod = prod

        def consume(self):
            for i in range(1, 11):
                print("Receiving Item", self.prod.q.get(i))
                print('\n')


p = producer()
c = consumer(p)


t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()

#Queue is having two function 1- Get() 2 - put()



#OUTPUT
Producing Item: 1
Receiving Item 1


Producing Item: 2
Receiving Item 2


Producing Item: 3
Receiving Item 3


Producing Item: 4
Receiving Item 4


Producing Item: 5
Receiving Item 5


Producing Item: 6
Receiving Item 6


Producing Item: 7
Receiving Item 7


Producing Item: 8
Receiving Item 8


Producing Item: 9
Receiving Item 9


Producing Item: 10
Receiving Item 10
