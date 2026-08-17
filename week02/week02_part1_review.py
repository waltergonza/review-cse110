# Numeric Variables
# Integer or int: its a whole numbers but doesn't include decimal values

song1 = "213 seconds" #this is a string
song2 = 213 # this is a number (int)
song3 = 213.5 # this is a number (float)

song4 = 150
song5 = 250.25

playlist = song4 + song5 # we cannot use math with a string and a number. Must be only numbers or only strings.

print (f"The playlist is {playlist} seconds. ")

# Converting strings to numbers: 

song1 = 162 
song2 = 175
song3 = float(input("What is the length of the song? "))
# This is how we can convert a string to a number. We can actually mix ing (integers) and float numbers. 
# it always depend on what we are working if we will use int or float to convert the string. 

playlist = song1 + song2 + song3

print (f"The playlist is {playlist} seconds. ")

"""
Operator              	Symbol	 Example	Result

Add                       +       3 + 4       7

Subtract                  -       3 - 4      -1

Multiply                  *       3 * 4       12

Divide                    /       15 / 4      3.75

Divide and 
drop remainder           //      15 // 4      3


Remainder or Modulus
(Get the remainder that 
would result from         %      25 % 7        4
dividing the first 
number by the 
second one.)


Exponent
(To the power of)         **      3 ** 4       81

These operators follow standard mathematical orders of operation (where * happens before +), but you can force it to evaluate 
using parentheses. For example, (3 + 4) * 2 will perform the addition first, and then multiple the result by 2.

"""