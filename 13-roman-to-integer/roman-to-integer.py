class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
        int_value = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and conversion_dict[s[i]] <  conversion_dict[s[i+1]]:
                int_value += conversion_dict[s[i+1]] - conversion_dict[s[i]]
                i += 2
            else:
                int_value += conversion_dict[s[i]]
                i += 1

        return int_value


