

TICKET_PRICE = 10

tickets_remaining = 100

#Output how many tickets are remaining using the tickets_remaining variable

print("There are {} tickets remaining." .format(tickets_remaining))

#Gather the users name and assign it to a new variable
while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("What is your name?   ")

    number_of_tickets = input("Hello {}, how many tickets would you like?   " .format(user_name))
    number_of_tickets = int(number_of_tickets)
    price_for_user = number_of_tickets * TICKET_PRICE

    print("OK! your price for {} tickets is {} dollars!" .format(number_of_tickets, price_for_user))
    should_proceed = input("Do you want to proceed?   Y/N  ")
    if should_proceed.lower() == "y":
        print("SOLD!")
        tickets_remaining -= number_of_tickets
    else:
        print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are all sold out!")


