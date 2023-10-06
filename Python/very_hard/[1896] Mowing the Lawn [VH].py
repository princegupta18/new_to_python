"""
####  Mowing the Lawn  ####

Create a function that takes in an array of grass heights and a variable sequence of lawn mower cuts and outputs the array of successive grass heights.
If after a cut, any single element in the array reaches zero or negative, return "Done" instead of the array of new heights.
A demo:
___
cutting_grass([3, 4, 4, 4], 1, 1, 1) ➞ [[2, 3, 3, 3], [1, 2, 2, 2], "Done"]

# 1st cut shaves off 1: [3, 4, 4, 4] ➞ [2, 3, 3, 3]
# 2nd cut shaves off 1: [2, 3, 3, 3] ➞ [1, 2, 2, 2]
# 3rd cut shaves off 1: [1, 2, 2, 2]➞ [0, 1, 1, 1], but one element reached zero so we return "Done".
_____



[Examples]

___
cutting_grass([4, 4, 4, 4], 1, 1, 1, 1)
➞ [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], "Done"]

cutting_grass([5, 6, 7, 5], 1, 2, 1)
➞ [[4, 5, 6, 4], [2, 3, 4, 2], [1, 2, 3, 1]]

cutting_grass([8, 9, 9, 8, 8], 2, 3, 2, 1)
➞ [[6, 7, 7, 6, 6], [3, 4, 4, 3, 3], [1, 2, 2, 1, 1], "Done"]

cutting_grass([1, 0, 1, 1], 1, 1, 1) ➞ ["Done", "Done", "Done"]
_____



[Notes]

___
*) The number of lawn cuts is variable.
*) There will be at least one cut.
*) Return "Done" onwards for each additional cut if the grass has already been completely mowed (see fourth example).
___



[arrays] [higher_order_functions] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Python For Loops
https://www.w3schools.com/python/python_for_loops.asp
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
_________

"""
#Your code should go here:

