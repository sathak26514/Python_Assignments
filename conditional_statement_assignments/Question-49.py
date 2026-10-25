    '''
    result status
    '''
    status = input("Enter result status (pass/fail): ").lower()

    match status:
        case "pass":
            print("Congratulstions! you passed.")
        case "fail"
            print("You failed. Try again.")
        case _:
        print("Invalid result status")