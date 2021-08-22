class Solution:
    def escapeGhosts(self, ghosts, target) -> bool:
        mydis = abs(target[0])+abs(target[1])
        ghodisli = [abs(x-target[0])+abs(y-target[1]) for x,y in ghosts]
        ghodis = min(ghodisli)
        return mydis<ghodis

# 最终都是要到target-->让ghost往target走，看ghost和hero谁先到
