class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sum=0
        result=[]
        for i in range(n):
            sum+=nums[i]
            result.append(sum)
        return result
        
