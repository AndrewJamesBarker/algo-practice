class Solution:
    # def longestCommonPrefix(self, strs: list[str]) -> str:
    #     if not strs: return ""
    #     prefix = strs[0]
    #     for str in strs[1:]:
    #         while not str.startswith(prefix):
    #             prefix = prefix[:-1]
    #             if not prefix: return ""
    #     return prefix


    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = float('inf')
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]
print(Solution().longestCommonPrefix(["flower","flow","flight"])) # fl