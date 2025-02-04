# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    The idea is to create a dummy node and then move the prev pointer to the appropriate place.
    The prev pointer actually points to the last node of the merged linked list and is used to add the next node.
    We compare the values of the two linked lists and add the smaller value to the merged linked list.
    We add the next node to the prev pointer and then move the prev pointer to the next node.
    We also update the list1 or list2 pointer to the next node. We continue this process until one of the linked lists is empty.
    We then add the remaining linked list to the merged linked list using prev.next = list1 or list2.
    We return the next node of the dummy node which is the merged linked list.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode() # dummy node to start the linked list

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            
            prev = prev.next
        
        # add the remaining linked list to the merged linked list
        prev.next = list1 or list2

        return dummy.next
        