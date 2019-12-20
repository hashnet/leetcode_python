class Solution:
    def numTrees(self, n: int) -> int:
        mem = {}

        def DP(n: int) -> int:
            if n == 0:
                return 0

            if n == 1:
                return 1

            if n in mem:
                return mem[n]

            sum = 2 * DP(n-1)
            for i in range(n-1):
                sum += DP(i) * DP(n-1-i)

            mem[n] = sum
            return sum


        return DP(n)


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))