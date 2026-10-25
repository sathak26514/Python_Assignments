    '''
    grade description based on grade
    '''
    grade = input("Enter grade (A, B, C, F): ").upper()

    match grade
        case "A":
            print("Exellent")
        case "B":
            print("Very good")
        case "C":
            print("Good")
        case "F"
            print("Fail")
        case _:
            print("Invalid grade")