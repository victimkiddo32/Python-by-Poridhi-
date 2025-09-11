# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:ListNode) -> ListNode:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next 
            if slow==fast:
                return slow
        return slow
    
    def detectCycle(self, head:ListNode) -> bool:
        slow=head
        intersection=self.hascycle(head)
        if not intersection:
            return None
        
        while slow is not intersection:
            slow=slow.next
            intersection=intersection.next 
            
        if slow==intersection:
            return slow
        
        return -1
        
        