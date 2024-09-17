class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        N_heights = sorted(heights)
        count= 0

        for i in range(len(heights)):
            if heights[i] != N_heights[i]:
                    count+=1
                
        return count

es1051=Solution()
print(es1051.heightChecker([1,1,4,2,1,3]))