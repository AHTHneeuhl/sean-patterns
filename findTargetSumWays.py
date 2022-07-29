class Solution:
    # Time - O(t*N) | Space - O(t*N)
    def findTargetSumWays(self, nums, target):
        self.memo = dict()
        n, total = len(nums) - 1, 0
        return self.solve(nums, target, n, total)

    def solve(self, nums, target, n, total):
        if (n, total) in self.memo:
            return self.memo[(n, total)]
        if n < 0 and total == target:
            return 1
        if n < 0:
            return 0

        pos = self.solve(nums, target, n - 1, total + nums[n])
        neg = self.solve(nums, target, n - 1, total - nums[n])
        self.memo[(n, total)] = pos + neg

        return self.memo[(n, total)]
