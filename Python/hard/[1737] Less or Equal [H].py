"""
####  Less or Equal  ####

Mubashir needs your help in a simple task.
Given a list of integers lst and an integer k, find the lowest positive integer x so that exactly k elements of the given list are less than or equal to x. Return None if the condition does not match.
See below examples for a better understanding:


[Examples]

___
less_or_equal([3, 7, 6, 1, 10, 3, 20], 4) ➞ 6
# 1, 3, 3, 6 = 4 elements
# All elements are less than or equal to 6

less_or_equal([3, 7, 6, 1, 10, 3, 20], 2) ➞ None
# 1, 3 = 2 elements
# Not possible to return 3 because we have another 3 in the list

less_or_equal([3, 7, 5, 1, 10, 3, 20], 4) ➞ 5
# 1, 3, 3, 5 = 4 elements
# All elements are less than or equal to 5

less_or_equal([10, 15, 20, 25], 0) ➞ 1
# k = 0
_____



[Notes]

___
*) All numbers of the given list and k will be ≥ 0.
*) Understanding the description of this challenge is the hardest part.
___



[interview] [logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Function
https://www.w3schools.com/python/ref_func_sorted.asp
Returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numeric …
_________
_________
len() Function
https://www.w3schools.com/python/ref_func_len.asp#:~:text=The%20len()%20function%20returns,of%20characters%20in%20the%20string.
Return the number of items in a list.
_________

"""
#Your code should go here:

