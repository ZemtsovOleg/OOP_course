class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, *args):
        self.root = None
        for key in args:
            self.insert(key)

    def insert(self, key) -> None:
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: Node, key) -> None:
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        if key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # def show_tree(self, node=1):
    #     if node == 1:
    #         node = self.root
    #     if node is None:
    #         return
    #     self.show_tree(node.left)
    #     print(node.key, end=' ')
    #     self.show_tree(node.right)
    #
    # def show_wide_tree(self, node=1):
    #     if node == 1:
    #         node = self.root
    #     if node is None:
    #         return None
    #     v = [node]
    #     while v:
    #         vn = []
    #         for x in v:
    #             print(x.key, end=' ')
    #             if x.left:
    #                 vn += [x.left]
    #             if x.right:
    #                 vn += [x.right]
    #         v = vn
    #         print()

    def find_max_branch_sum(self) -> int:
        if self.root is None:
            return None

        max_sum = float('-inf')

        def max_branch_sum(node):
            nonlocal max_sum

            if node is None:
                return 0

            left_sum = max_branch_sum(node.left)
            right_sum = max_branch_sum(node.right)

            max_sum = max(max_sum, node.key + max(left_sum, right_sum))
            return node.key + max(left_sum, right_sum)

        max_branch_sum(self.root)
        return max_sum


one = BinaryTree(10, 5, 6, 13, 16, 11, 2)

print(one.find_max_branch_sum())
# one.show_tree()
# one.show_wide_tree()


# def max_path_sum(node):
#     if node is None:
#         return None
#     max_path_sum(node.left)
#     max_path_sum(node.right)
#     return

# print(max_path_sum(one.root))


# def rec(value):
#     print(value)
#     if value < 5:
#         rec(value+1)
#     print(value)

# rec(1)


# def fac_rec(n):
#     if n < 2:
#         return 1
#     return n * fac_rec(n-1)

# print(fac_rec(5))
