# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head

        # find the mid point of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow = the mid point of the list

        # reverse the list from node after the slow node to the end of the list
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp


        # prev = the start of the reverse of the list
        # head = the start of the original list
        dummy = head

        while prev and head:
            # save the next nodes for updating prev and head
            t1 = prev.next
            t2 = head.next

            # if the head.next is not None, update the prev.next to head.next
            if head.next:
                prev.next = head.next
            
            head.next = prev # update the head.next to prev
            head = t2 # move the head to the next node 
            prev = t1 # move the prev to the next node
        
        return dummy.next