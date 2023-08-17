"""
####  Permutation as Disjoint Cycle Form  ####

Write a function which, given a permutation of [0, 1, ..., n-1] ( n>0) represented by a shuffled list, returns the permutation in disjoint cycle form as a set of tuples.
A permutation is a particular (re)ordering of a set of objects. For example, [1,3,0,4] is a permutation on the 4 objects [0,1,2,3]. In this problem, we represent permutations on n objects as lists containing the numbers in list(range(n)) == [0, ..., n-1].
A cycle or cyclic permutation is a particular kind of permutation whereby all elements are sent to one another in a cyclic fashion. In this problem, we represent cycles as tuples.
___
*) For example, the permutation [1,2,3,0] is a cyclic permutation of [0,1,2,3] because it can be made from [0,1,2,3] by applying the mapping {0:1, 1:2, 2:3, 3:0}, which maps elements in the cycle 0➞1➞2➞3➞0. We represent this cycle by the tuple (0,1,2,3), where each element gets sent to the one on the right, and the last is sent to the first.
*) The cycles (0,1,2,3), (1,2,3,0), (2,3,0,1) and (3,0,1,2) all represent the same cycle; namely 0➞1➞2➞3➞0 . We always choose the cycle to have the lowest element first: (0,1,2,3).
___

Finally, any permutation can be written in disjoint cycle form, or as an unordered set of cyclic permutations. Disjoint means none of the cycles have any elements in common. This form is unique up to the order of the cycles and up to the cycle representation.
___
*) The cyclic permutation [0,1,3,2,4,5] can be written as (2,3)—since 2 an 3 are swapped—and so the disjoint cycle form is {(2,3)}.
*) [1,0,3,2] is the mapping {0:1, 1:0, 2:3, 3:2} and has disjoint cycle form{(0, 1), (2, 3)} .
___

Your function takes a list (the permutation) and returns a set of tuples (the set of cyclic permutations).


[Examples]

___
disjoint_cycle_form([1, 0]) ➞ {(0, 1)}
# 0 and 1 are swapped, but lowest is listed first.

disjoint_cycle_form([0, 1, 2, 3]) ➞ set()
# Permutation is already in order.

disjoint_cycle_form([0, 1, 3, 2]) ➞ {(2, 3)}

disjoint_cycle_form([1, 0, 3, 2]) ➞ {(0, 1), (2, 3)}
# or {(2, 3), (0, 1)}; the cycle order in a set doesn't matter.

disjoint_cycle_form([1, 3, 0, 2]) ➞ {(0, 1, 3, 2)}
_____



[Notes]

Look up "disjoint cycle notation" or "cycle decomposition" for more information about permutations. This is the kind of thing you learn in a first course in Group Theory. Note that the given permutations will always have at least one element (the only such permutation is [0]), and a permutation of length n will always contain the elements of range(n) (that is, 0 to n-1 inclusive).


[algorithms] [data_structures] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Wolfram|Alpha Can Show Information About Permutations
https://www.wolframalpha.com/input/?i=permutation+%281%2C+2%2C+3%29%284%2C+5%29
W|A accepts permutations written as products of cycles, BUT WITH NUMBERS STARTING FROM ONE — not zero, as in this problem.
_________

"""
#Your code should go here:

