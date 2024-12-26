age = int(input("enter your age: "))
if age < 18:
    print("child")
elif age >= 18 and age < 35:
    print("youth")
elif age >= 35 and age< 60:
    print("citizen")
elif age >= 60:
    print("senior citizen")