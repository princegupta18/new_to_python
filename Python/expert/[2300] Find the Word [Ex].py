"""
####  Find the Word  ####

You are presented with a rectangular grid of capital letters. Within this grid a target word occurs a number of times. The word may be positioned horizontally left to right, right to left; vertically down to up or up to down and diagonally left to right downwards, right to left downwards, right to left upwards or left to right upwards.
Write a function which takes two parameters:

Your function should return a tuple (count, grid) where count is the total number of occurrences of the target word and the grid is the input grid with each occurrence of the target word in lower case.


[Examples]

___
count_word([
  ["I", "W", "I", "S", "H"],
  ["Z", "H", "S", "I", "W"],
  ["R", "S", "A", "D", "I"],
  ["Z", "I", "R", "E", "S"],
  ["J", "W", "K", "F", "H"]
], "WISH") ➞ (4, [
  ["I", "w", "i", "s", "h"],
  ["Z", "h", "s", "i", "w"],
  ["R", "s", "A", "D", "i"],
  ["Z", "i", "R", "E", "s"],
  ["J", "w", "K", "F", "h"]
 ])

count_word([
  ["M", "I", "W", "S", "W", "I", "I", "M"],
  ["W", "M", "I", "W", "W", "S", "M", "I"],
  ["I", "S", "S", "I", "M", "I", "S", "W"],
  ["S", "W", "I", "M", "W", "M", "W", "S"],
  ["I", "I", "W", "M", "I", "W", "I", "S"],
  ["I", "M", "I", "S", "M", "S", "M", "W"],
  ["W", "W", "S", "M", "W", "I", "S", "I"],
  ["S", "I", "M", "M", "I", "W", "S", "M"]
], "SWIM") ➞ (9, [
  ["m", "i", "w", "s", "W", "I", "I", "m"],
  ["W", "M", "I", "w", "W", "S", "M", "i"],
  ["I", "s", "S", "i", "M", "I", "s", "w"],
  ["s", "w", "i", "m", "W", "M", "w", "s"],
  ["I", "i", "W", "m", "I", "W", "i", "s"],
  ["I", "m", "i", "S", "M", "S", "m", "w"],
  ["W", "w", "S", "M", "W", "I", "S", "i"],
  ["s", "I", "M", "m", "i", "w", "s", "m"]
])
_____



[Notes]

Diagonals can be any diagonal the target word can fit in, not just the main diagonal. The target word will not be a palindrome.


[algorithms] [arrays] 



-------------------------------------------------------------------
[Resources]
_________
Happy Neuron
http://www.happy-neuron.com/
Publishes daily puzzles including this type of puzzle.
_________

"""
#Your code should go here:

