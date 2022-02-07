class Solution:
    def minimumSum(self, num: int) -> int:
        from itertools import permutations, combinations
        num = list(str(num))
        sums = set()
        for sss in permutations(num, 3):
            new1 = int(''.join(sss))
            new2 = num[:]
            [new2.remove(s) for s in sss]
            sums.add(new1 + int(new2[0]))
        for ss in permutations(num, 2):
            new1 = int(''.join(ss))
            new2 = num[:]
            [new2.remove(s) for s in ss]
            sums.add(new1 + int(new2[0] + new2[1]))
            sums.add(new1 + int(new2[1] + new2[0]))
        return min(sums)