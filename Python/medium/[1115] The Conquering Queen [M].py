"""
####  The Conquering Queen  ####

In chess, queens can move any number of squares horizontally, vertically or diagonally.
Given the location of your queen and your opponents' queen, determine whether or not you're able to capture your opponent's queen. Your location and your opponents' location are the first and second elements of the list, respectively.


[Examples]

___
can_capture(["A1", "H8"]) ➞ True
# Your queen can move diagonally to capture opponents' piece.

can_capture(["A1", "C2"]) ➞ False
# Your queen cannot reach C2 from A1 (although a knight could).

can_capture(["G3", "E5"]) ➞ True
_____



[Notes]

Assume there are no blocking pieces.


[arrays] [control_flow] [games] [strings] 



-------------------------------------------------------------------
[Resources]
_________
abs() Method
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________
_________
Chess Notation: How to Read and Record a Game of Chess
http://www.chessstrategiesblog.com/chess-notation/
How can you record your own chess games for later study (or to show your greatness to future generations)? The answer is in chess notation. This article (part 1 of 3 pa …
_________
_________
translate() Method
https://www.geeksforgeeks.org/python-string-translate/
Returns a string that is modified string of givens string according to given translation mappings.
_________
_________
Check If a Queen Can Attack a Given Cell on Chessboard
https://www.geeksforgeeks.org/check-if-a-queen-can-attack-a-given-cell-on-chessboard/
Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine whether the queen can attack the opponent or not. Note that …
_________
_________
ord() Method
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing Unicode code point for the given Unicode character.
_________

"""
#Your code should go here:

