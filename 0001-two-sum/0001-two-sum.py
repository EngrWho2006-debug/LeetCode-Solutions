class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining],i]
            seen[nums[i]] = i    
        nums = [2,7,11,15]
        target = 9
        print(twoSum(self, nums, target))        
        