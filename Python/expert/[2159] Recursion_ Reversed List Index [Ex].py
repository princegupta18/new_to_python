"""
####  Recursion: Reversed List Index  ####

Write a recursive function that filters the items in a list (given as parameter arr) by positional parity (odd or even), given as parameter par, starting from the opposite end. Return a list of items on odd positions (... 5, 3, 1) or on even positions (... 6, 4, 2) and counting from the last item in the list.


[Examples]

___
get_items_at([2, 4, 6, 8, 10], "odd") ➞ [2, 6, 10]
// 2, 6 & 10 occupy the 5th, 3rd and 1st positions from right.
// Odd positions, hence the parity, and from the opposite.

get_items_at(["E", "D", "A", "B", "I", "T"], "even") ➞ ["E", "A", "I"]
// E, A and I occupy the 6th, 4th and 2nd positions from right.
// Even positions, hence the parity, and from the opposite.

get_items_at([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "even") ➞ [")", "*", ^", "$", "@"]

get_items_at(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "even") ➞ ["R", "I", "R", "R", "L"]
_____



[Notes]

___
*) IMPORTANT: You are advised to solve this challenge via a recursive approach, hence, the very purpose of this challenge. You can check the Resources tab about a few topics on recursion.
*) Lists are zero-indexed, so, index+1 = position or position-1 = index.
*) Items in the list may contain duplicates. See example #4.
*) The last item in the list is always the first item to start a positional count.
*) The sequence of the items in the resulting list should be retained (i.e. example #1 - 6 should come after 2 and before 10, example #2 - "A" should come after "E" and before "I").
*) An iterative version of this challenge can be found via this link.
___



[arrays] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively in Python
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Indexing and Slicing
https://realpython.com/lessons/indexing-and-slicing/
In this video, you’ll practice list indexing and slicing. The elements of a list can be accessed by an index. To do that, you name the list, and then inside of a pair o …
_________
_________
Python Indexing and Slicing for Lists and Other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python, one of the most in-demand machine learning languages, supports slice notation for any sequential data type like lists, strings, and others. Discover more about …
_________

"""
#Your code should go here:

