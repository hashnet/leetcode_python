class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mem = {}
        mod = 10**9 + 7

        def DP(d:int , target: int) -> int:
            if d == 1:
                if target <= f:
                    return 1
                else:
                    return 0

            if (d, target) in mem:
                return mem[(d, target)]

            sum = 0
            for i in range(min(f, target-1), 0, -1):
                sum += DP(d-1, target - i)
                sum %=  mod

            mem[(d, target)] = sum
            return sum

        return DP(d, target)


if __name__ == "__main__":
    s = Solution()
    print(s.numRollsToTarget(d = 1, f = 6, target = 3))
    print(s.numRollsToTarget(d = 2, f = 6, target = 7))
    print(s.numRollsToTarget(d = 2, f = 5, target = 10))
    print(s.numRollsToTarget(d = 1, f = 2, target = 3))
    print(s.numRollsToTarget(d = 30, f = 30, target = 500))
