class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            return mirror(left.left, right.right) and mirror(left.right, right.left)
        return mirror(root.left, root.right)