class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, num in enumerate(nums):
            sum = target - num
            if sum in ans:
                return[ans[sum], i]
            ans[num] = i
        return None