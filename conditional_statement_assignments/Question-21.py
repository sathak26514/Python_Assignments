    '''
    smallest number in 3 number
    '''
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a <= b and a <= c:
        print("smallest:", a)
    elif b <= a and b <= c:
        print("smallest:", b)
    else:
        print("smallest:", c)