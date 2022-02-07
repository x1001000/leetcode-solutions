class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(m, s, startAt):
            cost = 0
            digits = f'{m:2d}{s:2d}'.replace(' ', '0').lstrip('0')
            for d in map(int, digits):
                if d == startAt:
                    cost += pushCost
                else:
                    cost += pushCost + moveCost
                startAt = d
            return cost
        m, s = targetSeconds//60, targetSeconds%60
        m, s = (m, s) if m < 100 else (m-1, s+60)
        return min(cost(m, s, startAt), cost(m-1, s+60, startAt)) if m > 0 and s < 40 else cost(m, s, startAt)