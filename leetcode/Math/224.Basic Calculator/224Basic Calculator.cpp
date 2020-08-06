class Solution {
public:
    
    void calc(stack<char> &op, stack<int> &num)
    {
        int y = num.top();
        num.pop();
        int x = num.top();
        num.pop();
        if (op.top() == '+') num.push(x+y);
        else num.push(x-y);
        op.pop();
    }
    
    int calculate(string s) {
        stack<char> op;
        stack<int> num;
        
        for (int i = 0; i<s.size(); i++)
        {
            char c = s[i];
            if (c==' ') continue;
            if (c == '(' || c == '+' || c == '-') op.push(c);
            else if (c == ')')
            {
                op.pop();
                if (!op.empty() && op.top() != '(')
                {
                    calc(op, num);
                }
            }
            else
            {
                int j = i;
                while (j<s.size() && isdigit(s[j])) j++;
                num.push(atoi(s.substr(i, j-i).c_str()));
                i = j-1;
                if (!op.empty() && op.top() != '(')
                {
                    calc(op, num);
                }
            }
        }
        return num.top();
    }
};