class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicate = -1
        missing = -1

        for i in nums:
            if i in seen:
                duplicate = i
            else:
                seen.add(i)

        for i in range(1,len(nums) + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate ,missing]

        