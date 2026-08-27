class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in t:
            if char not in d:
                return False
            if d[char] == 1:
                del d[char]
            else:
                d[char]-=1
        return not d
