'''
student exam eligibility
'''
attendence = float(input("Enter attendence percentage:"))
marks = int(input("Enter marks: "))

if attendence >- 75:
    if marks >= 40:
        print("eligible for exam")
    else:
        print("Not eligible: insufficient marks")
else:
    print("Not eligible: low attendence")
    