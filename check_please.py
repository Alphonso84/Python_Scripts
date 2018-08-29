import math
 
def split_check(total, number_of_people):
  return math.ceil(total / number_of_people)
 
try:
  total_due = float(input("What is the total in dollars? "))
  number_of_people = int(input("How many people? "))
except ZeroDivisionError:
  print("You've entered an invalid number of people. Try again...")
except ValueError:
  print("That is not a valid value. Try again...")
 
else:
  amount_due = split_check(total_due, number_of_people)
  print("each person owes ${}".format(amount_due))