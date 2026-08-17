# STRING METHODS

#Converting email address to lowercase - This function is called a method
email = input("What is your email address? ")
print (email.lower())
# If we put another print or display like the following it will print the original text. It is important to reasing the value if I 
#  want to get the same result. 
print (email)

"""
Code	Result
words = "the GLORY of GOD is intelligence"

the GLORY of GOD is intelligence

words.capitalize()

The glory of god is intelligence

words.title()

The Glory Of God Is Intelligence

words.upper()

THE GLORY OF GOD IS INTELLIGENCE

words.lower()

the glory of god is intelligence

words.count("g")

1

words.lower().count("g")

3

Notice that words.count("g") resulted in a 1, because it did not count the two cases of capital "G" in the sentence. 
On the other hand, words.lower().count("g") resulted in a 3, because it first converted everything to lowercase, and then 
counted them, so when it counted the g's, the capital G's in that sentence were first converted to lowercase g's, and then 
they were counted.

Hint from Instructor
The examples in this table all say "words." but the name "words" is not special. In this case, it assumes that the string is 
stored in a variable named words but it could have been any variable name such as: first_name.title() or book_title.capitalize().

"""


#ACTIVITY

name = input("What is your first name? ")
last_name = input("What is your last name? ")
print (f"Your name is {last_name.title()}, {name.title()} {last_name.title()}.")