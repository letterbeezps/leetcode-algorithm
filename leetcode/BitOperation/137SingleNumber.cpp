/*
python int是无限大
C++    int 2^32
从二进制的角度考虑问题
*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int bit = 0; bit < 32; bit++) {  // Bit代表位数，C++里int 最大2^32
            int counter = 0;
            for (int i = 0; i < nums.size(); i++ ) {
                counter += (nums[i] >> bit) & 1;
            }
            res += (counter % 3) << bit;  // 这一步可以排除重复出现三次的数
        } 
        return res;
    }
};

//////////////////////////////////////////////////
//python3
//////////////////////////////////////////////////
'''
考虑二进制形式的每一位
ones = 0 twos = 0
0个1   0 0
1个1   1 0   返回状态2的ones
2个1   0 1
3个1   0 0
自动机
简直神仙写法
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        #end_for
        return ones