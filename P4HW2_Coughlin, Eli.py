#Eli Coughlin 
#10-5-2026 
#PHW2 
# Salary calculator with loops

# request employee info 
name = input("Enter employee name or 'Done' to finish: ") 

# Create Accumulator Variables for overtime pay, regular pay, gross pay, and employee count 

overtimepay_total = 0 
regularpay_total = 0
grosspay_total = 0
employee_count = 0 

while name != 'Done': 
    # Add employee count plus one 
    employee_count += 1 # employee_count = employee_count + 1 
    # Ask for employee info 
    hours = float(input("How many hours did " +name+ " work this week? ")) 
    rate = float(input("What is " +name+ "'s hourly pay rate? "))    
    
    #Evaluate overtime
    if hours > 40:  
     
     #Caculate overtime  
     overtime_hours = hours - 40  
     #Caculate overtime pay  
     overtime_pay = overtime_hours * (rate * 1.5)  
     #Calculate salary for regular hours   
     regular_pay = 40 * rate   
     #Caculate Gross pay   
     gross_pay = regular_pay + overtime_pay   
    else: 
       overtime_hours = 0  
       overtime_pay = 0   
       regular_pay = hours * rate 
       gross_pay = regular_pay 
    
    #Add to accumulator totals
    overtimepay_total += overtime_pay  
    regularpay_total += regular_pay  
    grosspay_total += gross_pay    
    
    print("---------------------------------")  
    print("Employee name:", name)   
    print(f'{"Hours worked":<15}{"Pay Rate":<12}{"Overtime Pay":<12}{"Regular pay":<15}{"Gross Pay":<12}')   
    print("-------------------------------")   
    print(f'{hours:<15f}{rate:<12f}{overtime_pay:<12f}{regular_pay:<15f}{gross_pay:<12f}')   
    
    name = input("Enter employee name or 'Done' to finish: ")  
    
print("Total number of employees entered: ")  
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))   
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))   
print("Total amount paid in gross: $", format(grosspay_total, ',.2f')) 
