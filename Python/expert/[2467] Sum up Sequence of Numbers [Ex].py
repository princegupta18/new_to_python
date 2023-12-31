"""
####  Sum up Sequence of Numbers  ####

Write a function that computes the sum of k*sign(sin(k*k)) with begin_k <= k <= end_k. Python does not have a sign function but it's easy to implement the required logic: 1 if x > 0 else -1, ( sine of natural_num equal to zero only for n=0). Sum of consecutive numbers can be computed by the formula (n1 + n2) * (n2 – n1 + 1) / 2 when all numbers have the same sign.
The main point of this challenge is that it's hard to predict the sign of sin(k*k) for k. The sum of consecutive numbers between n1 and n2 with the specified sign can be positive or negative, large or small, as illustrated here:



[Examples]

___
sum_up(1, 101) ➞ 65

sum_up(200, 911) ➞ -456
_____



[Notes]

___
*) The function must be efficient because the intervals are large (be inventive).
*) For comparison, my solution takes 7 seconds to compute all tests, which is still under the server limit of 12 seconds.
___



[algorithms] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Multiprocessing
https://docs.python.org/3/library/multiprocessing.html
Is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effect …
_________

"""
#Your code should go here:

