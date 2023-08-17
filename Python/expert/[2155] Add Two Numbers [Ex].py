"""
####  Add Two Numbers  ####

The function input is two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list, in which the digits are also stored in reversed order. The class ListNode, building block of the linked list, is defined in the Tests tab.


[Class definition]

___
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
_____



[Examples]

___
lt1 = ListNode(2)
lt1.add_data([4, 3])
lt2 = ListNode(5)
lt2.add_data([6, 4])
# print(lt1.get_data())    # [2, 4, 3]
# print(lt2.get_data())    # [5, 6, 4]
# print(342 + 465)         # 807
add_two_numbers(lt1, lt2).get_data() ➞ [7, 0, 8]
_____

___
lt1 = ListNode(0)
lt2 = ListNode(0)
# print(lt1.get_data())    # [0]
# print(lt2.get_data())    # [0]
# print(0 + 0)             # 0
add_two_numbers(lt1, lt2).get_data() ➞ [0]
_____

___
lt1 = ListNode(9)
lt1.add_data([9,9,9,9,9,9])
lt2 = ListNode(9)
lt2.add_data([9,9,9])
# print(lt1.get_data())    # [9, 9, 9, 9, 9, 9, 9]
# print(lt2.get_data())    # [9, 9, 9, 9]
# print(9999999 + 9999)    # 10009998
add_two_numbers(lt1, lt2).get_data() ➞ [8, 9, 9, 9, 0, 0, 0, 1]
_____



[Notes]

___
*) The input linked lists can be of different lengths.
*) The returned reference has to point to the head of the new list.
___



[classes] [data_structures] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Create string from iterable.
_________
_________
Python Classes and Objects
https://www.w3schools.com/python/python_classes.asp
Python Classes and Objects
_________

"""
#Your code should go here:

