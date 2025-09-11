class node:
    def __init__(self,val:str,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next
        
class BrowserHistory:
    def __init__(self,homepage:str):
        self.curr=node(homepage)
        
    def forward(self, steps: int):
        while self.curr.next and steps>0:
            self.curr=self.curr.next
            steps-=1
        return self.curr.val
    
    def back(self, steps: int):
        while self.curr.prev and steps>0:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val
    
    def visit(self,url:str):
        newnode=node(url)
        self.curr.next=newnode
        newnode.prev=self.curr
        self.curr=newnode
        
# Your BrowserHistory object will be instantiated and called as such:
str1=input()
obj = BrowserHistory(str1)
str2=input()
obj.visit(str2)
param_2 = obj.back(1)
param_3 = obj.forward(1)