class node:
    def _init_(self,data):
        self.data=data
        self.lref=None
        self.rref=None
def inordertraversal(root):
    if root == None:
        return
    inordertraversal(root.lref)
    print(root.data,end=" ")
    inordertraversal(root.rref)
def preordertraversal(root):
    if root == None:
        return
    print(root.data,end=" ")
    preordertraversal(root.lref)
    preordertraversal(root.rref)
def postordertraversal(root):
    if root == None:
        return
    postordertraversal(root.rref)
    print(root.data,end=" ")
    postordertraversal(root.lref)


def levelordertraversal(root):
    if root ==None:
        return
    result=[]
    q=[root]
    while len(q)>0:
        n=len(q)
        sresult=[]
        for i in range (n):
            currnode=q.pop(0)
            sresult.append(currnode.data)
            if currnode.lref!=None:
                q.append(currnode.lref)
            if currnode.rref!=None:
                q.append(currnode.rref)
        result.append(sresult)
    print(result)


def zigzagLevelOrder(root):
        if root ==None:
            return
        result=[]
        q=[root]
        level=0
        while len(q)>0:
            n=len(q)
            sresult=[]
            for i in range (n):
                currnode=q.pop(0)
                sresult.append(currnode.data)
                if currnode.lref!=None:
                    q.append(currnode.lref)
                if currnode.rref!=None:
                    q.append(currnode.rref)
            if level%2==1:
                sresult=sresult[::-1]
            level+=1
            result.append(sresult)
        print (result)

def findleftview(root):
    if root ==None:
        return []
    result=[]
    q=[root]
    while len(q)>0:
        n=len(q)
        for i in range (n):
            currnode=q.pop(0)
            if i==0:
                result.append(currnode.data)
            if currnode.lref!=None:
                q.append(currnode.lref)
            if currnode.rref!=None:
                q.append(currnode.rref)
    print(result)
    
def findrightview(root):
    if root ==None:
        return []
    result=[]
    q=[root]
    while len(q)>0:
        n=len(q)
        for i in range (n):
            currnode=q.pop(0)
            if i==n-1:
                result.append(currnode.data)
            if currnode.lref!=None:
                q.append(currnode.lref)
            if currnode.rref!=None:
                q.append(currnode.rref)
    print(result)


def topViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
 
    topViewHelper(root.lref, store, hd - 1, level + 1)
    topViewHelper(root.rref, store, hd + 1, level + 1)
 
def findTopView(root):
    result = []
    if root == None:
        print(result)
 
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    print(result)
 
def bottomViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] < level:
        store[hd] = [level, root.data]
 
    bottomViewHelper(root.lref, store, hd - 1, level + 1)
    bottomViewHelper(root.rref, store, hd + 1, level + 1)
 
def findBottomView(root):
    result = []
    if root == None:
        print(result)
 
    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    print(result)
            



o1=node(30)
o2=node(40)
o3=node(50)
o4=node(60)
o5=node(70)
o6=node(80)
o7=node(90)
o8=node(100)
o9=node(110)
o10=node(-50)
o1.lref=o2
o1.rref=o3
o2.lref=o4
o2.rref=o5
o3.lref=o6
o3.rref=o7
o4.lref=o8
o4.rref=o9
o5.lref=o10
root=o1
inordertraversal(root)
print()
preordertraversal(root)
print()
postordertraversal(root)
print()
levelordertraversal(root)
print()
zigzagLevelOrder(root)
print()
findleftview(root)
print()
findrightview(root)
print()
findTopView(root)
print()
findBottomView(root)
