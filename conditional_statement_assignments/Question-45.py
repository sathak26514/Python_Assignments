    '''
    menu based food selection
    '''
    print("1. pizza")
    print("2. burger")
    print("3. sandwich")
    print("4. pasta")

    choice choice:
        case 1:
            print("You selected pizza")
        case 2:
            print("You selected burger")
        case 3:
            print("You selected sandwich")
        case 4:
            print("You selected pasta")
        case _:
            print("Invalid choise")