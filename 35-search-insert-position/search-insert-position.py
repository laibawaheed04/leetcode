class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = -1
        for i in range(len(nums)):
            if target < nums[0]:
                return 0
            
            index = -1
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                else:
                    if target > nums[i]:
                        index = i+1
                    else:
                        index = i
                        break
                
            return index
    
        