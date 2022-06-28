class Solution:
    def lengthLongestPath(self, string: str) -> int:

        stack = []
        ls = string.split("\n")


        big = 0
        pre = 0
        for l in ls:
            cnt = 0
            for c in l:
                if c!="\t":
                    break
                else:
                    cnt+=1
            while len(stack)!=cnt:
                pre-=stack.pop()+1
            stack.append(len(l)-cnt)
            pre += len(l)-cnt+1
            if "." in l:
                big = max(big,pre)
        return max(big-1,0)