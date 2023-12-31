"""
####  Recursion: Multiply By 11  ####

Given a positive number as a string, multiply the number by 11 and also return it as a string. However, there is a catch:
You are NOT ALLOWED to simply cast the numeric string into an integer!
Now, how is this challenge even possible? Despite this, there is still a way to solve it, and it involves thinking about how someone might multiply by 11 in their head. See the tips below for guidance.


[Examples]

___
multiply_by_11("11") ➞ "121"

multiply_by_11("111111111") ➞ "1222222221"

multiply_by_11("1213200020") ➞ "13345200220"

multiply_by_11("1217197941") ➞ "13389177351"

multiply_by_11("9473745364784876253253263723") ➞ "104211199012633638785785900953"
_____



[Tip]

There is a simple trick to multiplying any two-digit number by 11 in your head:

___
# 23 * 11
# Add together 2 and 3 to make 5
# Place 5 between the two digits to make 253
_____

___
# 77 * 11
# Add together 7 and 7 to make 14
# Place 4 between the two digits to make 747
# Carry the 1 to make 847
_____



[Notes]

___
*) See this resource to find out how this process can be utilized for numbers of any length.
*) This challenge was heavily inspired by Mubashir Hassan's challenge on adding two numbers together.
*) You are expected to solve this challenge recursively.
*) An iterative versioin of this challenge can be found via this link.
___



[logic] [math] [numbers] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Multiplying by Eleven
https://trachtenbergspeedmath.com/multiplication/basic-multiplication/multiplying-by-eleven/
Is amazingly simple when you know how. Multiply any number by eleven, in your head, using only simple addition.
_________
_________
Multiplication Function With Recursion
https://stackoverflow.com/questions/32668423/multiplication-function-with-recursion-in-python
Recursion means, you have to call the function itself. I need to write the function mult( n, m ) that should output the product of the two integers n and m. I am limite …
_________

"""
#Your code should go here:

