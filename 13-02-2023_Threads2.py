import time
from threading import*  #it is module

class Mythread:
    def task(self): # create a function
        self.task1()  # These are decleration of the function
        self.task2()
        self.task3()
    def task1(self):
        print("step1 of my problem") # step1 is your task1
        time.sleep(5)
        print("step completely")


    def task2(self):
        print("step2 of my problem")
        time.sleep(5)
        print("step completely")

    def task3(self):
        print("step2 of my problem")
        time.sleep(5)
        print("step completely")



obj = Mythread() # create a object
t = Thread(target=obj.task)
t.start() # Starts a python thread
