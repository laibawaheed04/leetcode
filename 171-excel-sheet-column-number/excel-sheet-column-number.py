class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for char in columnTitle.upper():
            num = num * 26 + (ord(char) - 64)
        
        return num
        