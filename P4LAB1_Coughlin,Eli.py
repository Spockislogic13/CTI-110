#Eli Coughlin 
#10-19-2026 
#P4LAB1 
#Use turtle and loops to draw a square a triangle 

# Import the turtle 

import turtle   

t = turtle.Turtle() 
t.forward(100) 


# Create the turtle window and drawing object  
win = turtle.Screen() 
pen = turtle.Turtle() 


# Set turtle options 
pen.pensize(5) 
pen.pencolor("purple")
pen.shape("arrow") 

# Code to draw the shapes 
for side in range(4): 
    pen.forward(100) 
    pen.left(90)  

# Move the turtle to the top of the square 
pen.penup()
pen.goto(0,100) 
pen.pendown()

# While loop that executes 3 times 
sides = 3 

while sides > 0: 
    pen.forward(100) 
    pen.left(120)
    sides = sides -1 


# Wait for the user to close window 
win.mainloop()
