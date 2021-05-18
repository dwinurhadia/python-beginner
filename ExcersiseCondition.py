weight = input("Weight : ")
# print(weight)
unit = input("(L)bs or (K)g : ")
if unit.upper() == 'L':
    print("Your weight is", float(weight)/2.2046, "kilos")
elif unit.upper() == 'K':
    print("Your weight is", float(weight)*2.2046, "lbs")
else:
    print("Make sure your unit correct")