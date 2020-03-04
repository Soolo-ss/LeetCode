# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def loop(root):
            if root is None:
                return
            
            if root.left is not None :
               loop(root.left)

            result.append(root.val)

            if root.right is not None:
                loop(root.right)


        result = []
  
        loop(root)

        return result