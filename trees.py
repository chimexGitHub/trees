import collections


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

        # defining an insertion function of a tree

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=' ')
        inOrderPrint(r.right)

def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)

def postOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        postOrderPrint(r.right)
        postOrderPrint(r.left)

def makeList(r):
    if r is None:
        return
    else:
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)
    return d

def bfs(al):
    queue = collections.deque('g')
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
        print(visited)

def dfs(al):
    stack = ['g']
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
            print(visited)


def search(al, key):
    stack = ['g']
    visited = []
    found = False
    while stack:
        node = stack.pop()
        if node == key:
            return True
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    return found


if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')

    d = {}
    # adjacency list
    aList = makeList(root)
    # print(aList)
    # for ele in aList:
       # print(f'{ele}:{d[ele]}')

   # bfs(aList)

   # dfs(aList)

print(search(aList, 'a'))

    # InOrder: left, root, right
    # PreOrder: root, left, right

    # printing all nodes inOrder
     # inOrderPrint(root)

    # printing all nodes preOrder
    # preOrderPrint(root)

    # printing all nodes postOrder
    # postOrderPrint(root)