"""
####  Poker Hands  ####

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

The cards are valued in the order:
___
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
_____

If two players have the same ranked hands then the rank made up of the highest value wins. For example, a pair of eights beats a pair of fives (see example #1). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example #4). If the highest cards tie then the next highest cards are compared, and so on.
Consider the following five hands dealt to two players:

Create a function which takes list of random hands dealt to two players. Each string contains ten cards (separated by a single space). The first five are Player 1's cards and the last five are Player 2's cards. The function should return the number of hands Player 1 won.


[Examples]

___
player1_wins([
  "8C TS KC 9H 4S 7D 2S 5D 3S AC",
  "5C AD 5D AC 9C 7C 5H 8D TD KS",
  "3H 7H 6S KC JS QH TD JC 2D 8S",
  "TH 8H 5C QS TC 9H 4D JC KS JS",
  "7C 5H KC QH JD AS KH 4C AD 4S"
]) ➞ 2

player1_wins([
  "5H QS 8S 6D 3C 8C JD AS 7H 7D",
  "6H TD 9D AS JH 6C QC 9S KD JC",
  "AH 8S QS 4D TH AC TS 3C 3D 5C",
  "5S 4D JS 3D 8H 6C TS 3S AD 8C",
  "6D 7C 5D 5H 3S 5C JC 2H 5S 3D",
  "5H 6H 2S KS 3D 5D JD 7H JS 8H",
  "KH 4H AS JS QS QC TC 6D 7C KS",
  "3D QS TS 2H JS 4D AS 9S JC KD",
  "QD 5H 4D 5D KH 7H 3D JS KD 4H"
]) ➞ 3

player1_wins([
  "5S 9C KH KD 9H 5C TS 3D 7D 2D",
  "5H AS TC 4D 8C 2C TS 9D 3H 8D"
]) ➞ 2
_____



[Notes]

___
*) Assume all hands are valid (no invalid characters or repeated cards).
*) Each player's hand is in no specific order.
*) In each hand there is a clear winner.
*) Ten is given as T instead of 10.
___



[arrays] [games] [logic] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

