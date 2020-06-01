from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        summing = [0]
        tot = 0
        for i in nums:
            tot += i
            summing.append(tot)

        memo = {}
        def DP(fr, to):
            if fr == to:
                return nums[fr]

            if (fr, to) in memo:
                return memo[(fr, to)]

            res = max(nums[fr] + (summing[to+1]-summing[fr+1]) - DP(fr+1, to), \
                nums[to] + (summing[to]-summing[fr]) - DP(fr, to-1) \
                )

            memo[(fr, to)] = res
            return res

        p1 = DP(0, len(nums)-1)
        p2 = summing[len(nums)] - p1
        return p1 >= p2

if __name__ == "__main__":
    s = Solution()
    print(s.PredictTheWinner([1, 5, 2]))
    print(s.PredictTheWinner([1, 5, 233, 7]))
