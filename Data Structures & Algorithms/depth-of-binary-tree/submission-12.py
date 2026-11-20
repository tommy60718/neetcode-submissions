# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # in-order recurrsive dfs travesal
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # # pre-order iterative dfs travesal
        
        # if not root:
        #     return 0

        # dfs_stack = [(root, 1)]
        # max_level =1

        # while dfs_stack:
        #     node, level = dfs_stack.pop()
        #     # don't forget to update max_level
        #     max_level = max(max_level, level)
        #     if node.right:
        #         dfs_stack.append((node.right, level+1))
        #     if node.left:
        #         dfs_stack.append((node.left, level+1))
        # return max_level
            