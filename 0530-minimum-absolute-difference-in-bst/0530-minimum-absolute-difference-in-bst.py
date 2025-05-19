# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')

        def dfs(node):
            nonlocal prev, min_diff
            if not node:            # If node == None then return
                return
            
            dfs(node.left)          # Inorder node's left child call

            # If prev != None then process current node
            if prev is not None:    
                diff = node.val - prev
                min_diff = min(min_diff, diff)

            prev = node.val         # Update value of prev with current node's value

            dfs(node.right)         # Inorder node's right child call

        dfs(root)
        return min_diff