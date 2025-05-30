# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')

        def dfs(node):
            nonlocal prev, min_diff
            if not node:
                return
            
            dfs(node.left)

            if prev is not None:
                diff = node.val - prev
                min_diff = min(min_diff, diff)
            
            prev = node.val

            dfs(node.right)

        dfs(root)           
        return min_diff