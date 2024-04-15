# Custom Library to make creating linked lists a bit simpler #

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    # end def
# end node
 
def make_nodes(a):
    start = Node(0)
    p = start
    for i in range(0, len(a)):
        p.next = Node(a[i])
        p = p.next
    return start.next
# end def

def make_cycle(a):
    start = Node(0)
    p = start
    for i in range(0, len(a)):
        p.next = Node(a[i])
        p = p.next
    p.next = start.next
    return start.next
# end def

def print_node_list(n):
    start_point = n
    while n != None:
        print(n.val, end=' ')
        n = n.next
        if n == start_point:
            print(" <- cycle")
            return
    print("")
# end def
