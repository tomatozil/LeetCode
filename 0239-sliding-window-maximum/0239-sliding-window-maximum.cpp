class Solution {
public:

    class MaxPosition {
    public:
        int num;
        int pos;
        MaxPosition(int num, int pos): num(num), pos(pos) {}
    };

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return {};

        deque<int> dq;
        vector<int> answer;

        for (int i = 0; i < n; ++i) {
            if (!dq.empty() && dq.front() == i - k)
                dq.pop_front();
            
            while (!dq.empty() && nums[dq.back()] <= nums[i])
                dq.pop_back();

            dq.push_back(i);

            if (i + 1 >= k)
                answer.push_back(nums[dq.front()]);
        }

        return answer;
    }

private:

    MaxPosition findMax(vector<int>& nums, int start, int end) {
        int num = nums[start];
        int idx = start;
        for(int i = start+1; i <= end; ++i) {
            if (num < nums[i]) {
                num = nums[i];
                idx = i;
            }
        }

        return MaxPosition(num, idx);
    }
};