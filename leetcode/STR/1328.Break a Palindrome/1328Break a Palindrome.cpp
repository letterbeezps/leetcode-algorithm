class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.length();
        if (n==1)
            return "";
        // 将第一个不是a的字符改成a
        for (int i=0; i<n; i++)
        {
            if ((n&1) && i==n/2)  //长度未奇数，中间数不能改
                continue;
            if (palindrome[i] != 'a')
            {
                palindrome[i] = 'a';
                return palindrome;
            }
        }
        palindrome.back() = 'b';
        return palindrome;
    }
};