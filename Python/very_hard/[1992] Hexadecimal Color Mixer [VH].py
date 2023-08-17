"""
####  Hexadecimal Color Mixer  ####

In this challenge, you have to mix two or more colors to get a brand new color from their average rgb values.
Each color will be represented in its hexadecimal notation, and so as a string starting with # containing three pairs of alphanumeric characters, equals to the three rgb values (in base 16) of red, green and blue.
To obtain the new color, you need to get the arithmetic average of the sums of the individual red, green and blue values of each given color. When the average is a float number, you have to round it to the nearest integer (rounding up for decimal parts equal to 0.5).
Mixing yellow and red:
___
Hexadecimal code of yellow = "#FFFF00"
Hexadecimal code of red = "#FF0000"

yellow to RGB = Red: ["FF" = 255], Green: ["FF" = 255], Blue: ["00", 0]
red to RGB = Red: ["FF" = 255], Green: ["00" = 0], Blue: ["00" = 0]

Average of Red values = (255 + 255) / 2 = 255
Average of Green values = (255 + 0) / 2 = 127.5 = 128
Average of Blue values = (0 + 0) / 2 = 0 = 0

Rgb of new color = [255, 128, 0]
Hexadecimal conversion = [255 = "FF"], [128 = "80"], [0 = "00"]

New color = "#FF8000" (orange)
_____

Given a list of strings colors containing a series of hexadecimal codes, implement a function that returns the hexadecimal code of the new color, as a new string.


[Examples]

___
hex_color_mixer(["#FFFF00", "#FF0000"]) ➞ "#FF8000"
# Orange

hex_color_mixer(["#FFFF00", "#0000FF"]) ➞ "#808080"
# Medium gray

hex_color_mixer(["#B60E73", "#0EAEB6"]) ➞ "#625E95"
# Lavender
_____



[Notes]

___
*) Remember to round to the nearest integer the average of the rgb values.
*) You can test the color codes in any hexadecimal-colors utility site, such as this one that I used for testing cases.
*) All the given hexadecimal strings are valid; there are no exceptions to handle.
*) If you're interested in rgb colors and their validation, you can give also try this challenge made by @Pustur.
___



[formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Web Colors
https://en.wikipedia.org/wiki/Web_colors
Are colors used in displaying web pages on the World Wide Web, and the methods for describing and specifying those colors. Colors may be specified as an RGB triplet or …
_________

"""
#Your code should go here:

