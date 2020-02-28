class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0

        if not str:
            return result

        fi = -1
        for i in range(len(str)):
            if not str[i].isspace():
                fi = i
                break

        if fi == -1:
            return 0

        fc = str[fi]

        isNeg = False
        if fc == "-":
            isNeg = True
            fi += 1
        elif fc == "+":
            fi += 1
        elif not fc.isdigit():
            return result

        result_str = ""

        while fi < len(str) and str[fi].isdigit():
            result_str += str[fi]
            fi += 1

        if not result_str:
            return 0

        result = int(result_str)

        if isNeg:
            result = -result

        if result > (pow(2, 31) - 1):
            return pow(2, 31) - 1

        if result < (-pow(2, 31)):
            return -(pow(2, 31))

        return result

slt = Solution()

print(slt.myAtoi("+"))
