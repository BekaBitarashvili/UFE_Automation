# while True:
#     answer = input('Please enter your name: ')
#     if answer.isalpha():
#         print(answer)
#         break
#     else:
#         print('Please enter a string')
# import random
#
# pass_length = int(input("Enter password length: "))
# pass_lower = input("lower case? (y/n): ")
# pass_upper = input("upper case? (y/n): ")
# pass_digit = input("digit? (y/n): ")
#
# lower_alp = "abcdefghijklmnopqrstuvwxyz"
# upper_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# digit = "0123456789"
# pass_data = ""
# for _ in range(pass_length):
#     if pass_lower == "y" and len(pass_data) < pass_length:
#         pass_data += random.choice(lower_alp)
#     if pass_upper == "y" and len(pass_data) < pass_length:
#         pass_data += random.choice(upper_alp)
#     if pass_digit == "y" and len(pass_data) < pass_length:
#         pass_data += random.choice(digit)
#
# print(f'random pass is {pass_data}')

# for _ in range(10, -1, -1):
#     print(_)


# enumerate something
# for i, j in enumerate('hello'):
#     print(i, j)