# Welcome message
print("Welcome what's to the tip calculator!")

# Get user inputs: total bill, tip %, and number of people
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15?'))
people = int(input('How many people to split the bill?'))

# Convert tip percentage to decimal
tip_as_percent = tip / 100

# Calculate total tip amount
total_tip_amount = bill * tip_as_percent

# Add tip to original bill
total_bill = bill + total_tip_amount

# Divide total by number of people
bill_per_person = total_bill / people

# Round to 2 decimal places for currency formatting
final_amount = round(bill_per_person, 2)

# Display final amount each person should pay
print(f'Each person should pay: ${final_amount}')