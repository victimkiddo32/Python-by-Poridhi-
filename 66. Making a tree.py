class treenode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def make_tree(self,arr,i=0):
        if i>=len(arr):
            return None
        root=treenode(arr[i])
        root.left=self.make_tree(arr,2*i+1) 
        root.right=self.make_tree(arr,2*i+2)
        return root
    
    def print_tree(self,root):
        if root:
            print(root.data)
            self.print_tree(root.left)
            self.print_tree(root.right)

        

if __name__=="__main__":
    arr=[10,5,6,2,13,22,14]
    tree=treenode(0)
    root=tree.make_tree(arr)
    tree.print_tree(root)




            
        
    


