class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        n=len(nums)
        for right in range(1,n):
            if nums[right]!=nums[k-1]:
                nums[k]=nums[right]
                k+=1

        return k

        