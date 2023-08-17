"""
####  Legal Backlog  ####

A courthouse has a backlog of several cases that need to be heard, and is trying to set up an efficient schedule to clear this backlog. You will be given the following inputs:
___
*) A dictionary cases whose values are the number of court sessions each case needs to be concluded.
*) An integer max_daily_sessions which gives the maximum number of court sessions that can be held each day.
___

Crucially, it is not possible to have two sessions of the same case in the same day.
Write a function that determines the minimum number of days needed to clear the backlog.


[Examples]

___
legalbacklog({"A":4, "B": 3, "C": 2}, 5) ➞ 4
# There are three cases "A", "B", "C" needing 4, 3, 2 sessions, respectively. 
# Moreover, up to five sessions can be held each day.
# A possible schedule is:
# day1 = ["A", "B", "C"], day2 = ["A", "B", "C"], day3 = ["A", "B"],
# day4 = ["A"]

legalbacklog({"A":4, "B": 3, "C": 2}, 3) ➞ 4
# Same cases as above, but now with up to three sessions each day
# Same schedule as above still words

legalbacklog({"A":4, "B": 3, "C": 2}, 1) ➞ 9
# Again same cases, but only one case per day,
# hence answer is the number of cases, i.e. 9 

legalbacklog({"A":4, "B": 3, "C": 2}, 2) ➞ 5
# Same cases, but at most two sessions per day.
# A possible schedule:
# day1 = ["A", "B"], day2 = ["A", "B"], day3 = ["A", "B"],
# day4 = ["A", "C"], day5 = ["C"]

legalbacklog({"A":4, "B": 4, "C": 4}, 2) ➞ 6
# Different case load, at most two sessions per day
# A possible schedule:
# day1 = ["A", "C"], day2 = ["A", "C"], day3 = ["A", "B"],
# day4 = ["A", "B"], day5 = ["C", "B"], day6 = ["C", "B"]
_____



[algorithms] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
_________

"""
#Your code should go here:

