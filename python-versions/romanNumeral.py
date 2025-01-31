class Solution:
    def romanToInt(self, s: str) -> int:
        romNums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        i = 0
        numLen = len(s)
        while i < numLen:
            if i < numLen - 1 and romNums[s[i]] < romNums[s[i + 1]]:
                result += romNums[s[i + 1]] - romNums[s[i]]
                i += 2
            else:
                result += romNums[s[i]]
                i += 1
        return result

print(Solution().romanToInt("LVIII")) 