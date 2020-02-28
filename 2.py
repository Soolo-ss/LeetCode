# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.add = False

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = None
        now = None

        while l1 != None or l2 != None:
            tmp = ListNode(0)

            tmp.val = self.addSingle(l1, l2)

            if result is None:
                result = tmp
                now = tmp
            else:
                now.next = tmp
                now = tmp

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if self.add == True:
            now.next = ListNode(1)

        return result

    def addSingle(self, l1, l2):
        l1_val = 0
        l2_val = 0

        if l1 != None:
            l1_val = l1.val

        if l2 != None:
            l2_val = l2.val

        sum = 0

        if self.add == True:
            sum = 1
            
        self.add = False

        sum += (l1_val + l2_val)

        if sum >= 10:
            self.add = True
            return sum % 10
        else:
            return sum

lhs = ListNode(9)
lhs.next = ListNode(8)
rhs = ListNode(1)

slt = Solution()
result = slt.addTwoNumbers(lhs, rhs)

while result != None:
    print(result.val)
    result = result.next



