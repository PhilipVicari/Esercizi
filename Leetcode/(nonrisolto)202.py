class Solution:
    def isHappy(self, n: int) -> bool:
        digits= list(map(int, str(n)))
        quadrati=[]
        for n in digits:
            square= n**2
            quadrati.append(square)
        somma=sum(quadrati)
        return somma
es_202=Solution()
print(es_202.isHappy(19))