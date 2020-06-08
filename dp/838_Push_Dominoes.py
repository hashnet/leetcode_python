class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = ["."] + list(dominoes) + ["."]
        
        isChanging = True
        while isChanging:
            isChanging = False
            changes = []

            for i in range(1, len(dom)-1):
                if dom[i] == ".":
                    if (not (dom[i-1] == "L" and dom[i+1] == "R")) and (not (dom[i-1] == "R" and dom[i+1] == "L")):
                        if dom[i+1] == "L":
                            changes.append((i, "L"))
                            isChanging = True
                        elif dom[i-1] == "R":
                            changes.append((i, "R"))
                            isChanging = True
            
            for change in changes:
                dom[change[0]] = change[1]

        return "".join(dom[1:len(dom)-1])

        
if __name__ == "__main__":
    s = Solution()
    print(s.pushDominoes(".L.R...LR..L.."))
    print(s.pushDominoes("RR.L"))