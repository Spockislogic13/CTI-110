# Eli Coughlin
# 9-11-2026 
# P1HW2 
# Calculating expenses into a travel Budget 

# Ask the user to enter their bidget 
budget = float(input("Enter your budget: $")) 

# Ask user to enter travel destination 
destination = input("Enter your travel destination: ") 

# Ask user for expenses 
gas = float(input("Enter amount you will spend on gas: $")) 
accomodation = float(input("Enter the amount you will spend on accomodation: $")) 
food = float(input("Enter the amount you will spend on food: $")) 

# Add expenses 
total_expenses = gas + accomodation + food 
 
# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display the travel budget summary 
print("------ Travel Summary ------")  
# Display the destination
print("Destination:", destination)  
# Display the original budget
print("Budget: $", budget)  
#Display the total expenses 
print("Total Expenses: $", total_expenses) 
#Display the remaining budget
print("Remaining Budget: $", remaining_budget)
