# Custom Library to make creating Trees simpler #
class Tree:
    def __init__(self):
        self.val = None
        self.right = None
        self.left = None

def TreeInsert(T , val):
    start = T
    t = Tree()
    t.val = val
    
    if T == None:
        return t
    
    while True:
        if T.val <= val:
            if T.right == None:
                T.right = t
                return start
            T = T.right
        else:
            if T.left == None:
                T.left = t
                return start
            T = T.left

def MakeTree(A):
    n = len(A)
    if n == 0:
        return None
    start = T = Tree()
    T.val = A[0]
    for i in range(1 , n):
        TreeInsert(T , A[i])
    return start

def CountTree(T):
    if T == None:
        return 0
    stack = [T]
    n = 0
    while len(stack) != 0:
        a = stack.pop()
        while a != None:
            n += 1
            if a.right != None:
                stack.append(a.right)
            a = a.left
    return n

def CountTreeHeight(T):
    if T == None:
        return 0
    stack = [T]
    heightStack = [0]
    max_height = 1
    while len(stack) != 0:
        a = stack.pop()
        height = heightStack.pop()
        while a != None:
            height += 1
            max_height = max(max_height , height)
            if a.right != None:
                stack.append(a.right)
                heightStack.append(height)
            a = a.left
    return max_height

def Arrify(T):
    n = CountTree(T)
    R = [None] * n
    id = 0
    queue = [T]
    while len(queue) != 0:
        a = queue.pop(0)
        R[id] = a.val
        id += 1
        if a.left != None: queue.append(a.left)
        if a.right != None: queue.append(a.right)
    # end while
    return R

# Example Uses #
#arr = [1,5,7,3,5,1]
#a = MakeTree(arr)
#print("Initial Array : " , arr)
#print("Tree Count : " , CountTree(a))
#print("Tree Height : " , CountTreeHeight(a))
#print("Tree Arrified : " , Arrify(a))
