class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        l = 0
        k = k % n
        r = len(nums) - 1
        def reverse(l,r):
            while (l < r) :

                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
                r -= 1
        
        reverse(0, n-1)

        reverse(0 ,k-1)

        reverse(k, n-1)
        