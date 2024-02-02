#DataStru and lists

states_in_india=["Maharashtra","kerla","Jammu","Uttarakhand","UP","Bihar","Gujrat"]    #lists of data can store in an order like 0,1,2...
#print(states_in_india[0])               #+ve index show first of data in array measn show top of the data
#print(states_in_india[-1])              #-ve index show last in data in array

#states_in_india[2] = "Jammu & Kashimr"  #suppose you missing or change the item list then it method used
#states_in_india.append("Karnataka")     #add another one item in list then used .append funtion
#states_in_india.extend(["Delhi","channai"])     #add list of item using .extend function
#print(states_in_india)
#print(len(states_in_india))               #it state that in array how many items is present
num_of_states = len(states_in_india)
print(states_in_india[num_of_states - 1])   