import random

# Total seats
TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))

# Store bookings
bookings = {}

# Generate booking ID
def generate_id():
    return random.randint(1000, 9999)

# Check availability
def check_availability():
    print(f"\nAvailable Seats: {len(available_seats)}")
    print(available_seats)

# Book ticket
def book_ticket():
    if not available_seats:
        print("\nNo seats available!")
        return

    name = input("Enter name: ")
    age = input("Enter age: ")

    seat = available_seats.pop(0)
    booking_id = generate_id()

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print(f"\nTicket booked successfully!")
    print(f"Booking ID: {booking_id}, Seat No: {seat}")

# View ticket
def view_ticket():
    booking_id = int(input("Enter Booking ID: "))

    if booking_id in bookings:
        data = bookings[booking_id]
        print("\n--- Ticket Details ---")
        print(f"Name
