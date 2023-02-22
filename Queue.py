from threading import *
from time import *
from queue import*


class producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(11):
            print("Producing Item:", i)
            self.q.put(i)
            sleep(1)

class consumer:
        def __init__(self,prod):
            self.prod = prod

        def consume(self):
            for i in range(1, 11):
                print("Receiving Item", self.prod.q.get(i))


pr = producer()
cn = consumer(pr)


t1=Thread(target=pr.produce)
t2=Thread(target=cn.consume)
t1.start()
t2.start()

#Queue is having two function 1- Get() 2 - put()


#OUTPUT
Producing Item: 0
Reseiving Item 0
Producing Item: 1
Reseiving Item 1
Producing Item: 2
Reseiving Item 2
Producing Item: 3
Reseiving Item 3
Producing Item: 4
Reseiving Item 4
Producing Item: 5
Reseiving Item 5
Producing Item: 6
Reseiving Item 6
Producing Item: 7
Reseiving Item 7
Producing Item: 8
Reseiving Item 8
Producing Item: 9
Reseiving Item 9
Producing Item: 10
