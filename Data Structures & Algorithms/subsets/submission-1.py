class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def helper(i,temp):
            if i == len(nums):
                result.append(temp[:])
                return
            temp.append(nums[i])
            helper(i+1,temp)

            temp.pop()
            helper(i+1,temp)
        helper(0,[])
        return result



        