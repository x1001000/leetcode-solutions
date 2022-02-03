class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = []
        while n not in cycle and n != 1:
            cycle.append(n)
            n = sum(map(lambda x: int(x)**2, str(n)))
        return True if n == 1 else False
