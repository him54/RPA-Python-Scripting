# Thread Communication Using Boolean Type Variable

# from threading import *
# from time import *
#
#
# class producer:
#     def __init__(self):
#         self.lst = []
#         self.dataproduce = False
#
#     def produce(self):
#         for i in range(1, 11):
#             self.lst.append(i)
#             sleep(1)
#             print("Item produced........")  #This list have element [1,2 ------ 10]
#         self.dataproduce = True
#
#
# class consumer:
#     def __init__(self, prod):
#         self.prod = prod
#
#     def consume(self):
#         while self.prod.dataproduce == False:
#             sleep(0.1)
#             print((self.prod.lst))
#
#
# p = producer()
# c = consumer(p)
#
# t1 = Thread(target=p.produce) # Both operate simultaneously - > produce
# t2 = Thread(target=c.consume)  # ->  consumer
# t1.start()



#OUTPUT

[1]
[1]
[1]
[1]
[1]
[1]
[1]
[1]
[1]
Item produced........
[1, 2]
[1, 2]
[1, 2]
[1, 2]
[1, 2]
[1, 2]
[1, 2]
[1, 2]
[1, 2]
[1, 2]
Item produced........
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
Item produced........
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
Item produced........
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
Item produced........
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
Item produced........
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
Item produced........
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
Item produced........
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Item produced........
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Item produced........
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]





# We Use produce and consumer can't work in parellel
from threading import *
from time import *


class producer:
    def __init__(self, lock):
        self.lst = []
        self.dataproduce = False
        self.lock = lock

    def produce(self):
        for i in range(1, 11):
            self.lock.acquire() # acquire lock
            self.lst.append(i)
            sleep(1)
            print("Item produced........")
            self.lock.release() # release lock
        self.dataproduce = True


class consumer:
    def __init__(self, prod, lock):
        self.prod = prod
        self.lock = lock

    def consume(self):
        while self.prod.dataproduce == False:
            self.lock.acquire() # acquire lock
            print((self.prod.lst))
            self.lock.release() # release lock
            sleep(0.1)
        print("Consumer")


lock = Lock() # create a lock
p = producer(lock)
c = consumer(p, lock)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)
t1.start()
t2.start()
# t2.start()

#OUTPUT

Item produced........
Item produced........
Item produced........
Item produced........
Item produced........
Item produced........
Item produced........
Item produced........
Item produced........
Item produced........
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Consumer



