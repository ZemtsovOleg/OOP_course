class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, *args) -> None:
        self.root = None
        for val in args:
            self.insert(val)

    def insert(self, val) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert_recursive(self.root, val)

    def __insert_recursive(self, node: Node, val) -> None:
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert_recursive(node.left, val)
        if val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert_recursive(node.right, val)

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.val, end=' ')
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return None
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.val, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
            print()


one = BinaryTree(10, 5, 6, 13, 16, 11, 2, 3, 12)
two = BinaryTree(1, 5, 6, 13, 16, 9, 2, 3, 12)

one.show_tree(one.root)
one.show_wide_tree(one.root)
