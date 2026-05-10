# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next    # this is the pointer

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fake_root = ListNode()
        tail = fake_root

        #while we have l1 and l2 list proceed with ->
        while l1 and l2:
            # if value of l1 is less than value of l2
            if l1.val < l2.val:
                # take l1 value and insert it as the tail
                tail.next = l1
                #update l1 pointer
                l1 = l1.next
            # if l2 is less than or equal to l1
            else:
                #update l2 pointer
                tail.next = l2
                l2 = l2.next
            #tail pointer has to be updated regardless
            tail = tail.next
        #if l1 or l2 is empty
        #if we have values in l1
        if l1:
            # taking the remainder of l1 and inserting to end of list
            tail.next = l1
        elif l2:
            tail.next = l2

        return fake_root.next