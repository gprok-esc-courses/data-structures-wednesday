
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.left = None
        self.right = None 

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
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

    def preorder(self):
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

    def inorder(self):
        pass

    def preorder_recursive(self, node):
        if node is not None:
            self.preorder_recursive(node.left)
            print(node.value)
            self.preorder_recursive(node.right)

    def postorder_recursive(self, node):
        pass

    def inorder_recursive(self, node):
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


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(35)
    bst.add(46)
    bst.add(12)
    bst.add(100)
    bst.add(11)
    bst.add(3)
    bst.add(38)
    bst.add(32)

    bst.remove(35)
    bst.preorder_recursive(bst.root)

    # n = bst.find(11)
    # print(n)
    # n = bst.find(120)
    # print(n)
