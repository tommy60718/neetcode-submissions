# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Q1: How to record visited?
        # Q2: every value is distinct? If not, how to trace?

        # Use "set(hash set)" to record visited
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

        # Use Floyd's tortoise and Hare method
        # 1. Core: If cycle exists, the hare will finally catch up on tortoise
        # 2. Case study: 
            # Case: If the cycle lenth 10, than the Hare will catch up on tortoise 
                # in 10 steps at most: 
            # Math: The distance between Hare and tortoise = 10
                # Each step : 10 + 1(tortoise) -2 (Hare) -> each step they get 1 closer
            # Answer: at most 10 steps the Hare will catch up on Tortoise.
        """
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        """
