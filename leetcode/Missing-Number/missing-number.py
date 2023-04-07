import numpy as np
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = np.array(sorted(nums))
        res = len(arr)
        for x in range(len(arr)):
            if x != arr[x]:
                return x
        return res