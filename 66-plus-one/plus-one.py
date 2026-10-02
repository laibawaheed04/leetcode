class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num = num + 1
        digit = []
        for n in str(num):
            digit.append(int(n))
        
        return digit
        
        