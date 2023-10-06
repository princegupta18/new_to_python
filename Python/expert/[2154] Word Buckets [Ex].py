"""
####  Word Buckets  ####

Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters. Only include full words inside each bucket.


[Examples]

___
split_into_buckets("she sells sea shells by the sea", 10)
➞ ["she sells", "sea shells", "by the sea"]

split_into_buckets("the mouse jumped over the cheese", 7)
➞ ["the", "mouse", "jumped", "over", "the", "cheese"]

split_into_buckets("fairy dust coated the air", 20)
➞ ["fairy dust coated", "the air"]

split_into_buckets("a b c d e", 2)
➞ ["a", "b", "c", "d", "e"]
_____



[Notes]

___
*) Spaces count as one character.
*) Trim beginning and end spaces for each word bucket (see final example).
*) If buckets are too small to hold a single word, return an empty list: []
*) The final goal isn't to return just the words with a length equal (or lower) to the given n, but to return the entire given phrase bucketized (if possible). So, for the specific case of "by" the only word with a proper length, the phrase can't be bucketized, and the returned list has to be empty.
___



[control_flow] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
String literals are surrounded by either single quotation marks, or double quotation marks.
_________

"""
#Your code should go here:

