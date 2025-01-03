def show_event_details(event_name, total_seats, available_seats, booked_seats):
    print(f"\nEvent: {event_name}")
    print(f"Total Seats: {total_seats}")
    print(f"Available Seats: {available_seats}")
    print(f"Booked Seats: {booked_seats}")


def book_ticket(event_name, available_seats, booked_seats):
    try:
        # User input for ticket booking
        num_tickets = int(input(f"\nEnter the number of tickets you want to book for {event_name}: "))
        
        if num_tickets <= 0:
            print("Please enter a valid positive number of tickets.")
            return available_seats, booked_seats
        
        if num_tickets > available_seats:
            print(f"Sorry, only {available_seats} seats are available.")
            return available_seats, booked_seats
        
        # Booking the tickets
        available_seats = available_seats - num_tickets
        booked_seats += num_tickets
        print(f"\nSuccessfully booked {num_tickets} ticket(s) for {event_name}!")
        return available_seats, booked_seats
    except ValueError:
        print("Invalid input. Please enter a valid number of tickets.")
        return available_seats, booked_seats


def main():
    # Event details
    event_name = "Concert"
    total_seats = 100
    available_seats = total_seats
    booked_seats = 0

    print("Welcome to the Ticket Booking System!")
    
    while True:
        # Display event details
        show_event_details(event_name, total_seats, available_seats, booked_seats)
        
        # Ask the user if they want to book a ticket
        action = input("\nDo you want to book a ticket? (yes/no): ").lower()
        
        if action == "yes":
            available_seats, booked_seats = book_ticket(event_name, available_seats, booked_seats)
        elif action == "no":
            print("\nThank you for using the Ticket Booking System!")
            break
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()