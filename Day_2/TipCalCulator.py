print("Welcome to the Tip Calculator:")
bill=float(input("What was the total bill? Rs="))
vetortip=int(input("What percentage to you like tip? 5,10,12,15?"))
people=int(input("How many people splitt the bill?"))
#bill_with_tip=vetortip / 100 * bill + bill
#bill_with_tip=bill * (1 + vetortip / 100)
vetortip_percentage = vetortip / 100
total_vetortip_amout = bill * vetortip_percentage
total_bill = bill + total_vetortip_amout
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"final amount is {final_amount}") 