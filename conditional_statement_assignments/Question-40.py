    '''
    check is password is valid or not
    '''password = input("Enter password: ")

    if len(password) >= 8:
        if any(ch.isdigit() for ch in password)
        print("Valid password")
    else:
        print("password must contain a digit")
    else:
        print("password must contain at least 8 characters")