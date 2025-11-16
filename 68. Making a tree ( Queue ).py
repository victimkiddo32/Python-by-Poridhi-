class treenode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def make_tree(self,arr):
        root=treenode(arr[0])
        print(root.data)
        queue=[root]
        n=len(arr)
        i=1
        for node in queue:
            if i>=n:
                break
            if i<n and arr[i] is not None:
                node.left=treenode(arr[i])
                queue.append(node.left)
                print(node.left.data)
                i+=1
            if i<n and arr[i] is not None:
                node.right=treenode(arr[i])
                queue.append(node.right)
                print(node.right.data)
                i+=1 
      
        return root


#Level order traversal using queue
#BFS
        

        
if __name__=="__main__":
    arr=[10,5,6,2,13,22,14]
    tree=treenode(0)
    root=tree.make_tree(arr)



    


