# 暴力遍历
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # :和->仅是对数据类型的解释
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []


# Hash表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict() # dict也是一种{key:value}结构
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        for i, num in enumerate(nums): 
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return [] # 同c++
