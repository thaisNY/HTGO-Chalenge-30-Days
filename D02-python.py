class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash = {}
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        for char in t:
            if char not in hash or hash[char] == 0:
                return False
            else:
                hash[char] -= 1

        return True
