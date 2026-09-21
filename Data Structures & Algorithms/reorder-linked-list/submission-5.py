# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 2 3 4 5 6 7 8 9
        # 1 2 3 4 5
        # 9 8 7 6
        # Overall Problem: We need to tracerse the linked list backward
            # but we don't have backward next pointer
        # Sol: create a new reversed linked list, and alternatively add new nodes

        # Problem 2: How to find the seperate point?
        # Sol 2: slow and fast pointer method
            # Odd nodes: 1 2 3 4(s) | 5 6 7 None(f)
            # Even nodes: 1 2 3(s) | 4 5 6(f) None
            # -> Start of second Linked list is s.next
        
        # Step 1: find seperate point
        slow, fast = head, head.next # when slow and fast start from different point, s will stop at the same place in both odd and even.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Seperate two singly linked list
        second = slow.next
        slow.next = None
        
        
        # Step 2: reverse second Linked list
        prev = None
        while second:
            # Cache next node, because we are gonna break the link of next
            temp = second.next
            second.next = prev
            # update pointer
            prev = second
            second = temp
        
        # Step 3: merge two linked list
        secondHead, firstHead= prev, head
        while secondHead:
            # reserve next for first linked list
            temp1, temp2 = head.next, secondHead.next
            # link to second
            head.next = secondHead
            head = head.next #move
            # link to first
            head.next = temp1
            head = head.next #move
            # update second head
            secondHead = temp2


