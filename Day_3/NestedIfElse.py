
print("Welcome to the JoyPark")
height=int(input("What is your height?"))

if height >= 120:
    print("You can ride rollercoaster")
    age=int(input("What is your age?"))
    if(age <=18):
        print("You can pay 7Rs/-")
    else:
        print("You can pay 20Rs/-")
else:
    print("You can not ride rollercoaster")