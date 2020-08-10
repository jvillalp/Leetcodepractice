
"""
- in this problem, you want to remove the kth node from the end of the linked list in place
- they are not asking us to create a new linked list


- First, want to check the contrains of the input. 
    K should be at least one, which means we take out last node
- return head because we want to return linked list, unchanged

- I wanted to make it easier to locate each node so 
    created empty array to store every single node in the linked list
    (lines 10-14)


- after creating an array of the nodes of the linked list, 
- if k is longer than linked list, return head unchanged

- we want to know how far away we are from the end, where k = 1
- once we locate index of k, we can pop the kth index from the linked list
(line 17-18)

- Go through the entire list of nodes that was created and 
    connect each node to the next node after kth node is removed




  T  O(n) -  while loop O(n) + for loop O(n) where n is the number of nodes in the linked list

  S O(n) - we are storing n number of nodes in an array 

- Going through the entire list of elements twice, but should go through it once
- inefficient because you are going through the entire array, 
  connecting all nodes one at a time even though all but one of the nodes are already connected
- In a better case scenario, we can just connect the previous index of the removed node to the index of where the next node is, then we can just do o(n), but only going through list once

"""

def remove_kth_from_end(head, k):   #we have the head and the kth node as the parameters

    
    if k == 0:     #k has to be at least one.   [if k <= 0:]
        return head    #if k is zero, do nothing and return head - is head the entire linked list?



    ######you have to create an empty array where we can store all the nodes to point to each other, 

    listOfNodes = []    #emtpy array to store pointer to each node
    pointer = head     #created a reference to head - why? 
    while pointer is not None:   
        listOfNodes.append(pointer)   #append pointer of current node
        pointer = pointer.next #go to next node


    #if k longer than length of the linked list, 
    #the linked list should not be changed
    
    if k > len(listOfNodes): #here we know the len of listOfNodes
        return head


    # we want the 0th index in this case, so did not include len(listofnodes)-1
    #want to complute how
    indexToRemove = len(listOfNodes) - k     #remove node that is kth from last
    listOfNodes.pop(indexToRemove)     #remove the node in that index
    

    # go through the entire list of nodes that was created and 
    # connect each node to each other after kth node is removed

    for i in range(len(listOfNodes)-1):     #iterate through list in range from len of ListOfNodes -1
        listOfNodes[i].next = listOfNodes[i+1]         #connect each node to the next node
    listOfNodes[-1].next = None     #last node connect to None
    return listOfNodes[0]     #return head of list
    
    ###########EDIT################
    
    if indexToRemove - 1 == len(listOfNodes) -1: #
        listOfNodes[indexToRemove-1].next = None #check if values equal to each other, if so, last node = Node
    else:
        listOfNodes[indexToRemove-1].next = listOfNodes[indexToRemove] #make the previous node connect to the next node, which is now indexToRemove




# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#