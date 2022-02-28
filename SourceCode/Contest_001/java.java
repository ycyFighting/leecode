// 暴力遍历
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j}; // 这种new但不赋值变量名的写法
                }
            }
        }
        return new int[0];
    }
}

// // 哈希表法：构造Hash表是因为Hash表的成员函数containsKey(x)可以在O(1)的时间内判断出是否存在x
// class Solution {
//     public int[] twoSum(int[] nums, int target) {
//         Map<Integer, Integer> hashtable = new HashMap<Integer, Integer>();
//         for (int i = 0; i < nums.length; ++i) {
//             if (hashtable.containsKey(target - nums[i])) {
//                 return new int[]{hashtable.get(target - nums[i]), i};
//             }
//             hashtable.put(nums[i], i); // 逐个放入再用Hash表的O(1)特点找表中是否存在，只需遍历一遍数组即可
//         }
//         return new int[0]; // 防止编译器报错，返回一个垃圾值
//     }
// }
