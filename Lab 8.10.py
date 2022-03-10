# Linh Pham - ID# 2027194
# Lab 8.10
# This program will identify whether in string input is palindrome

user_input = input()
normal = ""
reserve = ""

for character in user_input.lower():
    if character != ' ':
        normal = normal + character
        reserve = character + reserve
if normal == reserve:
    print(user_input, 'is a palindrome')
else:
    print(user_input, 'is not a palindrome')
