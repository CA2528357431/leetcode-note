class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {score[i]:i for i in range(len(score))}
        score.sort(reverse=True)
        res = [""]*len(score)
        for i in range(len(score)):
            index = dic[score[i]]
            if i==0:
                res[index] = "Gold Medal"
            elif i==1:
                res[index] = "Silver Medal"
            elif i==2:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(i+1)
        return res