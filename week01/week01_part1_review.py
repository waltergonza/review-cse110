#This is gonna be a review of the topics I learnt when I took this clase. 

#Its a good practice and efficient to open the folder where the file is instead of just the file to avoid problems or 
# misunderstandingnwhen trying to run your code. 

#Strings: It means it is  text

# Variables: Store information like putting things in a box.  - Just need a descriptive name and value 
# String is a colection of characters - Numbers: when using numbers we do not pur the quotation around it because it automatically 
# becomes into a string no matter if we are using numbers. 



print ("Hello Word")

print ("Welcome to CSE 110!")

print ("This is going to be a great course")

name = "Bob"
age = 24

print (name)
print (age)

# We can change what is store in a variable like the following:
age = 34

print (age)

# Code runs sequentially from the top to the botton. (It didn't change what we print before but it will print the new value as shown)


# Because we put the f the programm will look for the curly brases - once it runs it will display the "fstring"
# It helps because we can add text before the display and also we can display the variables the way we want them to display. 
print (f"Your name is {name}")
print (f"Your age is {age}")

# INPUT FUNCTION
# is a built in function like print. - when calling a function you type the name of the function and then put parentheses after it.
# Input always returns or gives you back a string

place = "Guatemala"

print (f"You are from {place}")

place = input("Where are you from? ")
print (f"You are from {place}")

vacation_place = input("Where do you want to go on vacation? ")
print (f"You want to go to {vacation_place}")


# ACTIVITY: 
#Instructions
# Write a program that asks a user for their favorite color, then allow them to type in their color. Finally, have the program
#  respond to them by displaying the text "Your favorite color is" followed by the color they typed.

favorite_color = input("Please type your favorite color: ")
print (f"Your favorite color is {favorite_color}")