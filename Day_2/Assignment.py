street_name = "Abbey Road"
print(street_name[4] + street_name[7])

#input 39 = output 3+9=12
two_digit_number=input(39)
fir_number=int(two_digit_number[0])
sec_number=int(two_digit_number[1])
two_digit_number=fir_number+sec_number
print(two_digit_number)

#BMI Calculator
height = input()
weight = input()
weight_as_int=int(weight)
height_as_float=float(height)
bmi=weight_as_int / (height_as_float * height_as_float)
bmi_as_int=int(bmi)
print(bmi_as_int)