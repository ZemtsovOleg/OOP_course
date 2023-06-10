class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, *args) -> None:
        self.root = None
        for value in args:
            self.insert(value)

    def insert(self, value) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert_recursive(self.root, value)

    def __insert_recursive(self, node: Node, value) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_recursive(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_recursive(node.right, value)

    def __eq__(self, other):
        if isinstance(other, BinaryTree):
            return self.__compare(self.root, other.root)
        else:
            raise TypeError

    def __len__(self):
        queue = [self.root]
        count = 0
        while queue:
            node = queue.pop()
            if node:
                queue += [node.left, node.right]
                count += 1
        return count

    def __compare(self, a: Node, b: Node):
        if a is None or b is None:
            return a is b

        return a.value == b.value and self.__compare(a.left, b.left) and self.__compare(a.right, b.right)

    def search(self, n: int) -> bool:
        node = self.root
        while node:
            if n == node.value:
                return True
            elif n < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def tree_traversal(self) -> list:
        result = []

        def inorder_traversal(node):
            if node is None:
                return None
            inorder_traversal(node.left)
            result.append(node.value)
            inorder_traversal(node.right)

        inorder_traversal(self.root)
        return result

    def tree_by_levels(self) -> list:
        queue = [self.root]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                queue += [node.left, node.right]
                result.append(node.value)

        return result


one = BinaryTree(10, 5, 6, 13, 16, 11, 2, 3, 12, 18)
