import threading
from threading import*

# We can use locks to ensure that only one thread can access a shared resource (the reservation system) at a time

class RailwayReservationSystem:
    def __init__(self):
        self.lock = threading.Lock()
        self.reservations = {}

    def make_reservation(self, passenger_name, seat_number):
        with self.lock:
            if seat_number not in self.reservations:
                self.reservations[seat_number] = passenger_name
                print(f"Reservation successful! Seat number {seat_number} assigned to {passenger_name}")
            else:
                print(f"Seat number {seat_number} is already taken.")

reservation_system = RailwayReservationSystem()

# Simulate multiple threads trying to make reservations
threads = [threading.Thread(target=reservation_system.make_reservation, args=("Passenger " + str(i), i)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
    
    #OUTPUT
    
Reservation successful! Seat number 0 assigned to Passenger 0
Reservation successful! Seat number 1 assigned to Passenger 1
Reservation successful! Seat number 2 assigned to Passenger 2
Reservation successful! Seat number 3 assigned to Passenger 3
Reservation successful! Seat number 4 assigned to Passenger 4
Reservation successful! Seat number 5 assigned to Passenger 5
Reservation successful! Seat number 6 assigned to Passenger 6
Reservation successful! Seat number 7 assigned to Passenger 7
Reservation successful! Seat number 8 assigned to Passenger 8
Reservation successful! Seat number 9 assigned to Passenger 9



 #2nd Method

from threading import *
from time import *

class Railway: # If you created a class
    def __init__(self, available): # constructor is created
        self.available = available

    def reserve(self, wanted): # Reserve Seats
        if self.available >= wanted: # This is to check seats are available or not
            name = current_thread().name
            print('%d berth allowed for %s' %(wanted, name))
            self.available = self.available - wanted # This will decrease number of seats
        else:
            print("Seat are not Available")


obj = Railway(1) # available seat

T1 = Thread(target=obj.reserve, args=(1,)) # Operate First Person
T1.setName("First Person") # Set Name for T1
T1.start() # Initiate the Thread for First Person

T2 = Thread(target=obj.reserve, args=(1,)) # Operate Second Person
T2.setName("Second Person") # Set Name for T2
T2.start() # Initiate the Thread for Second Person

TP = int(input("\nHow Many Seats Do You want to book for Third Person : "))
T3 = Thread(target=obj.reserve, args=(TP,)) # Operate Third Person
T3.setName("Third Person") # Set Name for T3
T3.start() # Initiate the Thread for Third Person

#setName - set your name
#getName - Fetch your name



