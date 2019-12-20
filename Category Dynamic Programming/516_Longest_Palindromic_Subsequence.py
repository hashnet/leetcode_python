class Solution:
    def __init__(self):
        self.mem = {}


    def DP(self, s: str, start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return 1
        
        if (start, end) in self.mem:
            return self.mem[(start, end)]

        if(s[start] == s[end]):
            res =  2 + self.DP(s, start+1, end-1)
        else:
            res = max(self.DP(s, start, end-1), self.DP(s, start+1, end))

        self.mem[(start, end)] = res
        return res


    def longestPalindromeSubseq(self, s: str) -> int:
        return self.DP(s, 0, len(s)-1)


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))