# solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        for ch in t:
            if ch not in freq:
                return False
            if freq[ch] == 0:
                return False
            freq[ch] -= 1
        return sum(freq.values()) == 0
        