class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if nums is None or len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            bp = i + 1
            ep = len(nums) - 1

            while bp < ep:
                tmp = nums[bp] + nums[ep] + nums[i]
                if tmp == 0:
                    result.append([nums[i], nums[bp], nums[ep]])
                    bp += 1
                    ep -= 1
                elif tmp > 0 and ep > i:
                    ep -= 1
                    continue
                elif tmp < 0 and bp < i:
                    bp += 1
                    continue
                else:
                    break

        return result



slt = Solution()

print(slt.threeSum([-1, 0, 1, 2, -1, -4]))