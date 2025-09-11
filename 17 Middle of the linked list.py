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
#main code to find the middle and print the linked list
#slow and fast pointer approach
#slow pointer moves one step at a time
#fast pointer moves two steps at a time
#when fast pointer reaches the end, slow pointer will be at the midddle
def middleNode(head):
    slow =head
    fast=head
    while fast and fast.next:
        slow=slow.next 
        fast=fast.next.next
        
    return slow

def printlist(head):
    while head:
        print(head.data,end=" -> ")
        head=head.next
    print("None")
    
arr=list(map(int,input().split()))
list=buildlist(arr)
middle=middleNode(list)
printlist(middle)