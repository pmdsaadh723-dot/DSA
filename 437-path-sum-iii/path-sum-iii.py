# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix = {0: 1}
        def dfs(node, currentSum):
            if not node:
                return 0
            currentSum += node.val
            paths = prefix.get(currentSum - targetSum, 0)
            prefix[currentSum] = prefix.get(currentSum, 0) + 1
            paths += dfs(node.left, currentSum)
            paths += dfs(node.right, currentSum)
            prefix[currentSum] -= 1
            return paths
        return dfs(root, 0)