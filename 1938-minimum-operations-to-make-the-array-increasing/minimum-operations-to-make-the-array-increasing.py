class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                operations += increment
                nums[i] = nums[i - 1] + 1

        return operations
