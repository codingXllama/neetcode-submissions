class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myFrequent_addiction = {}
    
        for item in nums:
            if item in myFrequent_addiction:
                return True
            else:
                myFrequent_addiction[item] = 1

        return False