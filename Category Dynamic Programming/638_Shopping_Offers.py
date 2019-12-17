from typing import List, Tuple


class Solution:
    def __init__(self):
        self.mem = {}


    def DP(self, remaining: Tuple[int]) -> int:
        if remaining in self.mem:
            return self.mem[remaining]

        minim = 0
        for i in range(self.itemCount):
            minim += remaining[i] * self.price[i]

        for discount in self.special:
            # Check if we can apply the discount
            discounted = True
            for i in range(self.itemCount):
                if discount[i] > remaining[i]:
                    discounted = False
                    break
            if discounted:
                newRemaining = tuple([remaining[i] - discount[i] for i in range(self.itemCount)])
                minim = min(minim, self.DP(newRemaining) + discount[-1])

        self.mem[remaining] = minim
        return minim


    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.itemCount = len(price)
        self.price = price
        self.special = special

        return self.DP(tuple([i for i in needs]))
    

if __name__ == '__main__':
    s = Solution()
    print(s.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))
    print(s.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))