class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        minNode = None
        result = None
        tmp = None
        while (minNode = self.getMinNode(l1, l2) is not None):
            if result is None:
                result = minNode
            else:
                result.next = minNode

    def getMinNode(self, l1, l2):
        if l1 is not None and l2 is not None:
            return l1 if l1.val <= l2.val else l2
        elif l1 is not None:
            return l1
        elif l2 is not None:
            return l2
        else:
            return None