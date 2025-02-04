# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        # Calculate the size of the linked list
        while curr:
            size += 1
            curr = curr.next
        
        # Edge case: if the size of the linked list is 1, return None
        if size == 1:
            return None

        # move to the desired node
        i = 0
        curr = head
        while i < size - n - 1 : # move to the node before the node to be removed
            curr = curr.next
            i += 1
        
        if n == size: # if the node to be removed is the head
            head = head.next
        else:
            curr.next = curr.next.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Better approach. Start with a dummy node and move the right pointer to the appropriate place.
    Then move both pointers until the right pointer reaches the end. The left pointer will be at the desired node which
    is one node before the node to be removed. So now we can remove the node by setting left.next = left.next.next

    This works for edge cases like [1] with n = 1 and output = [] 
    and [1, 2] with n = 2 with output [1] respectively.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # shift the right to the appropriate place
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next
        
        # now left is at the desired value and 
        left.next = left.next.next

        return dummy.next
        

        
        