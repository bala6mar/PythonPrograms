#This is the edited line of code
#This is the second line
year = int(input("Enter any year here: "))

"""if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap")
        else:
            print("Not a leap")
    else:
        print ("Leap")
else:
    print("Not a Leap")"""

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap")
else:
    print("Not a Leap")



