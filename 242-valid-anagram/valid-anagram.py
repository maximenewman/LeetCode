class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        s = list(s)
        t = list(t)
        print(s)
        print(t)
        t.sort()
        s.sort()
        return t == s