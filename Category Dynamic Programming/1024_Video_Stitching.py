from typing import List
from math import inf

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        memo = {}
        
        def DP(end):
            if end <= 0:
                return 0

            if end in memo:
                return memo[end]

            minim = inf
            for clip in clips:
                if clip[0] < end and clip[1] >= end:
                    minim = min(minim, DP(clip[0])+1)
        
            memo[end] = minim
            return minim

        result = DP(T)
        if result == inf:
            return -1
        else:
            return result
if __name__ == "__main__":
    s = Solution()
    print(s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10))
    print(s.videoStitching([[0,1],[1,2]], T = 5))
    print(s.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9))
    print(s.videoStitching([[0,4],[2,8]], T = 5))
