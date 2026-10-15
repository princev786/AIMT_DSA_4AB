class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

#NLR
def preorder(root):
    if root == None:
        return
    print(root.data ,end =" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data , end =" ")
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data , end =" ")

def levelorder(root):
    if root == None:
        return
    que = [] 
    que.append(root)
    while len(que)!=0:
        curr = que[0]
        print(curr.data ,end =" ")
        del que[0]
        if curr.left != None:
            que.append(curr.left)
        if curr.right != None:
            que.append(curr.right)

def height(root):
    if root ==None:
        return 0
    left = height(root.left)
    right = height(root.right)

    return 1+max(left,right)

def count(root):
    if root == None:
        return 0
    c=0
    que = []
    que.append(root)
    while len(que)!=0:
        curr = que[0]
        del que[0]
        c+=1
        if curr.left != None:
            que.append(curr.left)
        if curr.right != None:
            que.append(curr.right)
    return c

def buildtree(lst):
    if len(lst)==0:
        return None
    que = [] 
    root = Node(lst[0])
    que.append(root)
    i=1
    while len(que)!=0 and i<len(lst):
        curr = que[0]
        del que[0]
        if lst[i]!=None:
            curr.left = Node(lst[i])
            que.append(curr.left)
        if lst[i+1]!=None:
            curr.right = Node(lst[i+1])
            que.append(curr.right)
        i+=2
    return root

def isIdentical(root1,root2):
    if root1==None and root2==None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.data != root2.data:
        return False
    return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)

def ismirror(root1,root2):
    if root1==None and root2==None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.data != root2.data:
        return False
    return ismirror(root1.left,root2.right) and ismirror(root1.right,root2.left)

def diameter(root,lst):
    if root == None: 
        return 0
    left = diameter(root.left,lst)
    right = diameter(root.right,lst)

    lst[0] = max(lst[0],1+left+right)

    return 1+max(left,right)

def LCA(root,p,q):
    if root == None:
        return None
    if root == p or root==q:
        return root
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)

    if left!=None and right!=None:
        return root

    if left!=None:
        return left
    return right

def leftview(root):
    que = []
    que.append(root)
    while len(que)!=0:
        s = len(que)
        for i in range(0,s):
            curr = que[0]
            del que[0]
            if i==0:
                print(curr.data)
            if curr.left !=None:
                que.append(curr.left)
            if curr.right !=None:
                que.append(curr.right)

def rightview(root):
    que=[]
    que.append(root)
    while(len(que)!=0):
        s = len(que)
        for i in range(0,s):
            curr = que[0]
            del que[0]
            if(i==s-1):
                print(curr.data)
            if curr.left !=None:
                que.append(curr.left)
            if curr.right !=None:
                que.append(curr.right)
def ispathexist(root,target):
    if(root == None):
        return False
    if root.left == None and root.right == None and root.data == target:
        return True

    return ispathexist(root.left,target-root.data) or ispathexist(root.right,target-root.data)

def printpath(root,target,path,res):
    if(root == None):
        return
    if(root.left == None and root.right == None and root.data == target):
        res = list(path)
        res.append(root.data)
        print(res)

    path.append(root.data)
    printpath(root.left,target-root.data,path,res)
    printpath(root.right,target-root.data,path,res)
    del path[len(path)-1]

if __name__ == "__main__":
    root1 = buildtree([10,20,30,40,50,60,70,None,None,None,80])
    root2 = buildtree([5,2,4,3,None,2,8,1,None,None,None,None,6])

    printpath(root2,11,[],[])
    # print(ispathexist(root2,10))






    
    # lst=[0]
    # leftview(root1)
    # diameter(root2,lst) 
    # print(lst[0])
    # preorder(root)
    # preorder(root)
    # print()
    # inorder(root)
    # print()
    # postorder(root)
