class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx!=ty and tx>sx and ty>sy:
            if tx>ty:
                tx = tx%ty
            else:
                ty = ty%tx
        if tx==sx and ty==sy:
            return True
        if tx==sx:
            if ty>sy and (ty-sy)%tx == 0:
                return True
            else:
                return False
        if ty==sy:
            if tx>sx and (tx-sx)%ty == 0:
                return True
            else:
                return False
        return False