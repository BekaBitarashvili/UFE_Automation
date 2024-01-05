import random
import string

pass_length = int(input("Enter password length: "))
pass_lower = input("lower case? (y/n): ")
pass_upper = input("upper case? (y/n): ")
pass_digit = input("digit? (y/n): ")

# lower_alp with ascii
lower_alp = string.ascii_lowercase
upper_alp = string.ascii_uppercase
digit = string.digits
pass_data = ""
for _ in range(pass_length):
    if pass_lower == "y" and len(pass_data) < pass_length:
        pass_data += random.choice(lower_alp)
    if pass_upper == "y" and len(pass_data) < pass_length:
        pass_data += random.choice(upper_alp)
    if pass_digit == "y" and len(pass_data) < pass_length:
        pass_data += random.choice(digit)
print(pass_data)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(a))