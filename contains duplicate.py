class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exist=set()
        for x in nums:
            if x in exist:
                return True
            exist.add(x)
        return False

        
