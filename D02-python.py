class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expectedSum = ((0+(len(nums)) * (len(nums) + 1) ))/2
        
        for i in range(0,len(nums),1):
            expectedSum -= nums[i]
        
        return int (expectedSum)

        #time 0(n)  space 0(1)
