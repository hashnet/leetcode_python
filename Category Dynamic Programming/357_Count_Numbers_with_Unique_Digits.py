class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def DP(x: int):
            if x == 0:
                return (0, 1, 1)

            if x == 1:
                return (0, 9, 10)

            res = DP(x-1)
            notUniq = (res[0] * 10) + (res[1] * (x-1))
            uniq = res[1] * (10 - (x-1))
            total = res[2] + uniq

            return (notUniq, uniq, total)

        return DP(n)[2] if n <= 10 else DP(10)[2] 


if __name__ == "__main__":
    s = Solution()
    print(s.countNumbersWithUniqueDigits(0))
    print(s.countNumbersWithUniqueDigits(1))
    print(s.countNumbersWithUniqueDigits(2))
    print(s.countNumbersWithUniqueDigits(3))
    print(s.countNumbersWithUniqueDigits(9))
    print(s.countNumbersWithUniqueDigits(10))
    print(s.countNumbersWithUniqueDigits(11))
