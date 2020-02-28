class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""

        if len(strs) == 0:
            return result

        min_l = len(strs[0])
        for str in strs:
            min_l = min(len(str), min_l)

        for i in range(min_l):
            val = strs[0][i]
            for str in strs:
                if str[i] != val:
                    return result

            result += val

        return result
