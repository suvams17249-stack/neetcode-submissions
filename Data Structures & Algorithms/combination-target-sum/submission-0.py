class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(i,path,current_sum):

            if current_sum == target:
                result.append(path.copy())
                return
            if i >= len(nums) or current_sum > target:
                return
            path.append(nums[i])

            helper(i,path,current_sum + nums[i])

            path.pop()

            helper(i+1,path,current_sum)
        helper(0,[],0)
        return result
        

        