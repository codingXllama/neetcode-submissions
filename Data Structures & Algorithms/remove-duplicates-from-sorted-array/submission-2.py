class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        k=1
        for fast in range (len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
                k+=1
        return slow+1
