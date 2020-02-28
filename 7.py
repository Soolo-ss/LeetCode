class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        
        if x < 0:
            isNeg = True
            x = -x

        nl = list()

        n = 0
        while x != 0:
            n = x % 10
            x = int(x / 10)
            nl.append(n)

        sum = 0
        exp = 0
        for i in range(len(nl) - 1, -1, -1):
            sum = sum +  nl[i] * pow(10, exp)
            exp = exp + 1

        if isNeg:
            sum = -sum

        min = -(pow(2, 31))
        max = pow(2, 31) - 1

        if min > sum or sum > max:
            return 0

        return sum


slt = Solution()
print(slt.reverse(1534236469))