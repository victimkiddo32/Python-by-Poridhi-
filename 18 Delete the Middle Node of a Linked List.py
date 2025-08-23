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

# function to delete the middle node of a linked list
def deleteMidNode(head):
    slow=head
    fast=head
    prev=None
    
    while fast and fast.next :
        prev=slow
        slow=slow.next
        fast=fast.next.next
        
    if prev:
        prev.next=slow.next
        
    return head


        
arr=list(map(int,input().split()))
list=buildlist(arr)
head=deleteMidNode(list)
printlist(head)


 