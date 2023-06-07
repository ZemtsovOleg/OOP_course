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


    # def find_max_branch_sum(self) -> int:
    #     if self.root is None:
    #         return None

    #     max_sum = float('-inf')

    #     def max_branch_sum(node):
    #         nonlocal max_sum

    #         if node is None:
    #             return 0

    #         left_sum = max_branch_sum(node.left)
    #         right_sum = max_branch_sum(node.right)

    #         max_sum = max(max_sum, node.key + max(left_sum, right_sum))
    #         return node.key + max(left_sum, right_sum)

    #     max_branch_sum(self.root)
    #     return max_sum


one = BinaryTree(10, 5, 6, 13, 16, 11, 2, 3, 12)
two = BinaryTree(1, 5, 6, 13, 16, 9, 2, 3, 12)

# print(one.find_max_branch_sum())
one.show_tree()
one.show_wide_tree()


def compare(a, b):
    if a is None or b is None:
        return a is b
    return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)


print(compare(one.root, two.root))


