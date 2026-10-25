    '''
    traffic signal
    '''
    signal = input("Enter traffic signal color: ")

    match signal:
        case "red":
            print("stop")
        case "yellow":
            print("wait")
        case "green":
            print("go")
        case_:
            print("Invalid signal")
            