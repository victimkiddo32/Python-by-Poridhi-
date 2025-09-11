# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class solution:
    def reverse(self,head=ListNode):
        prev=None
        curr=head
        
        while curr:
            nextnode=curr.next 
            curr.next=prev
            prev=curr
            curr=nextnode
            
        return prev
    
#main code
arr=list(map(int,input().split()))
head=ListNode(arr[0])
tail=head
for i in range(1,len(arr)):
    temp=ListNode(arr[i])
    tail.next=temp
    tail=temp
    
list=solution()
reversed_head=list.reverse(head)
def printlist(head):
    while head:
        print(head.val,end=" -> ")
        head=head.next 
    print("None")
        
printlist(reversed_head)
