#Eli Coughlin 
# 9-22-2026
# P2LAB2
# I'm writing a program that creates a dictionary where the key and value pairs are as follows. 

vehicles = {"Camaro": 18, "Prius": 52, "Silverado": 22, "Mustang": 24 } 

# Store all the keys in a variable
keys = vehicles.keys()  

# Print the keys
print(keys)  

# Ask the user to choose a vehicle 
vehicle = input("Enter a vehicle from the list above: ") 

mpg = vehicles[vehicle] 

#Display the MPG
print(f"The MPG for {vehicle} is {mpg}.") 

#Ask for miles
miles = float(input("How many miles will you drive? "))

#Calculate the gallons needed
gallons_needed = miles / mpg 

print(f"You will need {gallons_needed:.2f} gallons of gas.")