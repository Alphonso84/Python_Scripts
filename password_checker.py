import sys

password = input("Please enter a password:        ")
attempt_count = 1

while password != '12345':
    if attempt_count > 3:
        sys.exit("Too many Invalid Attempts")
    password = input("Invalid Password. Try Again:     ")
    attempt_count += 1
print("Password Correct!")
