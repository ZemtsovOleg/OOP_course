# Класс для хранения узла бинарного дерева.
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def max_path_sum(root) -> int:
    max_path = -float('inf')

    # post order traversal of subtree rooted at `node`
    def gain_from_subtree(node) -> int:
        nonlocal max_path

        if not node:
            return 0
        
        print(f'data={node.data}, max_path={max_path}')
        # add the gain from the left subtree. Note that if the
        # gain is negative, we can ignore it, or count it as 0.
        # This is the reason we use `max` here.
        gain_from_left = max(gain_from_subtree(node.left), 0)
        print(f'left={gain_from_left}, data={node.data}, max_path={max_path}')

        # add the gain / path sum from right subtree. 0 if negative
        gain_from_right = max(gain_from_subtree(node.right), 0)
        print(f'left={gain_from_left}, right={gain_from_right}, data={node.data}, max_path={max_path}')

        # if left or right gain are negative, they are counted
        # as 0, so this statement takes care of all four scenarios
        max_path = max(max_path, gain_from_left + gain_from_right + node.data)
        print(f'max_path={max_path}')

        # return the max sum for a path starting at the root of subtree
        return max(
            gain_from_left + node.data,
            gain_from_right + node.data
        )

    gain_from_subtree(root)
    return max_path


if __name__ == '__main__':

    root = None

    ''' Construct the following tree
            1
          /   \
         /     \
        2      10
       / \    /  \
     -1  -4  -5  -6
         /   / \
        4   7   4
             \
             -2
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(-1)
    root.left.right = Node(-5)
    root.right.left = Node(-5)
    root.right.right = Node(-6)
    root.left.right.left = Node(4)
    root.right.left.left = Node(7)
    root.right.left.right = Node(4)
    root.right.left.left.right = Node(-2)

    print('The maximum path sum is', max_path_sum(root))






# # Рекурсивная функция для нахождения максимальной суммы путей, "начиная" с
# # данный узел в бинарном дереве. Максимальная сумма путей между двумя узлами
# # в бинарном дереве обновляется в `result`
# def findMaxPathSum(node, result=float('-inf')):

#     # Базовый случай: пустое дерево
#     if node is None:
#         return 0, result

#     print(f'data={node.data}')

#     # найти максимальную сумму пути, "начиная" с левого дочернего элемента
#     left, result = findMaxPathSum(node.left, result)

#     print(f'left={left}, result={result}, data={node.data}')

#     # найти максимальную сумму пути, "начиная" с правого потомка
#     right, result = findMaxPathSum(node.right, result)

#     print(f'left={left}, right={right}, result={result}, data={node.data}')

#     # Попробуйте все возможные комбинации, чтобы получить оптимальный результат
#     result = max(result, node.data)
#     print(f'result={result}')
#     result = max(result, node.data + left)
#     print(f'result={result}')
#     result = max(result, node.data + right)
#     print(f'result={result}')
#     result = max(result, node.data + left + right)
#     print(f'result={result}')

#     # возвращает максимальную сумму путей, "начиная" с данного узла.
#     return max(node.data, node.data + max(left, right)), result
