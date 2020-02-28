class Solution(object):
    def checkPalindrome(self, s, dp, i, j):
        if dp[i][j] is None:
            check = False

            if j - i >= 2:
                checked = self.checkPalindrome(s, dp, i + 1, j - 1)
            else:
                checked = True

            if checked is True:
                if s[i] == s[j]:
                    checked = True
                else:
                    checked = False

            dp[i][j] = checked

            return checked
        else:
            return dp[i][j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        maxone = ""

        if len(s) == 1:
            return s

        dp = []
        sp = {}

        for i in range(len(s)):
            dp.append(list())
            for i in range(len(s)):
                dp[i].append(list())

        #init
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)):
            if i + 1 < len(dp[i]):
                dp[i][i+1] = 1

        for i in range(3, len(s)):
            

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.checkPalindrome(s, dp, i, j):
                    nowlen = j - i + 1
                    if nowlen >= length:
                        length = nowlen
                        maxone = s[i : j + 1]

        return maxone



slt = Solution()

print(slt.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"))