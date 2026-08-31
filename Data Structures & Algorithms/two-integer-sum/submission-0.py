class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUpTable = {}
        for index in range (len(nums)):
            neededValue = target - nums[index]
            if neededValue not in lookUpTable:
                lookUpTable[nums[index]] = index
            else: 
                return [lookUpTable[neededValue],index]
