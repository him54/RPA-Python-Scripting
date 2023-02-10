#t.start() - Start ur thread here
#t.join([timeout]) - Thread timeout
#t.daemon - This is property that takes either true or false

# creating a thread without using a class
#creating a thread by creating sub class to Thread class  - Inheritance


# from threading import*
# def display(s):
#     print(s)
# for i in range(5):
#     t = Thread(target=display, args=('Hello',))
#     t.start()

# from threading import*
# class MyThread(Thread):
#     def __init__(self, s):
#         #super().__init__()      #super() function is used to give access to methods and properties of a parent or sibling class.
#                                  # The super() function returns an object that represents the parent class.
#         Thread.__init__(self)
#         self.s = s
#     def run(self):
#         print(self.s)
#
# t1=MyThread("Hello")
# t1.start()
# t1.join()

from threading import
class MyThread(Thread):
    def __init__(self, s):
        #super().__init__()      #super() function is used to give access to methods and properties of a parent or sibling class.
                                 # The super() function returns an object that represents the parent class.
        Thread.__init__(self)
        self.s = s
    def display(self, x, y):
        print(self.s)
        print(x,y)

obj=MyThread("Hello")
t1=Thread(target=obj.display, args=(1,2,))
t1.start()
t1.join()

#OUTPUT
Hello
1 2


