from typing import List
import collections

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = collections.Counter(nums)
        l = list(m.keys())
        l.sort()
        
        memoEnds = {}

        def DPEnds(i):
            if i < 0:
                return 0

            if i in memoEnds:
                return memoEnds[i]

            if i > 0 and l[i-1] == l[i]-1:
                res = max(DPEnds(i-1), DPEnds(i-2) + l[i]*m[l[i]])
            else:
                res = DPEnds(i-1) + l[i]*m[l[i]]

            memoEnds[i] = res
            return res

        return DPEnds(len(l)-1)


if __name__ == "__main__":
    s = Solution()
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
