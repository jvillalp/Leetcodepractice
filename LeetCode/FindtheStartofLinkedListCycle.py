
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #basially you want to see if a pointer is pointing to something      more than           
        #once and you want to check to see. if it is, there is a cycle
        # create set
        nodes_set = set()
        #while loop
        while head :
            #if head in set, return the head
            if head in nodes_set :
                return head
            #also add the head to the set
            nodes_set.add(head)
            head = head.next
        return None
