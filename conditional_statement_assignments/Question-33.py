    '''
    check weather a person can apply for loan
    '''
    age = int(input("Enter age: "))
    salary = float(input("Enter monthly slary: "))

    if age >= 25000:
        if salary >= 25000:
            print("Eligible to apply for a loan")
            else:
                print("Not eligible: salary to low")
    else:
        print("Not eligible: age requirement not met")
        