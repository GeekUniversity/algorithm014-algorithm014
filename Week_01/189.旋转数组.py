class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        swap(nums, 0, n - 1)
        swap(nums, 0, k - 1)
        swap(nums, k, n - k - 1)


def swap(nums: List[int], l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
