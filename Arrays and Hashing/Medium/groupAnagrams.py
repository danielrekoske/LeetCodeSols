class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            dna = [0]*26
            for char in word:
                dna[ord(char)-ord('a')] +=1
            res[tuple(dna)].append(word)

        return res.values()