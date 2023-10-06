"""
####  Happy Numbers  ####

You are given a list of 0s and 1s, like the one below:
___
[0, 1, 0, 0, 0, 1, 1, 1, 0, 1]

# The first element, a 0, and the last element, a 1 are both unhappy.
# The second element, a 1 is unhappy.
# The second-to-last element, a 0 is unhappy.
# All other numbers in this list are happy.
_____

A 1 is unhappy if the digit to its left and the digit to its right are both 0s. A 0 is unhappy if the digit to its left and the digit to its right are both 1s. If a number has only one neighbor, it is unhappy if its only neighbor is different. Otherwise, a number is happy.
Write a function that takes in a list of 0s and 1s and outputs the portion of numbers which are happy. The total portion of numbers which are happy can be represented as:
___
portion of happy numbers = (happy 0s + happy 1s) / total numbers
_____

In the example above, 0.6 is the number of happy numbers.


[Examples]

___
portion_happy([0, 1, 0, 1, 0]) ➞ 0

portion_happy([0, 1, 1, 0]) ➞ 0.5

portion_happy([0, 0, 0, 1, 1]) ➞ 1

portion_happy([1, 0, 0, 1, 1]) ➞ 0.8
_____



[Notes]

___
*) Remember: a 0 border number is unhappy if its only neighbor is a 1 and vice versa.
*) A list will contain at least two elements.
___



[arrays] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python range() function explained with examples
https://pynative.com/python-range-function/
Python range() function explained with examples
_________
_________
Python sum()
https://www.programiz.com/python-programming/methods/built-in/sum
Python sum()
_________
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Using the Python zip() Function for Parallel Iteration
_________
_________
Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types
_________

"""
#Your code should go here:

