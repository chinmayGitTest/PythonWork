
print("Welcome to the JoyPark")
height=int(input("What is your height?"))
bill = 0

if height >= 120:
    print("You can ride rollercoaster")
    age=int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket is 5Rs/-")
    elif age <=18:
        bill = 7
        print("Youth ticket is 7Rs/-")
    else:
        bill = 20
        print("Adult ticket is 20Rs/-")

    wants_photo=input("Do you want photos? Y or N")
    if wants_photo == "Y":
        bill +=3
    print(f"YOur final bill is RS{bill}")

else:
    print("You can not ride rollercoaster")