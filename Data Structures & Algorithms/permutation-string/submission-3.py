class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        need={}
        window={}
        left=0
        valid=0
        for c in s1:
            need[c]=need.get(c,0)+1
        for right in range(len(s2)):
            c = s2[right]
            if c in need:
                window[c]=window.get(c,0)+1
                if window[c]==need[c]:
                    valid+=1
            if right-left+1>len(s1):
                d=s2[left]
                left+=1
                if d in need:
                    if need[d]==window[d]:
                        valid-=1
                    window[d]-=1
            if valid == len(need):
                return True
        return False
                    