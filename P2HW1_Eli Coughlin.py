# Eli Coughlin
# 9-22-2026
# P2HW1
# Telling the user to select a destination and calculate the budget for the trip 

# Get user input 
budget = float(input("Enter Budget: ")) 

destination = input("Enter your destination: ") 

gas = float(input("How much will you spend on gas? "))  

hotel = float(input(" how much will you spend on a hotel? "))

food = float(input("How much will you spend on food? ")) 

# Calculate expenses and the remaining balance 
expenses = gas + hotel + food 
remaining_balance = budget - expenses 

#Dispay results 
print("\n-------Travel Expenses-------") 

print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}") 
print(f"{'Accomodation:':20}${hotel:.2f}")
print(f"{'Food:':20}${food:.2f}") 

print("-------------------------------") 

print(f"{'Remaining Balance:':20}${remaining_balance:.2f}")