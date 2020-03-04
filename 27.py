class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        ep = 0
        bp = len(nums) - 1

        while ep < len(nums) - bp:
            if nums[i] == val:
                tmp = nums[i]
                while nums[bp] != val:
                    
                nums[i] = nums[len(nums) - count - 1]
                nums[len(nums) - 1 - count] = tmp
                count += 1

            i += 1

        return len(nums) - count


slt = Solution()
print(slt.removeElement([3, 2, 2, 3], 3))
