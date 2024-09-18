class Solution:
    def longestCommonPrefix(self, words: list[str]) -> str:
        w_p1=0
        w_p2=0
        w_p3=0
        while w_p1 < len(words[0]) and w_p2 < len(words[1]) and w_p3 < len(words[2]):
            if w_p1==w_p2==w_p3:
                w_p1+=1
                w_p2+=1
                w_p3+=1
                break           
            return True

es_14=Solution()
print(es_14.longestCommonPrefix(["flower","flow","flight"]))
