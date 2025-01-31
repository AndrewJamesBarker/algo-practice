class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        mergedList = []
        
        while pointer1 < len(word1) or pointer2 < len(word2):
            if pointer1 < len(word1):
                mergedList.append(word1[pointer1])
                pointer1 += 1
            if pointer2 < len(word2):
                mergedList.append(word2[pointer2])
                pointer2 += 1
        
        return "".join(mergedList)
    
print(Solution().mergeAlternately("abcd", "pqrst"))