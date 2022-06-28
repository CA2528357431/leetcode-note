class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        for i in range(len(colors)):
            if i!=0 and i!=len(colors)-1:
                if colors[i-1]==colors[i]==colors[i+1]:
                    if colors[i]=="A":
                        a+=1
                    else:
                        b+=1
        return a>b