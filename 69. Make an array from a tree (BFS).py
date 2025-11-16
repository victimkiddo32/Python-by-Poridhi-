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
    
    def BFS_array(self,root):
        if not root:
            return []
        arr=[]
        queue=[root]
        for node in queue:
            if node:
                arr.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        return arr       
    
if __name__ == "__main__":
    arr = [10, 5, 6, 2, 13, 22, 14]
    tree = treenode(0)
    root = tree.make_tree(arr)
    print(tree.BFS_array(root))