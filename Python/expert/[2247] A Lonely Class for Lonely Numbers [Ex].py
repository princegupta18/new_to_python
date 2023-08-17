"""
####  A Lonely Class for Lonely Numbers  ####

In this challenge, write a funcion loneliest_number to find the last Lonely number inside a sequence. A number is Lonely if the distance from its closest Prime sets a new record of the sequence.
___
Sequence = from 0 to 3

# Any number lower than 3 doesn't have a Prime preceeding it...
# ...so that you'll consider only its next closest Prime.

0 has distance 2 from its closest Prime (2)
# It's a new record! 0 It's the first lonely number of the sequence
1 has distance 1 from its closest Prime (2)
2 has distance 1 from 3
3 has distance 1 from 2

# The sequence 0 to 3  has only one Lonely number: 0
_____

___
Sequence = Numbers from 5 to 10

5 has distance 2 from its closest Prime (3 or 7)
# It's a new record! 5 It's the first lonely number of the sequence
6 has distance 1 from 5 or 7
7 has distance 2 from 5
8 has distance 1 from 7
9 has distance 2 from 7 or 11
10 has distance 1 from 11

# The sequence 5 to 10  has only one Lonely number: 5
_____

___
Sequence = Numbers from 19 to 24

19 has distance 2 from its closest Prime (17)
# It's a new record! 19 It's the first lonely number of the sequence
20 has distance 1 from 19
21 has distance 2 from 5
22 has distance 1 from 23
23 has distance 4 from 19
# It's a new record! 23 is the second lonely number of the sequence
24 has distance 1 from 23

# The sequence 19 to 24  has two Lonely numbers: 19 and 23
_____

The function loneliest_number must accept two integers lo and hi being the inclusive bounds of the sequence to analyze, and returns a dictionay (dict) object with the following keys and values:
___
*) number: is the last Lonely number found in the given sequence;
*) distance: is the distance of the number from its closest Prime;
*) closest: is the Prime closest to number (if two Primes are equally distant from number, return the higher Prime).
___



[Examples]

___
loneliest_number(0, 22) ➞ {
  number: 0, distance: 2, closest: 2
}

loneliest_number(8, 123) ➞ {
  number: 53, distance: 6, closest: 59
}

loneliest_number(938, 1190) ➞ {
  number: 1140, distance: 11, closest: 1151
}

loneliest_number(120, 1190) ➞ {
  number: 211, distance: 12, closest: 223
}
_____



[Notes]

___
*) The numbers 0, 1 and 2 have no previous Prime to check, so that you'll consider only the next Prime to set the distance, as in Example #1.
*) Remember that you are searching for the closest Prime when establishing if the distance is a record: 7 has a distance equal to 2 because its closest Prime is 5.
*) If a Lonely number is equally distant from two Primes, you have to return the higher Prime, as in Example #2 (53 has distance 6 from either 47 and 59).
*) The first Lonely number of a sequence is (trivially) always equal to the sequence lower bound.
*) You can expect valid non-negative integers as input, without exceptions to handle.
___



[classes] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

