class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next
        return curr.val if curr else -1
    
    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val)
        if self.head is None:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            
    def addAtTail(self, val: int) -> None:
        newnode = ListNode(val)
        if self.head is None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                return
            curr = curr.next
        
        if curr is None:
            return
        
        newnode = ListNode(val)
        newnode.next = curr.next
        curr.next = newnode
        
        if newnode.next is None:
            self.tail = newnode
            
    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                return
            curr = curr.next
        
        if curr is None or curr.next is None:
            return
        
        curr.next = curr.next.next
        if curr.next is None:  
            self.tail = curr

#main code
obj = MyLinkedList()
obj.addAtHead(1)          # [1]
obj.addAtTail(3)          # [1,3]
obj.addAtIndex(1,2)       # [1,2,3]
print(obj.get(1))         # 2
obj.deleteAtIndex(1)      # [1,3]
print(obj.get(1))         # 3
