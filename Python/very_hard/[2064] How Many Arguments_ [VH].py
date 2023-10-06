"""
####  How Many Arguments?  ####

Create a function that takes a function func and counts its arguments. Examining a function's bytecode using __code__ is disabled.


[Examples]

___
num_args(lambda: "") ➞ 0

num_args(lambda x: "") ➞ 1

num_args(lambda x, y: "") ➞ 2
_____



[Notes]

___
*) All random test function expressions will be constructed using +, -, *, and /.
*) None of the parameters of func will have default values.
*) All functions will be converted to a custom class object to avoid use of __code__.
*) If disabling __code__ or removing function functionality is too harsh, feel free to leave a comment.
___



[closures] [functional_programming] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
Handling Exceptions
https://docs.python.org/3/tutorial/errors.html#handling-exceptions
It is possible to write programs that handle selected exceptions. A try statement may have more than one except clause, to specify handlers for different exceptions. At …
_________
_________
eval
https://docs.python.org/3/library/functions.html#eval
The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.
_________

"""
#Your code should go here:

