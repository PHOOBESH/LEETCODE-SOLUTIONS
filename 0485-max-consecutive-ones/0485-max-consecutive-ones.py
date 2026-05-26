class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0

        for x in nums:
            if x == 1:
                count += x
                maxi = max(maxi,count)

            else:
                count = 0

        return maxi