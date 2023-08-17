"""
####  Counting Nespers  ####

A permutation of a list is a way to reorder its entries. For instance, [1, 2, 3] has permutations:
___
[1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 1, 2] [3, 2, 1]
_____

This challenge is about nested permutations (nespers, for short) which are the same idea as permutations, but now for nested lists.
For example, the nespers of [1, [2, 3]] are:
___
[1, [2, 3]] [1, [3, 2]] [[2, 3], 1] [[3, 2], 1]
_____

Note that, as the name indicates, nespers must preserve the nested list structure, so that [2, [1, 3]] is not a nesper of [1, [2, 3]] since 1 and 2 are in different nest levels.
Put another way, a nesper treats each list level as a set (i.e. order is allowed to change), but elements can't move between sets.
Write a function that, given a nested list, returns the number of nespers of that list.
To see how to find the number of nespers, let's work out a larger example. Recall that, if a list has n elements, there are n! = n*(n-1)*(n-2)*...*3*2*1 permutations.
As such, I claim that [[1, 7], 3, [2, 4, 5, 6]] has 3! * 2! * 4! nespers. Why? Because there are 3! permutations of the outer level, 2! permutations of the [1, 7] level, and 4! permutations of the [2, 4, 5, 6] level.


[Examples]

___
nespers([1, 2, 3]) ➞ 6

nespers([1, [2, 3]]) ➞ 4

nespers([[1, 7], 3, [2, 4, 5, 6]]) ➞ 288

nespers([1, [3, [2, [5, 4]]]]) ➞ 16
# Note that there are 4 nesting levels.
_____



[Notes]

___
*) The elements inside the nested list will always be distinct, to avoid questions about two nespers looking the same.
*) Some nesting levels may be empty. Recall that 0!=1.
___



[arrays] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
isinstance()
https://www.w3schools.com/python/ref_func_isinstance.asp
The isinstance() function returns True if the specified object is of the specified type, otherwise False. If the type parameter is a tuple, this function will return T …
_________

"""
#Your code should go here:

