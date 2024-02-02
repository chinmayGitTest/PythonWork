import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l",
           "m","n","o","p","q","s","t","u","v","w","x",
           "y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbollas = ["!","@","#","$","%","^","&","*","(",")"]

print("Welcome to the Password Generator !!!")
nr_leters = int(input("How many letters would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbolls = int(input("How many symbolls would you like?\n"))

#Easy Level means suppose user have enter 3 letters,2 symbolls and 1 number then get password user (axu#^9)

# password =""
# for char in range(1,nr_leters+1):
#     password += random.choice(letters)

# for char in range(1,nr_numbers+1):
#     password += random.choice(numbers)


# for char in range(1,nr_symbolls+1):
#     password += random.choice(symbollas)

# print(f"your generated password = {password}")


#Hard Level


password_list =[]
for char in range(1,nr_leters+1):
    password_list.append(random.choice(letters))

for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)


for char in range(1,nr_symbolls+1):
    password_list += random.choice(symbollas)

print(password_list)
random.shuffle(password_list)                      #shuffle function used raarange the order 
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"your generated password = {password}")