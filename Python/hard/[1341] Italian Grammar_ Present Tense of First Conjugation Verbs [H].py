"""
####  Italian Grammar: Present Tense of First Conjugation Verbs  ####

In this challenge, you must build a function that inflects an infinitive regular Italian verb of the first conjugation form to the present tense, including the personal subjective pronoun.
All first conjugation Italian verbs share the same suffix: ARE. The first thing to do is separate the verb root from the suffix.
___
*) Root of "programmare" (to code) = "programm".
*) Root of "giocare" (to play) = "gioc".
___

For each subjective pronoun the root is combined with a new suffix: see table below (pronouns are numbered for coding ease, in real grammar they are grouped in singular and plural, both from first to third):

___
*) Present tense of verb "parlare" (to speak) for third pronoun:
Pronoun ("Egli") + Root ("parl") + Suffix ("a") = "Egli parla".
*) Present tense of verb "lavorare" (to work) for fourth pronoun:
Pronoun ("Noi") + Root ("lavor") + Suffix ("iamo") = "Noi lavoriamo".
___

There are two exceptions for present tense inflection:
___
*) If root ends with "c" or "g" the second and fourth pronoun suffixes add a "h" at the start:
"Attaccare" (to attack) = "Tu attacchi" (instead of "Tu attacci")
"Legare" (to tie) = "Noi leghiamo" (instead of "Noi legiamo")
*) If root ends with "i" the second and fourth pronoun suffixes lose the starting "i" (so that second pronoun suffix disappears):
"Inviare" (to send) = "Noi inviamo" (instead of "Noi inviiamo")
"Tagliare" (to cut) = "Tu tagli" (instead of "Tu taglii")
"Mangiare" (to eat) = "Noi mangiamo" (instead of "Noi mangiiamo")
"Cacciare" (to hunt) = "Tu cacci" (instead of "Tu caccii")
___

Given a string verb being the infinitive form of the first conjugation Italian regular verb, and an integer pronoun being the subjective personal pronoun, implement a function that returns the inflected form as a string.


[Examples]

___
conjugate("programmare", 5) ➞ "Voi programmate"

conjugate("iniziare", 2) ➞ "Tu inizi"

conjugate("mancare", 4) ➞ "Noi manchiamo"
_____



[Notes]

___
*) In the returned string, pronouns must be capitalized and verbs must be in lowercase, separated by a space between them.
*) Curious fact: first conjugation (verbs ending in "are") is also called "the living conjugation", because every new verb that enters the Italian dictionary is assigned to this category as a new regular verb; it often happens for verbs "borrowed" from English and for informatical neologisms: chattare, twittare, postare, spammare... will edabittare be the next?
___



[conditions] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Find and Replace Last Occurrence of a Character in String
https://sarathlal.com/replace-last-occurrence-of-character-in-string-python/
Some code that you might find helpful! :)
_________
_________
How to get Last N characters in a string?
https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/
In python, a String is a sequence of characters, and each character in it has an index number associated with it. For example, we have a string variable sample_str that …
_________

"""
#Your code should go here:

