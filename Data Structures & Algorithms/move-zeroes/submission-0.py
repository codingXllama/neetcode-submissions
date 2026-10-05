class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftPtr=0
        for rightPtr in range(len(nums)):
            if nums[rightPtr]!=0:
                nums[leftPtr],nums[rightPtr]=nums[rightPtr],nums[leftPtr]
                leftPtr+=1
