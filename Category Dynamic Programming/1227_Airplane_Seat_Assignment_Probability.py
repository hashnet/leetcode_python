class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        else:
            return 0.5

        # # below is the iterative approach
        # occupied = 1
        # free = n-1
        # totalPos = n
        # percentage = occupied / totalPos

        # for level in range(n-1, 0, -1):
            
        #     forOccupied = occupied * level
        #     forFree = free
        #     totalPos += forOccupied - forFree
            
        #     percentage = occupied / totalPos

        #     occupied *= 2
        #     free = totalPos - occupied

        # return percentage


if __name__ == "__main__":
    s = Solution()
    print(s.nthPersonGetsNthSeat(6))
