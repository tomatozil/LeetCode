#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); i++) {
            int differ = target - nums[i];
            auto it = m.find(differ);
            
            if (it != m.end()) {
                answer.push_back(it->second);
                answer.push_back(i);
                break;
            } else {
                m[nums[i]] = i;
            }
        }
        return answer;
    }
};