#Eli Coughlin 
#10-20-2026 
#P4HW1
#This program collects tests scores, validates input, drops the lowest score, calculates the average, and displays the corresponding letter grade 

#Ask the user how many scores they want to enter 
num_scores = int(input("How many scores do you want to enter? ")) 

#Create an empty list to store the scores 
score_list = [] 

#Loop the number of times specified by the user 
for i in range(num_scores): 

    #Ask the user to enter a score 
    score = float(input(f"Enter score#{i + 1}: ")) 

    #Continue asking for a score while the score is invalid 
    while score < 0 or score > 100: 

        #Display an error message 
        print("\nInvalid score entered!!!!") 

        #Tell the user the valid range 
        print("Score should be between 0 and 100") 

        #Ask the user to enter a valid score 
        score = float(input(f"Enter score #{i + 1} again: ")) 

    #Add the valid score to the score list 
    score_list.append(score)

#Find the lowest score in the list 
lowest_score = min(score_list) 

#Create a copy of the original list 
modified_scores = score_list.copy() 

#Remove the lowest score from the copied list 
modified_scores.remove(lowest_score)

#Add all scores remaining in the modified list 
total = sum(modified_scores) 

#Divide the total by the number of remaining scores 
average = total / len(modified_scores) 

#Determine if the average earns an A 
if average >= 90: 
    letter_grade = "A" 

#Determine if the average earns a B 
elif average >= 80: 
    letter_grade = "B" 

#Determine if the average earns a C 
elif average >= 70: 
    letter_grade = "C" 

#Determine if the average earns a D 
elif average >= 60: 
    letter_grade = "D" 

#Any average below 60 earns an F 
else: 
    letter_grade = "F"  

#Display a heading for the results section 
print("\n------------Results-------------")

#Display the lowest score entered 
print(f"Lowest Score: {lowest_score}") 

#Display the list after dropping the lowest score 
print(f"Modified List: {modified_scores}") 

#Display the calculated average 
print(f"Scores Average: {average:.2f}") 

#Display the letter grade 
print(f"Grade: {letter_grade}")  

#Display a closing line 
print("----------------------------------")


