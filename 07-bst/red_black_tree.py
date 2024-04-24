
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.left = None
        self.right = None 
        self.color = 'red'

    def __str__(self) -> str:
        return str(self.value)


class RedBlackTree:
    def __init__(self) -> None:
        self.root = None 

    def is_empty(self):
        return self.root is None

    def add(self, value):
        node = TreeNode(value)
        if self.is_empty():
            self.root = node 
        else:
            added = False
            temp = self.root
            while not added:
                if value > temp.value:
                    if temp.right is None:
                        temp.right = node
                        node.parent = temp
                        added = True
                    else:
                        temp = temp.right
                else:
                    if temp.left is None:
                        temp.left = node
                        node.parent = temp
                        added = True
                    else:
                        temp = temp.left
        self.insert_fixup(node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y 
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y 

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y 
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y 


    def insert_fixup(self, z):
        while z.parent is not None and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == 'red':      # Case 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.right:                   # Case 2
                    z = z.parent
                    self.left_rotate(z)
                else:                                       # Case 3
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:  # parent is right child of grandparent
                y = z.parent.parent.left
                if y is not None and y.color == 'red':      # Case 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.left:                   # Case 2
                    z = z.parent
                    self.right_rotate(z)
                else:                                       # Case 3
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'black'

    def inorder(self):
        stack = []
        temp = self.root
        while len(stack) > 0 or temp is not None:
            if temp is not None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(temp.value)
                temp = temp.right

    def postorder(self):
        pass

    def preorder(self):
        pass

    def inorder_recursive(self, node):
        if node is not None:
            self.inorder_recursive(node.left)
            print(node.value)
            self.inorder_recursive(node.right)

    def postorder_recursive(self, node):
        pass

    def preorder_recursive(self, node):
        pass

    def find(self, value):
        temp = self.root
        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                break 
        return temp
    
    def remove(self, value):
        node = self.find(value)
        if node is None:
            print("Value not found")
        else:
            # case 1 - Leaf
            if node.left is None and node.right is None:
                if node == self.root:
                    self.root = None
                elif value > node.parent.value:
                    node.parent.right = None
                else:
                    node.parent.left = None
            # case 2 - One child
            elif node.left is not None and node.right is None:
                node.value = node.left.value
                node.left = None
            elif node.right is not None and node.left is None:
                node.value = node.right.value
                node.right = None
            # case 3 - Two children 
            else:
                next = self.successor(node)
                next_value = next.value
                self.remove(next.value)
                node.value = next_value
                
    def successor(self, node):
        temp = node.right
        while temp.left is not None:
            temp = temp.left
        return temp
    
    def predecessor(self, node):
        pass

    def minimun(self):
        pass

    def maximum(self):
        pass

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1


if __name__ == "__main__":
    bst = RedBlackTree()
    # bst.add(35)
    # bst.add(46)
    # bst.add(12)
    # bst.add(100)
    # bst.add(11)
    # bst.add(3)
    # bst.add(38)
    # bst.add(32)
    for i in range(4000000):
        bst.add(i)

    print("Height:", bst.height(bst.root))
    print("Root:", bst.root.value)

    # bst.remove(35)
    # bst.inorder_recursive(bst.root)

    # n = bst.find(11)
    # print(n)
    # n = bst.find(120)
    # print(n)
