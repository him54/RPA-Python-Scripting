from threading import*
l1 = Lock()
l2 = Lock()

def bookticket():
    l1.acquire()
    print("Bookticket locked on train")
    print("Bookticket wants to look on compartment")
    l2.acquire()
    print("Bookticket locked on compartment")
    l1.release()
    l2.release()
    print("Booking a ticket is done")

 # The locks are acquired in the same order in both threads

def cancelticket(): # This is our task thread number 2
    l2.acquire()
    print("Cancel ticket locked compartment") # we are having two thread one is reservation and one is cancelation
    print("cancel ticket wants to lock on train")
    l1.acquire()
    print("cancel ticket locked train")
    l1.release()
    l2.release()
    print("cancellation ticket is done")


T1 = Thread(target = bookticket)
T2 = Thread(target = cancelticket)

T1.start()
T2.start


#When bookticket() acquires l1 lock and cancelticket() acquires l2 lock,
# both threads are blocked waiting for the other lock to be released before proceeding.
# Since both threads are waiting for each other to release the lock they hold, the program will be stuck in this state indefinitely,
# resulting in a deadlock.
