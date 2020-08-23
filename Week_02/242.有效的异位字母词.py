class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        temp = set(s)
        if temp == set(t):
            for i in temp:
                result = result and s.count(i) == t.count(i)
            return result
        else:
            return False