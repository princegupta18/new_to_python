"""
####  Matrix Movement  ####

Create a function which takes a parameter mat, where mat is a matrix (list of lists) such that all but one entry equals 0 (and the non-zero entry equals 1). The function, after being passed a matrix, should be repeatedly callable with the following str commands:
___
*) "up" ➞ Move the 1 to the cell above it.
*) "down" ➞ Move the 1 to the cell below it.
*) "left" ➞ Move the 1 to the cell to the left of it.
*) "right" ➞ Move the 1 to the cell to the right of it.
*) "stop" ➞ Return the resulting matrix.
___



[Examples]

___
one = [
  [1]
]

two = [
  [1, 0],
  [0, 0]
]

# Should work for 1×1 matrices
move(one)("up")("stop") ➞ [
  [1]
]

# The 1 should wrap around
move(two)("left")("stop") ➞ [
  [0, 1],
  [0, 0]
]

# Should accept multiple commands
move(two)("right")("down")("stop") ➞ [
  [0, 0],
  [0, 1]
]

# Should return a function
callable(move(two)) ➞ True
_____



[Notes]

___
*) The matrix can be of any size m×n, where m ≥ 1 and n ≥ 1.
*) The 1 should be able to wrap around, e.g. if the non-zero entry is at the top of the matrix, calling the command 'up' should move it to the bottom of the matrix.
*) The result of the original function move should be callable an arbitrary number of times.
___



[arrays] [closures] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Lambda Expressions
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used whe …
_________

"""
#Your code should go here:

