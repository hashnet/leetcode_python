from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def DP(idx):
            if idx in memo:
                return memo[idx]
        
            maxim = 0
            if idx != 0:
                for i in range(idx):
                    if nums[i] < nums[idx]:
                        maxim = max(maxim, DP(i))

            maxim += 1
            memo[idx] = maxim
            return maxim

        maxim = 0
        for i in range(len(nums)):
            maxim = max(maxim, DP(i))

        return maxim

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))