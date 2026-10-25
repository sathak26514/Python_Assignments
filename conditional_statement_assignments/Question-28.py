'''
Discount based on purchase amount using if-else satements.
'''
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount>= 2000:
    discount = amount * 0.10
else:
    discount = 0

    print("Discount: ₹", Discount)
    print("Final amount: ₹",amount - discount)
    