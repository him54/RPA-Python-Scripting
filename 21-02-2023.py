#notiify() - Is used by the produser - Then my task is completed
#wait() - it is used by the consumer

#one your production is done then we will go with consumption

from threading import Thread, Condition
from time import sleep

class Producer:
    def __init__(self):
        self.lst = []
        self.c = Condition()

    def produce(self):
        self.c.acquire()
        for i in range(11):
            self.lst.append(i)
            sleep(i)
            print("Item Purchased")
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        self.prod.c.acquire()
        while not self.prod.lst:
            self.prod.c.wait()
        self.prod.c.release()
        print(self.prod.lst)

pr = Producer()
cn = Consumer(pr)

t1 = Thread(target=pr.produce)
t2 = Thread(target=cn.consume)

t1.start()
t2.start()


# from threading import *
# from time import *
#
# class producer:
#     def __init__(self):
#         self.lst= []
#         self.c = Condition()
#
#     def produce(self):
#
#             self.c.acquire()
#
#             for i in range(11):
#                 self.lst.append(i)
#                 sleep(1)
#                 print("Item produced")
#             self.c.notify()
#             self.c.release()
#
# class consumer:
#         def __init__(self,prod):
#             self.prod = prod
#
#         def consume(self):
#             self.prod.c.acquire()
#             self.prod.c.wait(timeout=0)
#             self.prod.c.release()
#
#
# pr = producer()
# cn = consumer(pr)
#
#
# t1=Thread(target=pr.produce)
# t2=Thread(target=cn.consume)
# t1.start()
# t2.start()
