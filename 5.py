class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 

        if len(s) == 0 or not s:
            return ""

        p = [None] * len(s)
        for i in range(len(s)):
            p[i] = [0] * len(s)
        max = 0
        maxpos = None

        for i in range(len(s)):
            p[i][i] = 1
            maxpos = (i, i)

        for i in range(len(s)):
            if i + 1 < len(s):
                if s[i] == s[i + 1]:
                    p[i][i + 1] = 1
                    maxpos = (i, i + 1)

        if len(s) < 3:
            return s[maxpos[0] : maxpos[1] + 1]

        pl = 3

        while pl <= len(s):
            for i in range(0, len(s) - pl + 1):
                if s[i] == s[i + pl - 1] and p[i + 1][i + pl - 2] == 1:
                    p[i][i + pl - 1] = 1
                    max = pl
                    maxpos = (i, i + pl - 1)

            pl = pl + 1

        return s[maxpos[0]:maxpos[1] + 1]

slt = Solution()

print(slt.longestPalindrome("babad"))