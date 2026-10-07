#Eli Coughlin 
#10-5-2026 
#PHW2 
# Inputting employee name, hours, and payment 

# request employee info 
name = input("Enter employee name: ") 
hours = float(input("Enter number of hours worked: ")) 
rate = float(input("Enter the hourly pay rate: ")) 

#Evaluate overtime 
if hours > 40: 
    #Caculate overtime 
    overtime_hours = hours - 40 
    #Caculate over pay 
    overtime_pay = overtime_hours * (rate * 1.5) 
    #Calculate salary for regular hours 
    regular_pay = 40 * rate 
    #Caculate Gross pay 
    gross_pay = regular_pay + overtime_pay 
else:
    overtime_pay = 0 
    overtime_hours = 0  
    regular_pay = hours * rate
    gross_pay = regular_pay


#Display results 
print("---------------------------------") 
print("Employee name:", name) 
print(f'{"Hours worked":<15}{"Pay Rate":<12}{"Overtime Pay":<12}{"Regular pay":<15}{"Gross Pay":<12}') 
print("-------------------------------") 
print(f'{hours:<15f}{rate:<12f}{overtime_pay:<12f}{regular_pay:<15f}{gross_pay:<12f}')