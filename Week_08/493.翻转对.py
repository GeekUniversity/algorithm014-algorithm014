class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return self.mergesort(nums, 0, len(nums) - 1)

    def mergesort(self, nums, l, r):
        if l >= r: return 0
        mid = int(l + (r - l) / 2)
        count = self.mergesort(nums, l, mid) + self.mergesort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i = l
        t = l
        c = 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] <= 2 * nums[j]:
                i += 1
            while t <= mid and nums[t] < nums[j]:
                cache[c] = nums[t]
                c += 1
                t += 1
            cache[c] = nums[j]
            count += mid - i + 1
            c += 1
        while t <= mid:
            cache[c] = nums[t]
            c += 1
            t += 1
        nums[l:r + 1] = cache[:]
        return count
