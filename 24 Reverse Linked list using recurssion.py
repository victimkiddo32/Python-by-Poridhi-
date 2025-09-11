# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class solution:
    def reverselinkedlist(self,head=ListNode):
         # Base case: if head is None or only one node left
        if head is None or head.next is None:
            return head
        
        # Recursively reverse the rest of the list
        revhead = self.reverselinkedlist(head.next)

        # Rewire pointers:
        head.next.next = head   # makes next node point back to current (e.g., 3 -> 2)
        head.next = None        # breaks the old link (e.g., 2 -> 3)

        return revhead
    
#main code
arr=list(map(int,input().split()))
head=ListNode(arr[0])
tail=head
for i in range(1,len(arr)):
    temp=ListNode(arr[i])
    tail.next=temp
    tail=temp
    
list=solution()
reversed_head=list.reverselinkedlist(head)
def printlist(head):
    while head:
        print(head.val,end=" -> ")
        head=head.next 
    print("None")
        
printlist(reversed_head)