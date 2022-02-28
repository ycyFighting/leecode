// 暴力遍历
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> a; // 建立hash表存放数组元素
        vector<int> b(2,-1); // 创建一个vector，元素个数为2，且值均为-1
        for (int i = 0; i < nums.size(); i++){
            // 将键值对插入map，插入的元素类型是pair value_type是占位类型，是pair<const string, int>
            a.insert(pair<int, int>(nums[i],i)); 
        }
        for (int i=0; i < nums.size(); i++){
            // map.count()返回指定元素出现的次数；并且不是自己本身
            if (a.count(target - nums[i]) > 0 && (a[target - nums[i]] != i)) {
                b[0] = i;
                b[1] = a[target - nums[i]];
                break;
            }
        }
        return b;
    }
};

// Hash表法
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]); // 通过给定主键查找元素,没找到：返回unordered_map::end
            if (it != hashtable.end()) { // 不等于即找到了结果
                return {it->second, i}; // it->second即value值
            }
            hashtable[nums[i]] = i; // 存入Hash表<key, value>为<nums[i], i>
        }
        return {}; // 即返回这个函数(vector/String)所构造出来的对象
    }
};
