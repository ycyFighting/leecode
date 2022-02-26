# 暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 这个:和->是为了说明参数和返回值的数据类型，仅作提示作用
        n = len(nums)
        for i in range(n): # 从第一个数开始找
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


'''
# 暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 这个:和->是为了说明参数和返回值的数据类型，仅作提示作用
        n = len(nums)
        for i in range(n): # 从第一个数开始找
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
'''
