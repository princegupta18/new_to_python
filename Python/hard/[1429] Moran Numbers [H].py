"""
####  Moran Numbers  ####

A Harshad number is a number which is divisible by the sum of its digits. For example, 132 is divisible by 6 (1+3+2).
A subset of the Harshad numbers are the Moran numbers. Moran numbers yield a prime when divided by the sum of their digits. For example, 133 divided by 7 (1+3+3) yields 19, a prime.
Create a function that takes a number and returns "M" if the number is a Moran number, "H" if it is a (non-Moran) Harshad number, or "Neither".


[Examples]

___
moran(132) ➞ "H"

moran(133) ➞ "M"

moran(134) ➞ "Neither"
_____



[Notes]

N/A


[algebra] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Moran Numbers
http://www.numbersaplenty.com/set/Moran_number/
A number n is a Moran number if n divided by the sum of its digits gives a prime number.
_________
_________
Harshad Numbers
http://www.numbersaplenty.com/set/Harshad_number/
A number n is a Harshad (also called Niven) number if it is divisible by the sum of its digits.
_________
_________
Python Program to Print All Prime Numbers in an Interval
https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval/
The idea to solve this problem is to iterate the val from start to end using a for loop and for every number, if it is greater than 1, check if it divides n. If we find …
_________

"""
#Your code should go here:

