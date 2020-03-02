class Solution(object):
    def __init__(self):
        self.next = []

    def getNext(self, needle):
        self.next = []

        self.next.append(-1)

        i = 0
        j = -1

        while i < len(needle):
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                self.next.append(j)
            else:
                j = self.next[j]

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        self.getNext(needle)

        i = 0
        j = 0

        while i < len(haystack):
            #j == -1 代表第一个字符就不匹配
            if haystack[i] == needle[j] or j == -1:
                i += 1
                j += 1
            else:
                j = self.next[j]

            if j == len(needle):
                return i - j

        return -1

slt = Solution()
#print(slt.strStr("hello", "ll"))
print(slt.strStr("mississippi", "issip"))