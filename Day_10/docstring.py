
def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        """This is the docstring """
        return "You did not enter you fname and lname"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result : {formated_f_name} {formated_l_name}"                                                      #in return funtion return formatted string
    #print("this is code") 
    
format_name()                                                                                     #After return statement print fun is not executed bcz computers tell that executer end of the code in return function