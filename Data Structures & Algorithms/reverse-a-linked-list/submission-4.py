# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input: 0, 1, 2, 3
        # output: 3, 2, 1, 0

        #Init,Class assign is ALIAS, they point to the same object.
        curr, prev =head, None

        # loop stops when "curr" exceed the end, 
        # so prev is the actual new head
        while curr:
            # Update "next"
            temp = curr.next # record next, so we have the location
            curr.next = prev # point back

            # Update "pointers"
            prev = curr
            curr = temp
        return prev
            

            




