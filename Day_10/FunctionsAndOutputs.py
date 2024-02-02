#Functions with OP

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You did not enter you fname and lname"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result : {formated_f_name} {formated_l_name}"                                                      #in return funtion return formatted string
    #print("this is code")                                                                                      #After return statement print fun is not executed bcz computers tell that executer end of the code in return function
print(format_name (input("What is your first name?"),input("What is your last name?")))                       #print first letter of string is Capital and last is also Capital

