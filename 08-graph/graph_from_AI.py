class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


# Graph class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            for adj in self.adj[i]:
                print(" -> {}".format(adj), end="")
            print(" \n")


if __name__ == "__main__":
    # Create a graph
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    print("Graph representation:")
    graph.print_graph()

    # Create a Binary Search Tree
    # bst = None
    # numbers = [10, 5, 15, 3, 7, 12, 17]
    # for num in numbers:
    #     bst = insert(bst, num)

    # print("\nBinary Search Tree representation (Inorder traversal):")
    # inorder_traversal(bst)
