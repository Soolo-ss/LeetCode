# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = None
        tmp = None
        minNode = None
        while True:
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    minNode = l1
                    l1 = l1.next
                else:
                    minNode = l2
                    l2 = l2.next
            elif l1 is not None:
                minNode = l1
                l1 = l1.next
            elif l2 is not None:
                minNode = l2
                l2 = l2.next
            else:
                minNode = None

            if minNode is None:
                break

            if result is None:
                result = ListNode(minNode.val)
                tmp = result
            else:
                tmp.next = ListNode(minNode.val)
                tmp = tmp.next

        return result


slt = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

slt.mergeTwoLists(l1, l2)