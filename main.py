# Write your solution below
# Follow the instructions in the tab to the right

# Use this exchange rate
NAIRA_PER_DOLLAR = 410.59  # exchange rate as of Nov 10 2021

#the code below prompts the user to input the USD value
user_value = float(input("Please enter the USD amount you want to convert: "))

#this code shows the conversion formular from USD to NGN
conversion_formular = NAIRA_PER_DOLLAR * user_value

#below assigns the fstring to the variable conversion_value
conversion_value = (f"{conversion_formular:.2f}")

print(f"{user_value} USD is {conversion_value} NGN")
