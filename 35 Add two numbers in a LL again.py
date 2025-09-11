class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)   
        tail = dummy
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = carry + val1 + val2
            digit = total % 10
            carry = total // 10
            
            # add new digit at tail
            tail.next = ListNode(digit)
            tail = tail.next
            
            # move forward
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next