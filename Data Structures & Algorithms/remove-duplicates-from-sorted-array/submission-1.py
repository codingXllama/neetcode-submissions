class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowPtr=0
        fastPtr=0
        uniqueValue=1

        while fastPtr<len(nums):
            if nums[fastPtr]==nums[slowPtr]:
                fastPtr+=1
            else:
                slowPtr+=1
                nums[slowPtr]=nums[fastPtr]
                uniqueValue+=1
        return uniqueValue
