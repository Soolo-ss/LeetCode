class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        121 

        -121

        10
        """
        str_x = str(x)

        result = False

        bp = 0
        ep = len(str_x) - 1

        if ep <= bp:
            return True

        while ep > bp:
            if bp == "+":
                bp += 1
                continue

            if bp == "-":
                return False

            if str_x[bp] != str_x[ep]:
                return False

            bp += 1
            ep -= 1

        return True

slt = Solution()
print(slt.isPalindrome(121))

