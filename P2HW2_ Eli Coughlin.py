# ELi Coughlin 
# 9-23-2026  
# P2HW2  
# Taking six module grades and determining the lowest, highest, and average of the grades. 

# Input six module grades 

module1 = float(input("Enter the grade for module 1: ")) 
module2 = float(input("Enter the grade for module 2: ")) 
module3 = float(input("Enter the grade for module 3: ")) 
module4 = float(input("Enter the grade for module 4: ")) 
module5 = float(input("Enter the grade for module 5: ")) 
module6 = float(input("Enter the grade for module 5: ")) 

module_grades = [module1,module2,module3,module4,module5,module6]

# Find the lowest of the grades 
lowest_grade = min(module_grades) 

# Find the highest of the grades 
highest_grade = max(module_grades) 

# Find the total of the grades 
total_grades = sum(module_grades) 

# Find the lowest of the grades 
average_grade = total_grades/ len(module_grades) 

# Display the results
print("\n--------Results-----------") 
print(f"{'Lowest Grade:':20}{lowest_grade}") 
print(f"{'Highest Grade:':20}{highest_grade}") 
print(f"{'Sum of Grades:':20}{total_grades}") 
print(f"{'Average:':20}{average_grade:.2f}") 
print("---------------------------------")
