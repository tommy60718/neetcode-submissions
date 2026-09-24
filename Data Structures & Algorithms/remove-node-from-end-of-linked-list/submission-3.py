# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Main: re-connect nodes
        # Problem: choose from the back
            # Sol: two pointer
        # Case: 1 2 3 4 None, n=2
            # size = 4
            # 4-2=2 -> pointer move 2 to target
            # But we need to reconnect 4-3=1 -> pointer move 1 to target
            # leftBridge ( start from dummy) = size - n
        
        sizeCounter = 0
        counterNode = head
        dummy = ListNode(0, head)
        leftBridge = dummy

        # Step1: Calculate size
        while counterNode:
            counterNode = counterNode.next
            sizeCounter += 1
        
        # Step2: move left Bridge, 
        # leftBridge = size - n
        for _ in range(sizeCounter-n):
            leftBridge = leftBridge.next
        
        # Step3: Reconnect
        leftBridge.next = leftBridge.next.next
        
        # Return
        return dummy.next



        