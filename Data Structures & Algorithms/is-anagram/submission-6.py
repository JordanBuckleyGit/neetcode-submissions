class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hMap = {}
        res = True
        if len(s) != len(t):
            return False

        for i in s:
            if i in hMap:
                hMap[i] += 1
            else:
                hMap[i] = 1

        for j in t:
            if j in hMap:
                hMap[j] -= 1
        
        for num in hMap.values():
            if num != 0:
                res = False
        return res