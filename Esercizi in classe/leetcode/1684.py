class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        consistente = 0
        for word in words:
            for l in word:
                if l in allowed:
                    consistente += 1
        return consistente
            
        
        
es_1684=Solution()
print(es_1684.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))