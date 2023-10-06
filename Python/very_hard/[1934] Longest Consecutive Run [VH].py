"""
####  Longest Consecutive Run  ####

A consecutive-run is a list of adjacent, consecutive integers. This list can be either increasing or decreasing. Create a function that takes a list of numbers and returns the length of the longest consecutive-run.
To illustrate:
___
longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
_____



[Examples]

___
longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
# Longest consecutive-run: [1, 2, 3].

longest_run([5, 4, 2, 1]) ➞ 2
# Longest consecutive-run: [5, 4] and [2, 1].

longest_run([3, 5, 7, 10, 15]) ➞ 1
# No consecutive runs, so we return 1.
_____



[Notes]

If there aren't any consecutive runs (there is a gap between each integer), return 1.


[arrays] [control_flow] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Python's most efficient way to choose longest string in list?
https://stackoverflow.com/questions/873327/pythons-most-efficient-way-to-choose-longest-string-in-list
I have a list of variable length and am trying to find a way to test if the list item currently being evaluated is the longest string contained in the list. And I am us …
_________
_________
Python splitting list based on missing numbers in a sequence
https://stackoverflow.com/questions/3149440/python-splitting-list-based-on-missing-numbers-in-a-sequence
I am looking for the most pythonic way of splitting a list of numbers into smaller lists based on a number missing in the sequence. For example, if the initial list was …
_________

"""
#Your code should go here:

