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
