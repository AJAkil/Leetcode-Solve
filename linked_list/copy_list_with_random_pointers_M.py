"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        curr = head
        # the hashmap is needed to keep track of the old node to new node mapping as we create the new nodes for copying we need to know the reference to the new node
        # for updating the next and random pointers
        # create new nodes for copying but dont add the next and random pointers
        # keep track of the old node to the new node mapping.
        # this is needed to update the next and random pointers
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # start from the head and update the next and random pointers
        curr = head


        while curr:
            copied_curr = old_to_new[curr] # get the copied node
            copied_curr.next = old_to_new.get(curr.next, None) # update the next pointer
            copied_curr.random = old_to_new.get(curr.random, None) # update the random pointer
            curr = curr.next # move to the next node
        
        return old_to_new.get(head, None) # return the head of the copied linked list
        