class listnode:
    def __init__(self,data=0):
        self.data=data
        self.next=None

def buildlist(arr):
    head=listnode(arr[0])
    tail=head
    for i in range(1,len(arr)):
        temp=listnode(arr[i])
        tail.next=temp
        tail=temp
    return head

def printlist(head):
    while head:
        print(head.data,end=" -> ")
        head=head.next
    print("None")   
    
def removeNthNodefromEnd(head,n):
    dummy=listnode(0)
    dummy.next=head
    slow=dummy
    fast=dummy
    
    for _ in range(n+1):
        fast=fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next

    # Delete the nth node from the end
    slow.next = slow.next.next
        
    return dummy.next

arr=list(map(int,input().split()))
list=buildlist(arr)
head=removeNthNodefromEnd(list,2)
printlist(head)