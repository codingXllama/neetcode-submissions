class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rightPtr=0
        leftPtr=0
        while rightPtr<len(nums):
            if nums[rightPtr]!=0:
                nums[leftPtr],nums[rightPtr]= nums[rightPtr],nums[leftPtr]
                leftPtr+=1
            rightPtr+=1
            