class treenode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def make_tree(self,arr):
        root=treenode(arr[0])
        stack=[(root,0)]
        n=len(arr)
        while stack:
            node,i=stack.pop()
            print(node.data)

            left=2*i+1
            right=2*i+2

            if left<n and arr[right] is not None:
                node.right=treenode(arr[right])
                stack.append((node.right,right))

            if right<n and arr[left] is not None:
                node.left=treenode(arr[left])
                stack.append((node.left,left))

        return root
        
        
#Preorder traversal using stack
#DFS
        
if __name__=="__main__":
    arr=[10,5,6,2,13,22,14]
    tree=treenode(0)
    root=tree.make_tree(arr)




    


