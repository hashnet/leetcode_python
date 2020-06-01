class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        mid = (N-1)/2

        def translate(x, y):
            if x > mid:
                x = int(mid + mid - x)
            
            if y > mid:
                y = int(mid + mid - y)

            return (x, y)


        memo = {}
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        def DP(x, y, k):
            if k <= 0:
                return 1

            if (x, y, k) in memo:
                return memo[(x, y, k)]
            
            probab = 0
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]

                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    (nx, ny) = translate(nx, ny)
                    probab += DP(nx, ny, k-1)

            memo[(x, y, k)] = probab
            return probab

        if K == 0:
            return 1.0
        else:
            result = DP(r, c, K)
            result /= (8**K)
            return result
if __name__ == "__main__":
    s = Solution()
    print(s.knightProbability(3, 1, 1, 2))      #0.25
    print(s.knightProbability(3, 2, 0, 0))      #0.0625
    print(s.knightProbability(1, 0, 0, 0))      #1.0
    print(s.knightProbability(1, 1, 0, 0))      #0.0