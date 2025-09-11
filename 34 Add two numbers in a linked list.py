# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addatTail(self,head:ListNode,tail:ListNode,val:int):
        newnode=ListNode(val)
        if head is None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=newnode
            
        return head,tail    
    
    def addTwoNumbers(self, l1: ListNode, l2:ListNode) ->ListNode:
        carry=0
        anshead=ListNode(0)
        anstail=anshead
        
        while l1!=None or l2!=None or carry!=0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
        
        sum=carry+val1+val2
        digit=sum%10
        carry=sum//10
        anshead,anstail=self.addatTail(anshead,anstail,digit)
        if l1 is not None:
            l1=l1.next 
        if l2 is not None:
            l2=l2.next
            
        return anshead
        
  