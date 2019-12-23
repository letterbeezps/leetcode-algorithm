class Solution {
public:
    bool isPowerOfThree(int n) {
        // 1162261467是2^31内最大的3的整次幂
        return n > 0 && 1162261467 % n == 0;
    }
};