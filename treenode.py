# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        pass


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