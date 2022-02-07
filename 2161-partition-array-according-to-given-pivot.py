class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, pivots, right = [], [], []
        for _ in range(len(nums)):
            n = nums.pop(0)
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                pivots.append(pivot)
        return left + pivots + right