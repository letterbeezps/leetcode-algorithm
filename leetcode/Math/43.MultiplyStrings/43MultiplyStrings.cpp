//高精度乘法题
class Solution {
public:
    string multiply(string num1, string num2) {
        vector<int> product(num1.size() + num2.size(), 0);
        for (int i=0; i<num1.size(); i++)
            for (int j=0; j<num2.size(); j++)
                product[num1.size()-i+num2.size()-j-2] += (num1[i]-'0')*(num2[j]-'0');
        int t = 0;
        for (int i=0; i<product.size(); i++)
        {
            int &x = product[i];
            t += x;
            x = t % 10;
            t /= 10;
        }
        string res;
        int k = product.size()-1;
        while (!product[k] && k>0) k--;
        for (int i=k; i>=0; i--) res += to_string(product[i]);
        return res;
    }
};