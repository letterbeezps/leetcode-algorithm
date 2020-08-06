class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26, 0);
        for (const char task : tasks)
        {
            ++count[task - 'A'];
        }
        int max_count = *max_element(count.begin(), count.end());
        size_t ans = (max_count - 1) * (n+1);
        ans += count_if(count.begin(), count.end(),
                       [max_count](int c){return c == max_count;});
        
        return max(tasks.size(), ans);
    }
};