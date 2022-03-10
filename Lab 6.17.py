# Lab 6.17
# Linh Pham - ID# 2027194
# This code demonstrate how to make simple password into stronger one by replacing some letter from user's password.

word = input()
password = ''

i = 0
while i < len(word):
    p = word[i]
    if p == 'i':
        password += '!'
    elif p == 'a':
        password += '@'
    elif p == 'm':
        password += 'M'
    elif p == 'B':
        password += '8'
    elif p == 'o':
        password += '.'
    else:
        password += p
    i += 1

password += "q*s"
print(password)
