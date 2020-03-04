# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []

        tmp = head
        while tmp != None:
            stack.append(tmp)
            tmp = tmp.next
        
        while n > 0:
            tmp = stack.pop()
            n = n - 1

        prev = None if len(stack) == 0 else stack.pop()
        next = tmp.next

        if prev is None:
            head = next
        else:
            prev.next = next

        return head

head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

slt = Solution()
slt.removeNthFromEnd(head, 1)