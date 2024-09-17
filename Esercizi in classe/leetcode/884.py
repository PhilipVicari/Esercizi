class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        l:list =[]
        New_s1=s1.split()
        New_s2=s2.split()
        for word in New_s1:
            lala= New_s1.count(word)
            if lala == 1:
                if word not in New_s2:
                    l.append(word)
        
        for words in New_s2:
            lalo= New_s2.count(words)
            if lalo == 1:
                if words not in New_s1:
                    l.append(words)
                    
                
        return l
        


es884=Solution()
print(es884.uncommonFromSentences("apple apple", "banana"))