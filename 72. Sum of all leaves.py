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
    

    def DFS_array(self,root,arr=[]):
        if not root:
            return []
        
        arr.append(root.data)
        self.DFS_array(root.left,arr)
        self.DFS_array(root.right,arr)

        return arr
    
    def SumOfLeaves(self,root):
        if not root:
            return 0
        
        if root.left is None and root.right is None:
            return root.data

        return self.SumOfLeaves(root.left) + self.SumOfLeaves(root.right)
    

            
    
if __name__ == "__main__":
    arr = [10, 5, 6, 2, 13, 22, 14]
    tree = treenode(0)
    root = tree.make_tree(arr)
    print(tree.DFS_array(root))
    print(tree.SumOfLeaves(root))