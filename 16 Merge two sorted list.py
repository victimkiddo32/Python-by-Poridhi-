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

def mergetwosortedlist(list1,list2):
    dummy=listnode(0)
    tail=dummy
    #dummy is a placeholder to start the merged list
    if not list1:
        return list2
    if not list2:
        return list1
        
    while list1 and list2:
        if list1.data<list2.data:
            tail.next=list1
            list1=list1.next
            tail=tail.next
        else:
            tail.next=list2
            list2=list2.next 
            tail=tail.next
                
    tail.next=list1 if list1 else list2
            
    return dummy.next
    
def printlist(head):
    while head:
        print(head.data,end=" -> ")
        head=head.next
    print("None")
        
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

list1=buildlist(arr1)
list2=buildlist(arr2)
merged_list=mergetwosortedlist(list1,list2)
printlist(merged_list)


                
            
                