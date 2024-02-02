programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

#1.Retrieving items from dictionary.
#print(programming_dictionary["Bug"])

# #2.Adding new items to dictionar
programming_dictionary["loop"]="The action something over and over again"
print(programming_dictionary)

#3.creating an empty dictionary.
empty_dicitionar = {}

# #4.wipe an existing dictionar
# programming_dictionary = {}
# print(programming_dictionary)

#5.Edite an item in a dictionary
programming_dictionary["Bug"] = "A moth is your computer."
# print(programming_dictionary)

#6.Loop through a dictionary
# for thing in programming_dictionary:
    # print(thing)                        #print only keys
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) 