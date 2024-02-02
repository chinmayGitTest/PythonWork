target = int(input("Please Enter a Number :\n")) 
# even_sum=0
# for number in range(2,target+1,2):
#   even_sum += number
# print(f"Addition of even number is : {even_sum}")

#Second Method
alternate_sum = 0
for number in range(2,target+1):
  if number %2 == 0:
    alternate_sum += number
print(alternate_sum)

