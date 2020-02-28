class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        cs = {}

        bp = 0
        ep = 0

        i = 0
        j = 0

        while i <= len(s) - 1:
            cs = {}
            cs[s[i]] = i

            j = i + 1

            while j <= len(s):
                if j == len(s):
                    length = max(length, j - i)
                    break

                if s[j] in cs:
                    length = max(length, j - i)
                    break
                else:
                    cs[s[j]] = j
                    length = max(length, j - i + 1)
                
                j = j + 1

            i = i + 1

        return length

test = "dvdf"

slt = Solution()
print(slt.lengthOfLongestSubstring(test))