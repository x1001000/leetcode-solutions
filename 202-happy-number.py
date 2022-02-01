class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        while n not in history and n != 1:
            history.append(n)
            n = sum(map(lambda x: int(x)**2, str(n)))
        return True if n == 1 else False
