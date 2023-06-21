class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
     
    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp
 
        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)
 
        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root
 
def printPostorder(root,arr):
    printPostorder.arr=arr
 
    if root != None:
 
        # First recur on left child
        printPostorder(root.left,printPostorder.arr)
 
        # the recur on right child
        printPostorder(root.right,printPostorder.arr)
 
        # now print the data of node
        printPostorder.arr.append(root.data)


    
 
# Driver Code
if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    arr=[]
    printPostorder(root,arr)
    for x in range(0,len(printPostorder.arr)-1):
        print((printPostorder.arr)[x],end=" ")
    print(printPostorder.arr[-1])