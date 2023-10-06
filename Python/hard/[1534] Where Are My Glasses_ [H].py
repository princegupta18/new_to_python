"""
####  Where Are My Glasses?  ####

Oh no! I've lost my glasses, but paradoxically, I need glasses to find my glasses!
Please help me out by showing me the index in the list which contains my glasses. They look like two capital Os, with any number of dashes in between!
___
*) This means that both O--O and O------------O are valid glasses, but not O----#--O for example!
*) Search thoroughly, maybe you'll find my glasses in places such as 'dustO-Odust'
___



[Examples]

___
find_glasses(["phone", "O-O", "coins", "keys"]) ➞ 1

find_glasses(["OO", "wallet", "O##O", "O----O"]) ➞ 3

find_glasses(["O--#--O", "dustO---Odust", "more dust"]) ➞ 1
_____



[Notes]

___
*) All lists will include one valid pair of glasses because I swear I dropped them around here somewhere ...
*) All elements in the list are strings.
___



[arrays] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________

"""
#Your code should go here:

