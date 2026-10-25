'''
check if number is single digit or double digit or triple using if-else statements.
'''
 num = int(input("Enter a number: "))
 num = abs(num)

 if num <= 9:
    print("Single-digit number")
elif num<= 99:
    print("Double-digit number")
elif num <= 999:
    print("Three-digit number")
elif:
    print("More than three digits")
    