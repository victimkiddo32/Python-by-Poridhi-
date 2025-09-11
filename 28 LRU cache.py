class ListNode:
    def __init__(self,key:int,val:int):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=ListNode(-1,-1)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def add_after_head(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        
    def remove_node(self,node):
        prev_node=node.prev
        next_node=node.next 
        prev_node.next=next_node
        next_node.prev=prev_node
        
    def remove_from_end(self):
        if self.tail.prev==self.head:
            return None
        node=self.tail.prev
        self.remove_node(node)
        return node
    
class LRUCache:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.map={}  #key->node
        self.dll=DoublyLinkedList()
        
    def get(self,key:int)->int:
        if key in self.map:
            node=self.map[key]
            self.dll.remove_node(node)
            self.dll.add_after_head(node)
            return node.val
        return -1

    def put(self,key:int,value:int):
        if key in self.map:
            node=self.map[key]
            node.val=value
            self.dll.remove_node(node)
            self.dll.add_after_head(node)
        else:
            if len(self.map)>=self.capacity:
                lru=self.dll.remove_from_end()
                if lru:
                    del self.map[lru.key]
                    
            newnode=ListNode(key,value)
            self.dll.add_after_head(newnode)
            self.map[key]=newnode
            
#main code 
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # returns 1
lru.put(3, 3)      # evicts key 2
print(lru.get(2))  # returns -1 (not found)
                    
            
            
        
           
        
    
    
    