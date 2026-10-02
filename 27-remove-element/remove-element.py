class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        write = 0
        while i+1 <= len(nums) and i < len(nums):
            if nums[i] == val:
                i += 1
                continue
            else:
                nums[write] = nums[i]
                write += 1
                i += 1

        return write