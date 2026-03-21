bill= input("What is the total? ")
tip = input("What percentage tip would you like to give? ")
bill = float(bill)
tip = float(tip)
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
print(f"your total bill is: ${total_bill:.2f}")