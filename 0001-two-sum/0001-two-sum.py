class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in s:
                return [s[a],i]
            s[nums[i]] = i
