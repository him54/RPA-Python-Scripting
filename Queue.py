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
