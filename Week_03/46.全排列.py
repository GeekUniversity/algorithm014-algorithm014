class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def new(first = 0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                new(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        new()
        return res