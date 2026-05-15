# unit converter
weight = float(input("the given weight : "))
unit = input("is that unit is K or L : ")

if unit == "K":
    weight = weight * 2.208
    print(f"the wight is : {weight} lbs")
elif unit == "L":
    weight = weight / 2.208
    print(F"the weight is : {weight} kgs")
else:
    print(f"{unit} is not valid")