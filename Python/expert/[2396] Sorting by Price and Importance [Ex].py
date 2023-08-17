"""
####  Sorting by Price and Importance  ####

Create a function that returns a list of the most important items purchasable with a given budget. You will be given a dictionary dct containing items and their respective price and importance, and you will also be given a budget b to restrict the number of items you can buy. The importance can only be from 1-10, whereas the price and budget can be anything.


[Example]

___
price_importance_sort({
  "apples": { "price": 5, "importance": 3 },
  "oranges": { "price": 3, "importance": 2},
  "pears": { "price": 2,  "importance": 2}
}, 5) ➞ ["oranges", "pears"]
_____

The oranges and pears can be purchased at budget with a total importance of 4. Apples and oranges or pears are not able to be purchased due to the budget and apples themselves only have an importance value of 3, making the oranges/pears group preferable.


[Notes]

___
*) More importance is better, not worse (it isn't a 1st/2nd/3rd ranking).
*) The whole budget may be used.
*) In the case of a tie, use the cheaper/more important of the two.
*) Order the final list alphabetically.
___



[arrays] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Permutations and Combinations
https://www.geeksforgeeks.org/permutation-and-combination-in-python/
This method can give you all possible combinations in a list. Ex: lst = [1, 2, 3] permutations: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
_________

"""
#Your code should go here:

