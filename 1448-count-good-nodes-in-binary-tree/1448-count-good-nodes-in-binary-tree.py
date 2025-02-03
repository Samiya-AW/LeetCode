# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, max_node_val) -> int:
            if not root:
                return 0

            count = 0

            if root.val >= max_node_val:
                count += 1
            
            max_node_val = max(max_node_val, root.val)

            count += dfs(root.left, max_node_val)
            count += dfs(root.right, max_node_val)

            return count
        
        return dfs(root, root.val)