class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(path):

            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                helper(path)
                path.pop()
        helper([])
        return result
        