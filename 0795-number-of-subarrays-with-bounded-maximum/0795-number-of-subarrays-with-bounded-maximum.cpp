class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int invalid = -1, valid = -1, sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > right)
                invalid = i;
            if (left <= nums[i] && nums[i] <= right)
                valid = i;
            
            sum += max(0, valid - invalid);
        }

        return sum;
    }
};