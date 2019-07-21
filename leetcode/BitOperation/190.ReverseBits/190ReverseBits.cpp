class Solution {
public:
    // this is a general solution
    // 虽然也有神仙做法，这里就不写了
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i = 0; i < 32; i++) {
            int t = 1 & (n >> i);
            // cout << t << endl;
            res += t;
            if (i < 31)
                res = res << 1;
        }
        return res;
    }
};