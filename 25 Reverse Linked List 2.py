# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        if not head or left==right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        for _ in range(left-1):
            prev=curr
            curr=curr.next
            
        for _ in range(right-left):
            nextnode=curr.next
            curr.next=nextnode.next 
            nextnode.next=prev.next
            prev.next=nextnode
            
        # 1 2 3 4 5
        # 1->3->2->4->5
        # 1->4->3->2->5
        return dummy.next
    
#main code
arr=list(map(int,input().split()))
head=ListNode(arr[0])
tail=head
for i in range(1,len(arr)):
    temp=ListNode(arr[i])
    tail.next=temp
    tail=temp
    
list=Solution()
reversed_head=list.reverseBetween(head,2,4)
def printlist(head):
    while head:
        print(head.val,end=" -> ")
        head=head.next 
    print("None")
        
printlist(reversed_head)