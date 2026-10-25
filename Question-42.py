    '''
    calculator operations
    '''
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
     match op:
        case "+":
            print("Result:, a + b")
        case "-":
            print("Result:", a - b)
        case "/":
            if b != 0:
                    print("Cannot divide by zero")
        case_:
        print("Invalid operator")