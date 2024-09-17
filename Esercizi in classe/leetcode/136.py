class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count=0
        for number in nums:
            count+=1
            if number in nums:
                count+=1
            if count==1:
                return number
            
            
            
es_136= Solution()
print(es_136.singleNumber([2,2,1]))