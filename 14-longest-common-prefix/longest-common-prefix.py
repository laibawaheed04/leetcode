class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for str in zip(*strs):
            if len(set(str)) == 1:
                prefix += str[0]
            else:
                break

        return prefix


        