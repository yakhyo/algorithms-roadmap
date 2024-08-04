# solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        freq = {}
        for word in strs:
            w = "".join(sorted(word))
            if w in freq:
                freq[w].append(word)
            else:
                freq[w] = [word]
        return [x for x in freq.values()]
        