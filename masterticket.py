

TICKET_PRICE = 10

tickets_remaining = 100

#Output how many tickets are remaining using the tickets_remaining variable

print("There are {} tickets remaining." .format(tickets_remaining))

#Gather the users name and assign it to a new variable

user_name = input("What is your name?   ")

number_of_tickets = input("Hello {}, how many tickets would you like?   " .format(user_name))

price_for_user = number_of_tickets * TICKET_PRICE

print("OK! your price for {} tickets is {} dollars!" .format(number_of_tickets, price_for_user))


