from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def DP(idx: int) -> int:
            if idx < 0:
                return 0

            if idx in memo:
                return memo[idx]

            res = max((nums[idx] + DP(idx-2), DP(idx-1)))
            memo[idx] = res
            return res

        return DP(len(nums) - 1)

if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))