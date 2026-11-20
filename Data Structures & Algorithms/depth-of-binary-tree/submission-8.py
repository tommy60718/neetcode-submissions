# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Sol 1: dfs in-order recursive
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # Sol 2: dfs pre-order iterative
        if not root:
            return 0
        
        dfs_stack = [(root, 1)]
        max_level = 1

        while dfs_stack:
            node, level = dfs_stack.pop()
            max_level = max(level, max_level)
            if node.right:
                dfs_stack.append((node.right, level+1))
            if node.left:
                dfs_stack.append((node.left, level +1))
        return max_level
            
