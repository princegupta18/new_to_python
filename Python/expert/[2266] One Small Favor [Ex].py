"""
####  One Small Favor  ####

My friend required some help with an assignment in school and I thought this would be a nice addition to be added as a challenge here as well.
Create a function that takes a sentence and returns a modified sentence abided by these rules:
___
*) If you encounter a date within the sentence, in the format DD/MM/YY or DD.MM.YY, you have to change it over to DD/MM/YYYY or DD.MM.YYYY (same separator char).
*) If you encounter a date within the sentence, in the format MonthName, DD. YY. you have to change it over to MonthName, DD. YYYY.
*) If you encounter an invalid MonthName then leave it as is.
*) For this challenge there is an arbitrary rule that if YY is less than 25 the year-prefix will be 20, otherwise, the year-prefix will be 19.
*) Meaning 08/11/20 -> 08/11/2020 or 02/11/95 -> 02/11/1995
___



[Examples]

___
small_favor("I was born on 11/02/98")
➞ "I was born on 11/02/1998"

small_favor("I was born on 11/02/98 and what about you?")
➞ "I was born on 11/02/1998 and what about you?"

small_favor("I was born on 02.11.19")
➞ "I was born on 02.11.2019"

small_favor("I was born on February, 02. 98.")
➞ "I was born on February, 02. 1998."

small_favor("I was born on January, 01. 15. and today is October, 08. 20.")
➞ "I was born on January, 01. 2015. and today is October, 08. 2020."

small_favor("I was born on Fakemonthy, 01. 15. dont change invalid dates")
➞ "I was born on Fakemonthy, 01. 15. dont change invalid dates"
_____



[Notes]

Don't forget to apply the arbitrary year-prefix rule defined above.
___
*) DD/MM/YY -> DD/MM/YYYY
*) DD.MM.YY -> DD.MM.YYYY
*) Month, DD. YY. -> Month, DD. YYYY.
*) DD|MM|YY -> DD|MM|YY (invalid separator, means it remains unchanged)
___



[formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expressions
https://www.tutorialspoint.com/python3/python_reg_expressions.htm
Is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pat...
_________
_________
Lookahead and Lookbehind
https://www.rexegg.com/regex-lookarounds.html
Explains the fine details of Lookahead and Lookbehind, including zero-width matches, overlapping matches and atomicity.
_________

"""
#Your code should go here:

