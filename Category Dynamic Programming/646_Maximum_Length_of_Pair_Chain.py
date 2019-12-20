from typing import List
from math import inf


class Solution:
    def __init__(self):
        self.mem = {}


    def DP(self, pairs: List[List[int]], last: int) -> int:
        if last in self.mem:
            return self.mem[last]

        maxim = 0
        for pair in pairs:
            if pair[1] > last:
                break
            
            maxim = max(maxim, self.DP(pairs, pair[0] - 1) + 1)
        
        self.mem[last] = maxim
        return maxim


    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        
        return self.DP(pairs, inf)

    
if __name__ == "__main__":
    s = Solution()
    print(s.findLongestChain([[3,4], [1,2], [2,3]]))