class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for char in strs:
            res = [0]*26
            for l in char:
                res[ord(l) - ord('a')] += 1
            hashMap[tuple(res)].append(char) # had to do this so its immutable for storing key
        
        return list(hashMap.values())