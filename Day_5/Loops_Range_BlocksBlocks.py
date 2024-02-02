#FoorLoop

fruits=["apple","peach","bear","grapes"]
for fruit in fruits:                        #in for loop fruit is variable and it assign to the fruits(loops is assig the code in multiple line)
    print(fruit)
    print(fruit + "Pie")
    #print(fruits)                           #in foor loop indentation is most imp bcz 
                                             #inside the foor loop all of fruits item printed in the loop 
#print(fruits)                                #in the outside of the foor loop they have printed out side of the loop print stat

#for loop with range
#for number in range(1,10):                     #range function is used to assign range bet 1 to 10 but not include 10.
for number in range(1,11,3):            #it means range 1 to 10 and steps count 3 and print next number 
    print(number)

#addition bet 1 to 100 numbers4
total=0
for number in range(1,101):
    total += number
print(f"total addition of number 1 to 100 is :{total}")