init = input("Enter your string or number here: ").lower()
final = init[::-1]
if init == final:
    print("Given is a Palindrome")
else:
    print("Given is not a Palindrome")

"""***************************************************************************************************"""

"""for i in init:
    final = i + final
if init == final:
    print ("Given string is Palindrome")
else:
    print("Given string is not a Palindrome")"""

"""*******************************************************************************************************"""

"""num = int(input("Enter your num here: "))
sum = 0
while num >=1:
    rem = num % 10
    sum = 10 * sum + rem
    num = num // 10
if num == sum:
    print("Given num is Palindrome")
else:
    print("Given num is not a Palindrome")"""
