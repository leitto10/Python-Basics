TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# run this code continioslly until we run out of tickets.
while tickets_remaining:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = raw_input("What is your name: ")
    num_tickets = input("How many tickets would you like? {}  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("ho no, we run in to a problem.")
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = raw_input("Do you want to proceed?  y/n : ")

        if should_proceed.lower() == "y":
            print("Tickets sold....")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways {}! ".format(name))

print("Sorry, the tickets are all sold out... :(")