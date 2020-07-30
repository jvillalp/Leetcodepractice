#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #carry will be one (remainder)
        carry = 0
        #create variables
        l3 = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = l3
        #while loop
        while p1 or p2:
            #sum of two linked list,setting it to zero if none
            sum = carry + (p1.val if p1 else 0) + (p2.val if p2 else 0)
            #carry can now be remaider if value is double diget
            carry = int(sum/10)
            #val of ListNode(0) is sum % 10
            p3.val = sum % 10
            #does checks 
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            #check if length of list is same, if not next node is listNode(0)
            if p1 or p2:
                p3.next = ListNode(0)
                p3 = p3.next

        if (carry > 0):
            p3.next = ListNode(carry)
            #add to next node if carry is more than 1
        return l3
